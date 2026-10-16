"""Static Phase6 consistency/declared-traceability checks. Never executes OpsHub."""
from pathlib import Path
import copy,datetime,hashlib,json,re,sys
from collections import Counter
import jsonschema
from inventory_sources import derive
from render_plan import digest

ROOT=Path(__file__).resolve().parents[2]
def read(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def sha(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()

def validate(m,coverage,gates,inventory,files=True):
    errors=[]
    def fail(code,detail): errors.append({'code':code,'detail':detail})
    schema=read('docs/implementation/task-manifest.schema.json')
    for e in jsonschema.Draft202012Validator(schema).iter_errors(m): fail('SCHEMA',str(list(e.path))+': '+e.message)
    ids=[t['id'] for t in m['tasks']]; by={t['id']:t for t in m['tasks']}; gs={g['id']:g for g in gates['gates']}
    if len(ids)!=len(set(ids)): fail('DUPLICATE_TASK','Task IDs must be unique')
    if len(gs)!=len(gates['gates']): fail('DUPLICATE_GATE','Gate IDs must be unique')
    ancestors={tid:set() for tid in by}
    for t in m['tasks']:
        for d in t['dependencies']:
            if d not in by: fail('DANGLING_DEPENDENCY',t['id']+' -> '+d)
            if d==t['id']: fail('SELF_DEPENDENCY',t['id'])
            if d in by: ancestors[t['id']].add(d)
        if len(t['dependencies'])!=len(set(t['dependencies'])): fail('DUPLICATE_DEPENDENCY',t['id'])
    changed=True
    while changed:
        changed=False
        for tid,aset in ancestors.items():
            new=set().union(*(ancestors[d] for d in list(aset))) if aset else set()
            if not new<=aset: aset.update(new); changed=True
    if any(tid in aset for tid,aset in ancestors.items()): fail('CYCLE','Dependency graph contains a cycle')
    order=m['topological_order']; rank={tid:i for i,tid in enumerate(order)}
    if len(order)!=len(ids) or set(order)!=set(ids): fail('TOPOLOGICAL_COVERAGE','Order must contain every task exactly once')
    for t in m['tasks']:
        if any(rank.get(d,10**9)>=rank.get(t['id'],-1) for d in t['dependencies']): fail('PREDECESSOR_ORDER',t['id'])
        if set(c['task_id'] for c in t['consumed_contracts'])!=set(t['dependencies']): fail('CONTRACT_DEPENDENCIES',t['id'])
        for c in t['consumed_contracts']:
            if c['task_id'] in by and c['contract_id'] not in {x['id'] for x in by[c['task_id']]['produced_contracts']}: fail('UNDEFINED_CONTRACT',t['id']+' '+c['contract_id'])
        if not t['requirement_ids'] and not t['validation_contract_ids']: fail('UNJUSTIFIED_TASK',t['id'])
        if t['complexity']=='XL' and not t['complexity_rationale']: fail('UNJUSTIFIED_XL',t['id'])
        if t['status']=='NOT_STARTED' and t['completion_evidence_refs']: fail('FALSE_COMPLETION_EVIDENCE',t['id'])
        if t['status']=='ACCEPTED' and not t['completion_evidence_refs']: fail('MISSING_COMPLETION_EVIDENCE',t['id'])
        if m['approval_status']=='PHASE6_NOT_APPROVED_IMPLEMENTATION_NOT_AUTHORIZED' and (t['status']!='NOT_STARTED' or t['readiness']!='WAITING_AUTHORIZATION'): fail('APPROVAL_BOUNDARY',t['id'])
        if not any(x['gate_id']=='G-P6' and x['stage']=='START' for x in t['decision_gates']): fail('IMPLEMENTATION_PERMISSION',t['id'])
        for ref in t['decision_gates']:
            if ref['gate_id'] not in gs: fail('UNKNOWN_GATE',t['id']+' '+ref['gate_id']); continue
            if {'task_id':t['id'],**ref} not in gs[ref['gate_id']]['applications']: fail('GATE_APPLICATION',t['id']+' '+ref['gate_id'])
        for lock in t['execution_claim']['locks']:
            if lock not in t['shared_change_locks']: fail('UNDECLARED_CLAIM_LOCK',t['id']+' '+lock)
        if t['type'] in ('OWNER_DECISION','OPERATIONAL_RELEASE') and t['accountable_role']=='IMPLEMENTING_AGENT_WITH_INDEPENDENT_REVIEWER': fail('WRONG_ACCOUNTABLE_ROLE',t['id'])
        if t['effect_class']!='LOCAL_REVERSIBLE' and t['type']!='OWNER_DECISION':
            if not any(gs.get(r['gate_id'],{}).get('category')=='AUTHORIZATION' and r['gate_id']!='G-P6' for r in t['decision_gates']): fail('MISSING_EFFECT_AUTHORIZATION',t['id'])
        if files:
            p=ROOT/t['task_spec']
            if not p.is_file(): fail('TASK_FILE',t['id']); continue
            text=p.read_text(encoding='utf-8')
            for marker in (f"identity: {t['id']}; milestone: {t['milestone']}; status: {t['status']}",'dependencies: '+','.join(t['dependencies']),f"manifest-digest: {m['plan_digest']}"):
                if marker not in text: fail('TASK_VIEW_DRIFT',t['id']+' '+marker)
            for item in t['test_requirements']+t['acceptance_criteria']:
                if item['id'] not in text: fail('TASK_ASSERTION_DRIFT',t['id']+' '+item['id'])
            for s in t['spec_refs']:
                if not (ROOT/s['path']).is_file(): fail('SPEC_PATH',t['id']+' '+s['path']); continue
                if sha(s['path'])!=s['sha256']: fail('SPEC_DIGEST',t['id']+' '+s['path'])
                lines=(ROOT/s['path']).read_text(encoding='utf-8').splitlines()
                if s['line']>s['end_line'] or s['end_line']>len(lines): fail('SPEC_RANGE',t['id']+' '+s['path'])
                elif lines[s['line']-1].lstrip('# ').strip()!=s['section'].lstrip('# ').strip(): fail('SPEC_LOCATOR',t['id']+' '+s['path']+':'+str(s['line']))
    expected={r['id']:r for r in inventory['requirements']}; rows={r['requirement_id']:r for r in coverage['mappings']}
    if set(expected)!=set(rows) or len(rows)!=len(coverage['mappings']): fail('COVERAGE_INVENTORY','Independent source inventory and mapping IDs differ')
    for rid,row in rows.items():
        if rid not in expected: continue
        r=expected[rid]
        if (row['source'],row['source_line'],row['source_locator'])!=(r['source'],r['line'],r['locator']): fail('COVERAGE_SOURCE',rid)
        if not row['task_ids']: fail('MISSING_COVERAGE',rid)
        reverse={t['id'] for t in m['tasks'] if rid in t['requirement_ids']+t['validation_contract_ids']}
        if reverse!=set(row['task_ids']): fail('COVERAGE_REVERSE',rid)
        tests={x['id'] for tid in row['task_ids'] if tid in by for x in by[tid]['test_requirements']}
        criteria={x['id'] for tid in row['task_ids'] if tid in by for x in by[tid]['acceptance_criteria']}
        if not set(row['test_refs'])<=tests or not row['test_refs']: fail('COVERAGE_TEST_REFERENCE',rid)
        if not set(row['acceptance_refs'])<=criteria or not row['acceptance_refs']: fail('COVERAGE_ACCEPTANCE_REFERENCE',rid)
        if not set(row['release_gates'])<=set(gs) or not row['release_gates']: fail('COVERAGE_GATE',rid)
    for t in m['tasks']:
        if not set(t['requirement_ids']+t['validation_contract_ids'])<=set(expected): fail('UNKNOWN_REQUIREMENT',t['id'])
    decision_ids={r['id'] for r in inventory['decisions']}
    if not decision_ids<=set(gs): fail('MISSING_DECISION_GATE',str(decision_ids-set(gs)))
    for gid in decision_ids:
        if not gs[gid]['applications']: fail('UNMAPPED_DECISION_GATE',gid)
        if not gs[gid]['responsible_decision_maker'] or gs[gid]['responsible_decision_maker'].startswith(gid): fail('GATE_ACCOUNTABILITY',gid)
    excluded={r['id'] for r in inventory['deferred_excluded']}
    if {r['id'] for r in coverage['deferred_excluded']}!=excluded: fail('EXCLUSION_INVENTORY','Deferred/excluded source inventory differs')
    if any(excluded&set(t['requirement_ids']+t['validation_contract_ids']) for t in m['tasks']): fail('DEFERRED_FEATURE','A task claims a deferred/excluded requirement')
    for milestone in m['milestones']:
        if set(milestone['task_ids'])!={t['id'] for t in m['tasks'] if t['milestone']==milestone['id']}: fail('MILESTONE_MEMBERSHIP',milestone['id'])
    if sum(len(x['task_ids']) for x in m['milestones'])!=len(ids): fail('MILESTONE_TOTAL','Task totals disagree')
    prior=set()
    for tid in m['first_runway']:
        if tid not in by or not set(by[tid]['dependencies'])<=prior: fail('RUNWAY_DEPENDENCY',tid)
        prior.add(tid)
    if m['first_runway'][0]!='T0001' or by['T0001']['dependencies']: fail('FIRST_TASK','T0001 must remain the small no-predecessor repository task')
    # Strong obligations are explicit task ancestry, not a keyword mention in a plan.
    safety={
      'T0707':{'T0711','T0706','T0608','T0609','T1202','T1205','T0308'},
      'T0708':{'T0712','T0706','T0608','T0609','T1202','T1205','T0405'},
      'T0709':{'T0713','T0706','T0608','T0609','T1202','T1205','T0308'},
      'T0710':{'T0714','T0706','T0608','T0609','T1202','T1205','T0308'},
      'T1301':{'T0701','T0608','T0609','T1202','T1205','T1207','T1108'},
      'T1302':{'T1301','T0707','T0708','T0709','T0710'},
      'T1303':{'T0507','T0504','T0606','T0209','T1202','T1205','T1108','T1207'},
      'T1205':{'T1208','T0210','T0609','T1106'},
      'T1207':{'T1211','T1210','T1209','T0308','T0405','T0914','T1108','T1205'},
      'T1306':{'T1305','T1304','T1302','T1303','T1207','T1210'}}
    for tid,needed in safety.items():
        if tid not in by or not needed<=ancestors[tid]: fail('SAFETY_PREDECESSOR',tid+': '+str(sorted(needed-ancestors.get(tid,set()))))
    for gate in gates['gates']:
        if 'required_task_ids' in gate and not set(gate['required_task_ids'])<=set(by): fail('GATE_PROOF_TASK',gate['id'])
        for app in gate['applications']:
            if app['task_id'] not in by or {k:v for k,v in app.items() if k!='task_id'} not in by[app['task_id']]['decision_gates']: fail('GATE_REVERSE',gate['id'])
    pairs=read('docs/implementation/parallel-safety.json')['pairs']
    active=[t for t in m['tasks'] if t['execution_claim']['owner']]
    candidates=[(p['task_ids'][0],p['task_ids'][1]) for p in pairs]+[(a['id'],b['id']) for i,a in enumerate(active) for b in active[i+1:]]
    for a,b in candidates:
        if a not in by or b not in by: fail('PARALLEL_TASK','Unknown parallel task'); continue
        if a in ancestors[b] or b in ancestors[a]: fail('PARALLEL_DEPENDENCY',a+' '+b)
        if 'SERIAL' in (by[a]['parallelism'],by[b]['parallelism']): fail('PARALLEL_CLASSIFICATION',a+' '+b)
        if set(by[a]['shared_change_locks'])&set(by[b]['shared_change_locks']): fail('SHARED_LOCK',a+' '+b)
        for x in by[a]['editable_areas']:
            for y in by[b]['editable_areas']:
                if x==y or x.startswith(y.rstrip('/')+'/') or y.startswith(x.rstrip('/')+'/'): fail('OVERLAPPING_EDIT_AREA',a+' '+b+' '+x+' '+y)
    if files:
        if m['plan_digest']!=digest(m): fail('PLAN_DIGEST','Manifest digest mismatch')
        if sha(m['input_baseline']['path'])!=m['input_baseline']['sha256']: fail('BASELINE_DIGEST','Baseline file drift')
        baseline=read(m['input_baseline']['path'])
        for record in baseline['protected_files']:
            if not (ROOT/record['path']).is_file() or sha(record['path'])!=record['sha256']: fail('PROTECTED_INPUT',record['path'])
        protected={x['path'] for x in baseline['protected_files']}
        for folder in ('source','docs','evidence'):
            for p in (ROOT/folder).rglob('*'):
                if p.is_file():
                    rel=p.relative_to(ROOT).as_posix()
                    if rel not in protected and not rel.startswith(('docs/implementation/','evidence/implementation/')): fail('UNAUTHORIZED_OUTPUT',rel)
        if read('evidence/implementation/source-inventory.json')!=derive(): fail('INVENTORY_DRIFT','Inventory must be independently reproducible from protected inputs')
        topo=read('docs/implementation/task-order.json')
        if topo['topological_order']!=order or topo['plan_digest']!=m['plan_digest']: fail('ORDER_VIEW','Task-order drift')
        graph=(ROOT/'docs/implementation/dependency-graph.mmd').read_text(encoding='utf-8')
        if set(re.findall(r'^\s*(T\d{4})\[',graph,re.M))!=set(ids): fail('GRAPH_NODES','Mermaid task nodes differ')
        if set(re.findall(r'^\s*(T\d{4}) --> (T\d{4})$',graph,re.M))!={(d,t['id']) for t in m['tasks'] for d in t['dependencies']}: fail('GRAPH_EDGES','Mermaid edges differ')
        runway_text=(ROOT/'docs/implementation/22-first-coding-runway.md').read_text(encoding='utf-8')
        if re.findall(r'^\d+\. \[(T\d{4})\]',runway_text,re.M)!=m['first_runway']: fail('RUNWAY_VIEW','Runway document differs')
        summary=(ROOT/'docs/implementation/00-implementation-summary.md').read_text(encoding='utf-8')
        if f"**{len(ids)} tasks in {len(m['milestones'])} outcome milestones" not in summary: fail('SUMMARY_TOTAL','Summary count differs')
        gate_text=(ROOT/'docs/implementation/17-decision-gate-map.md').read_text(encoding='utf-8')
        gate_rows={line.split('|')[1].strip():line.split('|')[2] for line in gate_text.splitlines() if line.startswith('| ') and line.split('|')[1].strip() in gs}
        if set(gate_rows)!=set(gs): fail('GATE_MAP_VIEW','Derived gate rows differ')
        for gid,cell in gate_rows.items():
            if Counter(re.findall(r'(T\d{4})/(START|COMPLETION|SHADOW|ACTION_ENABLEMENT|CUTOVER)',cell))!=Counter((x['task_id'],x['stage']) for x in gs[gid]['applications']): fail('GATE_MAP_APPLICATION',gid)
        roadmap=(ROOT/'docs/implementation/03-milestone-roadmap.md').read_text(encoding='utf-8')
        for milestone in m['milestones']:
            block=re.search(r'^## '+milestone['id']+r' — .*?(?=^## |\Z)',roadmap,re.M|re.S)
            found=re.findall(r'\[(T\d{4})\]\(tasks/',block[0]) if block else []
            if set(found)!=set(milestone['task_ids']) or len(found)!=len(milestone['task_ids']): fail('ROADMAP_VIEW',milestone['id'])
        required=['START-HERE.md','execution-state.md','adr-impact-map.md','agent-prompts/single-task.md','agent-prompts/bounded-batch.md']
        required += [f'{i:02d}-' for i in range(23)]
        existing=[p.name for p in (ROOT/'docs/implementation').glob('*.md')]
        for name in required:
            if name.endswith('-'):
                if sum(x.startswith(name) for x in existing)!=1: fail('CHAPTER',name)
            elif not (ROOT/'docs/implementation'/name).is_file(): fail('HANDOFF',name)
        for p in (ROOT/'docs/implementation').rglob('*.md'):
            text=re.sub(r'```.*?```','',p.read_text(encoding='utf-8'),flags=re.S)
            text=re.sub(r'`[^`]*`','',text)
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
                target=target.split('#',1)[0].strip('<>')
                if not target or re.match(r'^[a-z]+://',target): continue
                if not (p.parent/target).resolve().exists(): fail('LOCAL_LINK',str(p.relative_to(ROOT))+' -> '+target)
    return errors

def main():
    m=read('docs/implementation/task-manifest.yaml'); c=read('docs/implementation/requirements-coverage.yaml'); g=read('docs/implementation/decision-gates.yaml'); inventory=derive()
    errors=validate(m,c,g,inventory)
    controls=[]
    for name,expected in [('dangling_dependency','DANGLING_DEPENDENCY'),('dependency_cycle','CYCLE'),('missing_coverage','COVERAGE_INVENTORY'),('missing_contact_safety','SAFETY_PREDECESSOR'),('unsafe_shared_parallel_lock','SHARED_LOCK'),('invalid_status_schema','SCHEMA'),('missing_assertion_reference','COVERAGE_TEST_REFERENCE')]:
        mm,cc=copy.deepcopy(m),copy.deepcopy(c)
        if name=='dangling_dependency': mm['tasks'][0]['dependencies'].append('T9999')
        if name=='dependency_cycle': mm['tasks'][0]['dependencies'].append('T1306')
        if name=='missing_coverage': cc['mappings']=[r for r in cc['mappings'] if r['requirement_id']!='MR01']
        if name=='missing_contact_safety': next(t for t in mm['tasks'] if t['id']=='T1303')['dependencies']=['T0001']
        if name=='unsafe_shared_parallel_lock':
            for t in mm['tasks']:
                if t['id'] in ('T0702','T0703'): t['shared_change_locks'].append('negative-control:shared')
        if name=='invalid_status_schema': mm['tasks'][0]['status']='DONE'
        if name=='missing_assertion_reference': cc['mappings'][0]['test_refs']=['NONEXISTENT-TEST']
        found={e['code'] for e in validate(mm,cc,g,inventory,files=False)}
        controls.append({'name':name,'expected_rejection':expected,'result':'PASS' if expected in found else 'FAIL'})
    output={'schema_version':'1.0','generated_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'plan_revision':m['plan_revision'],'plan_digest':m['plan_digest'],
        'result':'PASS' if not errors and all(x['result']=='PASS' for x in controls) else 'FAIL',
        'scope':'Static schema, independently derived declared traceability, dependency/gate/contract/parallel/view integrity and protected content digests only. Not application execution or semantic/security/provider certification.',
        'counts':{'tasks':len(m['tasks']),'milestones':len(m['milestones']),'source_requirements':len(inventory['requirements']),'mvp_capabilities':sum(r['kind']=='MVP' for r in inventory['requirements']),'owner_decisions':sum(r['kind']=='OWNER_DECISION' for r in inventory['requirements']),'adrs':sum(r['kind']=='ADR' for r in inventory['requirements']),'architecture_modules':sum(r['kind']=='ARCHITECTURE_MODULE' for r in inventory['requirements']),'source_decisions':len(inventory['decisions']),'gates':len(g['gates']),'golden_scenarios':sum(bool(re.fullmatch(r'GD\d{2}',r['id'])) for r in inventory['requirements']),'kpi_contracts':sum(bool(re.fullmatch(r'KR\d{2}',r['id'])) for r in inventory['requirements']),'protected_files':len(read(m['input_baseline']['path'])['protected_files'])},
        'negative_controls':controls,'errors':errors,'runtime_checks':{'application_unit_database_rls_browser':'NOT_CHECKED','actual_provider_capability_and_effects':'NOT_CHECKED','actual_s3_auth0_resend_telemetry':'NOT_CHECKED','restore_performance_shadow_cutover':'NOT_CHECKED'},
        'review_evidence':['evidence/implementation/independent-review.md','evidence/implementation/quality-review.md']}
    (ROOT/'evidence/implementation/verification.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,ensure_ascii=True,indent=2)); return 0 if output['result']=='PASS' else 1
if __name__=='__main__': sys.exit(main())
