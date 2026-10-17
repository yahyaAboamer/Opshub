"""Render documentation views from the canonical manifest. No application operations."""
from pathlib import Path
import hashlib, json, re

ROOT=Path(__file__).resolve().parents[2]
DOC=ROOT/'docs/implementation'

def read(path): return json.loads((ROOT/path).read_text(encoding='utf-8'))
def write(path,text):
    p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text.rstrip()+'\n',encoding='utf-8')
def digest(data):
    return hashlib.sha256(json.dumps({k:v for k,v in data.items() if k!='plan_digest'},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def tasklink(t): return f"[{t['id']}](tasks/{t['id']}.md)"
NOT_APPROVED='PHASE6_NOT_APPROVED_IMPLEMENTATION_NOT_AUTHORIZED'
APPROVED='PHASE6_APPROVED_LOCAL_TASK_IMPLEMENTATION_AUTHORIZED'

def render():
    m=read('docs/implementation/task-manifest.yaml')
    for milestone in m['milestones']:
        if milestone['id'] in ('M3','M4','M7','M9','M11'):
            milestone['outcome_level']='LOCAL_PLUS_QUALIFIED_CONTROLLED_EVIDENCE'
    for t in m['tasks']:
        if t['id'] in ('T0702','T0703','T0704','T0705'):
            t['parallelism']='PARALLEL WITH RESTRICTIONS'
    approved=m['approval_status']==APPROVED
    if approved or m['approval_status']==NOT_APPROVED:
        gates={g['id']:g for g in read('docs/implementation/decision-gates.yaml')['gates']}
        status={t['id']:t['status'] for t in m['tasks']}
        for t in m['tasks']:
            # After recorded G-P6 approval the local-permission blocker is gone; accepted predecessors stop blocking.
            t['blockers']=[] if approved else [{'kind':'AUTHORIZATION','id':'G-P6','detail':'Phase6/local implementation approval pending'}]
            t['blockers'] += [{'kind':'DEPENDENCY','id':d,'detail':'Predecessor must be ACCEPTED on current main with actual contract/evidence'} for d in t['dependencies'] if not (approved and status[d]=='ACCEPTED')]
            for ref in t['decision_gates']:
                if ref['stage']=='START' and ref['gate_id']!='G-P6' and gates[ref['gate_id']]['status']!='SATISFIED':
                    gate=gates[ref['gate_id']]
                    kind='AUTHORIZATION' if gate['category']=='AUTHORIZATION' else 'DEPENDENCY' if gate.get('required_task_ids') else 'DECISION'
                    t['blockers'].append({'kind':kind,'id':ref['gate_id'],'detail':ref['capability']})
            later=[b['kind'] for b in t['blockers'] if b['id']!='G-P6']
            t['readiness_after_local_approval']='WAITING_DEPENDENCIES' if 'DEPENDENCY' in later else 'WAITING_AUTHORIZATION' if 'AUTHORIZATION' in later else 'WAITING_DECISION' if 'DECISION' in later else 'READY'
            if approved and t['status']=='NOT_STARTED': t['readiness']=t['readiness_after_local_approval']
    m['plan_digest']=digest(m)
    write('docs/implementation/task-manifest.yaml',json.dumps(m,ensure_ascii=False,indent=2))
    by={t['id']:t for t in m['tasks']}
    # Graph is rendered before any detailed task contracts.
    graph=['flowchart TD']
    for t in m['tasks']:
        graph.append(f"  {t['id']}[\"{t['id']}: {t['title'].replace(chr(34),chr(39))}\"]")
        for dep in t['dependencies']: graph.append(f"  {dep} --> {t['id']}")
    write('docs/implementation/dependency-graph.mmd','\n'.join(graph))
    write('docs/implementation/task-order.json',json.dumps({'plan_revision':m['plan_revision'],'plan_digest':m['plan_digest'],'topological_order':m['topological_order']},indent=2))
    write('docs/implementation/02-dependency-graph.md',f'''# Implementation dependency graph

Plan {m['plan_revision']}. The full [task DAG](dependency-graph.mmd) has {len(m['tasks'])} nodes; [topological order](task-order.json) is authoritative data derived from the manifest. Every edge consumes the predecessor's versioned boundary and acceptance evidence, not merely its source files.

```mermaid
flowchart LR
  T0001 --> T0002 --> T0004 --> T0101 --> T0102 --> T0109
  T0001 --> T0003 --> T0007
  T0109 --> T0201 --> T0202 --> T0204 --> T0302
  T0008 --> T0209 --> T0501 --> T0504 --> T0507
  T0302 --> T0303 --> T0401 --> T0404
  T0501 --> T0601 --> T0603 --> T0608 --> T0609
  T0608 --> T0706 --> T0708 --> T0701
  T0404 --> T0901 --> T0913 --> T1106
  T1106 --> T1205 --> T1108 --> T1206 --> T1207
  T1208 --> T1205 --> T1209 --> T1210 --> T1211 --> T1207
  T0701 --> T1301
  T1207 --> T1301 --> T1302 --> T1304 --> T1305 --> T1306
  T1207 --> T1303 --> T1304
```

This compressed diagram shows selected transitive relationships; exact direct edges are in the full DAG/manifest. There is no duration estimate. Structural bottlenecks are tenant isolation, atomic queue qualification, source/run identity, contact/action recovery, complete golden realization, qualified real reads/actions, staged recovery, private rehearsal, shadow and authority transfer.

Milestones organize outcomes and are not whole-milestone prerequisites. T1201–T1204 may establish controlled staging before M3/M4 read qualification; local work can continue while those authorized-environment tasks wait. M11 private rehearsal consumes M12 staged recovery, while M12 shadow consumes that rehearsal. These are acyclic task edges, not permission to pretend every milestone finishes in number order.

After a predecessor merge, each consumer branch updates from accepted main and revalidates the produced contract/version. A future release gate is not an invented task dependency on an owner decision.
''')
    for t in m['tasks']:
        sections=[f"# {t['id']} — {t['title']}",
            f"<!-- identity: {t['id']}; milestone: {t['milestone']}; status: {t['status']} -->",
            '<!-- dependencies: '+','.join(t['dependencies'])+' -->',
            f"<!-- manifest-digest: {m['plan_digest']} -->",
            f"Milestone **{t['milestone']}** · **{t['type']}** · risk **{t['risk']}** · complexity **{t['complexity']}**. Execution **{t['status']}**; readiness **{t['readiness']}**. The [manifest](../task-manifest.yaml) owns status and dependency metadata; this is a generated view.",
            '## Goal\n\n'+t['goal'],'## Why\n\n'+t['why']+'\n\nRequirements: '+', '.join(t['requirement_ids'])+'. Validation contracts: '+(', '.join(t['validation_contract_ids']) or 'None directly; named engineering prerequisites above')+'.',
            '## Dependencies and contracts consumed\n\n'+ ('\n'.join(f"- **{c['task_id']} / {c['contract_id']}**: {c['consumes']}" for c in t['consumed_contracts']) or ('No predecessor task. G-P6 local implementation approval is recorded; this Task ID must still be explicitly selected.' if m['approval_status']==APPROVED else 'No predecessor task. Human plan/local implementation approval remains required.')),
            '## Definition of Ready and smallest reading set\n\n'+t['definition_of_ready'],
            '## Relevant specifications\n\n'+'\n'.join(f"- [{s['path']}:{s['line']}]({Path('../../../'+s['path']).as_posix()}): "+re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',s['section'])+f" (lines {s['line']}–{s['end_line']})." for s in t['spec_refs']),
            '## Contract produced\n\n'+'\n'.join(f"**{c['id']}**, boundary `{c['boundary']}`. {c['meaning']}\n\nFuture record `{c['record']}`: {c['required_content']}" for c in t['produced_contracts']),
            '## Scope\n\n'+t['scope'],'## Explicit non-scope\n\n'+t['explicit_non_scope'],
            '## Expected code and editable areas\n\nThese are planned ownership boundaries, not pre-existing files. Inspect the accepted repository layout before allocating actual files.\n\n'+'\n'.join('- `'+x+'`' for x in t['editable_areas']),
            '## Data changes\n\n'+t['data_changes'],'## Security and tenancy\n\n'+t['security_tenancy'],
            '## Failure and edge cases\n\n'+t['failure_edge_cases'],
            '## Tests required\n\n'+'\n'.join(f"- **{x['id']} — PLANNED** ({x['environment']}): {x['assertion']}" for x in t['test_requirements']),
            '## Acceptance criteria\n\n'+'\n'.join(f"- **{x['id']}**: {x['criterion']}" for x in t['acceptance_criteria']),
            '## Completion evidence\n\nNo implementation evidence exists yet; `completion_evidence_refs` is empty. Provide actual commit/tree, base-main revision, environment/tool versions, fixture/policy digests, exact commands and unabridged safe failure/pass summaries, review disposition and produced-contract record.\n\n**PLANNED commands:** T0009 must establish `npm run check:format`, `check:lint`, `check:types`, `test:unit`, `test:db`, `test:contracts`, `test:e2e`, `build` and relevant `test:recovery`/`test:golden` scripts. These scripts do not exist at the Phase6 baseline. Use only the lanes relevant to this task; record exact task selectors after they exist. Earlier compatibility tasks define and record their own isolated commands. T0001 records Git inventory/ignore/protected-digest checks without scaffolding an application.\n\nSafety evidence includes deterministic fault barrier order and observed request/effect/start counts. Reports state PASS/FAIL/NOT_CHECKED and what each proves.\n\n'+t['ui_journey'],
            '## Change and recovery boundary\n\n'+t['change_recovery_boundary'],
            '## Decision gates\n\n'+'\n'.join(f"- **{g['gate_id']} / {g['stage']}**, {g['environment']}: {g['capability']}" for g in t['decision_gates'])+'\n\nCanonical owner/evidence criteria: [decision-gates.yaml](../decision-gates.yaml). A gate at SHADOW/ACTION_ENABLEMENT/CUTOVER does not block unrelated synthetic construction. START gates block this task; COMPLETION gates permit bounded preparatory work but prevent acceptance in the stated environment. No deadline or elapsed time is approval.',
            '## Accountable role and permitted effects\n\n'+t['accountable_role']+'. Environments: '+', '.join(t['permitted_environment'])+'. Effect class: **'+t['effect_class']+'**. A coding agent cannot supply owner, Merchant Admin, account-owner or operational-release approval.',
            '## Branch isolation and parallelism\n\n**'+t['parallelism']+'**. '+t['branch_isolation']+'\n\nShared-change locks: '+', '.join('`'+x+'`' for x in t['shared_change_locks'])+'. '+t['merge_order']+'\n\n'+t['complexity_rationale'],
            '## Bounded execution steps\n\n- [ ] Claim this Task ID and all edit locks on the current accepted baseline; verify readiness and exact effects permission.\n- [ ] Fix independent fixture/input expectations and demonstrate the named negative case before implementing its behavior.\n- [ ] Implement only this boundary, including its necessary UI/data/test contract; stop on an unresolved source contradiction.\n- [ ] Run the appropriate deterministic checks and review actual scope, failures and recovery evidence.\n- [ ] Submit actual evidence and contract for independent review; integration owner accepts/merges in dependency order and updates the canonical manifest. Operational approvals remain separate.'
        ]
        write(t['task_spec'],'\n\n'.join(sections))
    roadmap=DOC/'03-milestone-roadmap.md'
    if roadmap.exists():
        text=roadmap.read_text(encoding='utf-8')
        for milestone in m['milestones']:
            match=re.search(r'^## '+milestone['id']+r' — .*?(?=^## |\Z)',text,re.M|re.S)
            block=match[0]; ts=[by[x] for x in milestone['task_ids']]; ids=set(milestone['task_ids'])
            external=sorted({d for t in ts for d in t['dependencies'] if d not in ids})
            block=re.sub(r'Included \*\*\d+ tasks\*\*: .*?\.\n',f"Included **{len(ts)} tasks**: "+', '.join(tasklink(t) for t in ts)+'.\n',block)
            block=re.sub(r'Whole-milestone external contracts needed before all tasks can exit: .*?\.\n','Whole-milestone external contracts needed before all tasks can exit: '+(', '.join(external) or 'none')+'.\n',block)
            text=text[:match.start()]+block+text[match.end():]
        write('docs/implementation/03-milestone-roadmap.md',text)
    gates=read('docs/implementation/decision-gates.yaml')['gates']
    table=['| Gate | Exact tasks and blocking stages | Responsible role and evidence |','|---|---|---|']
    for gate in gates:
        table.append('| '+gate['id']+' | '+', '.join(a['task_id']+'/'+a['stage'] for a in gate['applications'])+' | '+gate['responsible_decision_maker'].replace('|','/')+'; see canonical register for exact environment, scope and required evidence verdict |')
    gate_doc=DOC/'17-decision-gate-map.md'
    if gate_doc.exists():
        prefix=gate_doc.read_text(encoding='utf-8').split('| Gate |')[0]
        write('docs/implementation/17-decision-gate-map.md',prefix+'\n'.join(table))
    coverage=read('docs/implementation/requirements-coverage.yaml')['mappings']
    adr=['# ADR impact map','','The owner-approved Phase4 ADR intent is unchanged; historical proposed labels remain protected. Actual tests/qualifications are future work.','','| ADR | Milestone/task implementation homes | Acceptance and tests |','|---|---|---|']
    for row in coverage:
        if row['kind']=='ADR':
            adr.append('| ['+row['requirement_id']+'](../../'+row['source']+') | '+', '.join(by[x]['milestone']+'/'+x for x in row['task_ids'])+' | '+'; '.join(row['test_refs'])+'; corresponding task AC01 and stage gates |')
    write('docs/implementation/adr-impact-map.md','\n'.join(adr))
    for name in ('00-implementation-summary.md','START-HERE.md','execution-state.md'):
        p=DOC/name
        if p.exists():
            text=p.read_text(encoding='utf-8').replace('P6-r1',m['plan_revision'])
            text=re.sub(r'contains \*\*\d+ tasks in \d+ outcome milestones',f"contains **{len(m['tasks'])} tasks in {len(m['milestones'])} outcome milestones",text)
            write('docs/implementation/'+name,text)
    return m

if __name__=='__main__':
    result=render(); print(json.dumps({'task_specs':len(result['tasks']),'plan_digest':result['plan_digest']}))
