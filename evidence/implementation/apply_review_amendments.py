"""Apply the recorded independent-review repair packet to planning metadata only."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[2]
def read(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def save(p,d): (ROOT/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read('docs/implementation/task-manifest.yaml'); c=read('docs/implementation/requirements-coverage.yaml'); g=read('docs/implementation/decision-gates.yaml'); inv=read('evidence/implementation/source-inventory.json')
old_digest=m['plan_digest']; by={t['id']:t for t in m['tasks']}; req={r['id']:r for r in inv['requirements']}; maps={r['requirement_id']:r for r in c['mappings']}
for packet in ('review-amendment-tasks.json','review-runtime-additions.json'):
    d=read('evidence/implementation/'+packet)
    for t in d['tasks']: by.setdefault(t['id'],t)
    for tid,ids in d['extra_requirement_owners'].items():
        for rid in ids:
            if tid=='T0111' and rid=='COM02': continue
            row=maps[rid]
            if tid not in row['task_ids']:
                row['task_ids'].append(tid); row['acceptance_refs'].append(tid+'-AC01'); row['test_refs'].append(by[tid]['test_requirements'][0]['id'])
            key='validation_contract_ids' if req[rid]['kind']=='VALIDATION' else 'requirement_ids'
            if rid not in by[tid][key]: by[tid][key].append(rid)
extra_deps={'T0008':['T0003'],'T0308':['T0309'],'T0405':['T0406'],'T0914':['T0915'],
    'T0706':['T0309','T0406'],'T0707':['T0711'],'T0708':['T0712'],'T0709':['T0713'],'T0710':['T0714'],
    'T1202':['T0210'],'T1203':['T0111'],'T1204':['T0309','T0406','T0915','T0010'],
    'T1205':['T1208'],'T1207':['T1210']}
for tid,ids in extra_deps.items(): by[tid]['dependencies']=sorted(set(by[tid]['dependencies']+ids))
t=by['T0001']
t['scope']='Create Git only after local implementation approval; preserve all 298 protected files on disk and their private custody/digests, while separately approving a trackable clone allowlist for safe docs/synthetic fixtures. Define workspace/ignore boundaries with source/customer/private evidence and secrets excluded. Record Node24 baseline without choosing unverified patches.'
t['test_requirements'][0]['assertion']='On-disk protected input hashes unchanged; a fresh clone contains only the explicitly approved safe trackable inventory, while private originals remain in restricted custody with digest/path references and are not required to enter Git.'
t['acceptance_summary']=t['scope']; t['acceptance_criteria'][0]['criterion']=t['scope']+' Review the two inventories separately; no protected original is moved, deleted or publicly committed.'
t['produced_contracts'][0]['meaning']=t['scope']
t['branch_isolation']='Bootstrap exception: if Git is still absent, owner-authorized T0001 initializes the existing protected workspace without copying/deleting originals, establishes accepted main and its own reviewed boundary. If Git now exists, inspect/reuse accepted main and claim an isolated task branch/worktree. No duplicate task owner.'
by['T0010']['risk']='MEDIUM'
for tid in ('T0707','T0708','T0709','T0710'):
    by[tid]['permitted_environment']=['AUTHORIZED_CONTROLLED_NONPRODUCTION','EXPLICIT_SYNTHETIC_PILOT_ACCOUNT_ENVELOPE']
    by[tid]['explicit_non_scope']+=' Controlled sandbox evidence does not qualify another pilot account. Actual pilot account/native-automation bindings must match qualification evidence; a tightly bounded synthetic pilot effect needs its own explicit envelope.'

def new_gate(ident,role,evidence):
    if not any(x['id']==ident for x in g['gates']): g['gates'].append({'id':ident,'category':'AUTHORIZATION','status':'PENDING','responsible_decision_maker':role,'acceptance_evidence':evidence,'resolution_mode':'EXPLICIT_AUTHORIZATION','applications':[]})
new_gate('AUTH-PRODUCTION-INFRA','Owner and authorized production infrastructure/recovery operator','Separate exact production purchased services/region/keys/grants/storage/backup approval; no production sync/effects/cutover implied.')
new_gate('AUTH-PRODUCTION-DEPLOY','Owner, current verified Merchant Admin and authorized production release operator','Exact staged candidate/image/schema/target/current source ownership and access-off deployment permission. No real read synchronization/provider/customer effect or mail implied.')
new_gate('AUTH-TELEMETRY','Owner/security/privacy reviewer and environment operator','Exact environment/destination and pre-serialization allowlist/scrubbing/retention/residency/sample approval before real Sentry/OTEL transmission; local mock sink needs no external-send approval.')
bg={x['id']:x for x in g['gates']}
def attach(gid,tid,stage,capability):
    t=by[tid]
    if not any(x['gate_id']==gid and x['stage']==stage and x['capability']==capability for x in t['decision_gates']):
        t['decision_gates'].append({'gate_id':gid,'stage':stage,'capability':capability,'environment':t['permitted_environment'][0]})
for gid,tid,stage,cap in [
 ('A08-DATABASE','T0008','START','Real disposable DB rollback/migration compatibility before recovery-envelope harness reliance'),
 ('AUTH-STAGING-DEPLOY','T1208','START','Exact complete reviewed staging candidate and expansion schema'),
 ('AUTH-PRODUCTION-INFRA','T1209','START','Dedicated purchased production resources, egress off'),
 ('AUTH-PRODUCTION-DEPLOY','T1210','START','Exact disabled production shadow candidate deployment'),
 ('AUTH-TELEMETRY','T1204','START','Staging redacted telemetry destination'),('AUTH-TELEMETRY','T1208','START','Complete staging candidate telemetry'),('AUTH-TELEMETRY','T1210','START','Production redacted telemetry destination'),
 ('A08-SDK','T0711','START','Qualified pinned mutation client/no retry'),('A08-SDK','T0712','START','Qualified pinned mutation client/no retry'),('A08-SDK','T0713','START','Qualified pinned mutation client/no retry'),('A08-SDK','T0714','START','Qualified pinned mutation client/no retry'),
 ('A08-RECOVERY-PROTOCOL','T0210','START','Accepted descriptor and private file protocols before concrete S3 driver'),
 ('A05','T1209','START','Production region/residency/key/retention procurement scope'),('A06','T1209','START','Production purchased-service/backup/operations envelope'),
 ('OP02','T1210','START','Verified production initial Admin and source-owner establishment'),('A04','T1210','START','Current production initial-Admin/session/recovery verification'),('MD09','T1210','START','Production current authority established independently before access'),
 ('Q-SHOPIFY-READ','T1210','COMPLETION','Actual production pilot connection account/version equals qualified scope'),('Q-BOSTA-READ','T1210','COMPLETION','Actual production Bosta binding equals qualified scope'),('Q-META-READ','T1210','COMPLETION','Applicable production Meta binding/qualification or exact approved unavailable state')]: attach(gid,tid,stage,cap)
roles={
 'OP01':'Owner and current Merchant Admin/account owner with provider-qualified engineer','OP02':'Owner, verified merchant representative and security/identity reviewer',
 'OP03':'Owner and current Merchant Admin','OP04':'Owner and merchant contact-operations lead','OP05':'Owner and current Merchant Admin with physical-evidence reviewer','OP06':'Owner and current Merchant Admin with provider-qualified engineer',
 'OP07':'Owner and analytics lead','OP08':'Owner and merchant operations lead','OP09':'Owner and analytics lead','OP10':'Owner and current Merchant Admin/source reviewer','OP11':'Owner/commercial authority and billing Merchant Admin','OP12':'Owner/legal and security/privacy reviewer','OP13':'Owner/operations and provider/analytics leads','OP14':'Owner for any future scope expansion',
 'A01':'Merchant owner/current Admin and provider-qualified engineer','A02':'Provider-qualified engineer and current Merchant Admin','A03':'Owner and current Merchant Admin','A04':'Owner and security reviewer','A05':'Owner/legal and privacy reviewer','A06':'Owner and operations/recovery lead','A07':'Owner and analytics lead','A08':'Engineering compatibility reviewer; owner approves material architecture deviation'}
for gid,role in roles.items():
    bg[gid].setdefault('source_gate_label',bg[gid]['responsible_decision_maker']); bg[gid]['responsible_decision_maker']=role
for gate in g['gates']: gate['applications']=[]
for t in by.values():
    t['requirement_ids']=sorted(set(t['requirement_ids'])); t['validation_contract_ids']=sorted(set(t['validation_contract_ids']))
    t['consumed_contracts']=[{'task_id':d,'contract_id':'C-'+d+'-v1','consumes':by[d]['scope']} for d in t['dependencies']]
    t['execution_claim']={'owner':None,'branch':None,'worktree':None,'base_main_revision':None,'locks':[]}
    for p in (f"docs/implementation/claims/{t['id']}.md",f"docs/implementation/completion/{t['id']}.md"):
        if p not in t['editable_areas']: t['editable_areas'].append(p)
    t['blockers']=[{'kind':'AUTHORIZATION','id':'G-P6','detail':'Phase6/local execution not approved'}]+[{'kind':'DEPENDENCY','id':d,'detail':'Predecessor must be ACCEPTED on current main'} for d in t['dependencies']]
    for ref in t['decision_gates']:
        bg[ref['gate_id']]['applications'].append({'task_id':t['id'],**ref})
        if ref['stage']=='START' and ref['gate_id']!='G-P6': t['blockers'].append({'kind':'AUTHORIZATION' if bg[ref['gate_id']]['category']=='AUTHORIZATION' else 'DECISION','id':ref['gate_id'],'detail':ref['capability']})
    for rid in t['requirement_ids']+t['validation_contract_ids']:
        r=req[rid]
        if not any(s['path']==r['source'] and s['line']<=r['line']<=s['end_line'] for s in t['spec_refs']):
            t['spec_refs'].append({'path':r['source'],'section':r['locator'],'line':r['line'],'end_line':r['line'],'sha256':r['source_sha256']})
    for criterion in t['acceptance_criteria']:
        if 'boundary' in criterion['criterion'] and criterion['id'].endswith('AC02'): pass
m['tasks']=sorted(by.values(),key=lambda t:t['id']); m['plan_revision']='P6-r2'
for milestone in m['milestones']: milestone['task_ids']=[t['id'] for t in m['tasks'] if t['milestone']==milestone['id']]
order=[]; remaining=set(by)
while remaining:
    ready=sorted(t for t in remaining if all(d in order for d in by[t]['dependencies']))
    if not ready: raise ValueError('Cycle: '+str(remaining))
    order.append(ready[0]); remaining.remove(ready[0])
m['topological_order']=order
save('docs/implementation/task-manifest.yaml',m); save('docs/implementation/requirements-coverage.yaml',c); save('docs/implementation/decision-gates.yaml',g)
schema=read('docs/implementation/task-manifest.schema.json')
schema['$defs']['task']['properties']['execution_claim']={'type':'object','additionalProperties':False,'required':['owner','branch','worktree','base_main_revision','locks'],'properties':{**{k:{'type':['string','null']} for k in ['owner','branch','worktree','base_main_revision']},'locks':{'$ref':'#/$defs/strings'}}}
if 'execution_claim' not in schema['$defs']['task']['required']: schema['$defs']['task']['required'].append('execution_claim')
save('docs/implementation/task-manifest.schema.json',schema)
save('evidence/implementation/review-repair-record.json',{'review':'evidence/implementation/independent-review.md','reviewed_draft_plan_digest':old_digest,'amended_revision':'P6-r2','new_task_ids':[t for t in sorted(by) if t in {n['id'] for packet in ('review-amendment-tasks.json','review-runtime-additions.json') for n in read('evidence/implementation/'+packet)['tasks']}],'disposition':'IR01-IR07 incorporated; verification and bounded reviewer recheck pending'})
print(json.dumps({'tasks':len(by),'gates':len(g['gates']),'topological_order':len(order),'revision':m['plan_revision']}))
