"""Derive Phase 6 traceability inventory from protected inputs, never from tasks."""
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'evidence/implementation/source-inventory.json'

def derive():
    requirements, exclusions, decisions = {}, {}, {}
    def add(target, identifier, path, line, text, kind):
        p = ROOT / path
        candidate={'id': identifier, 'kind': kind, 'source': path, 'line': line,
            'locator': text.strip(), 'source_sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
        def score(value):
            s=value['locator']; ident=re.escape(identifier)
            if re.match(r'(?:\|\s*|\*\*|#{2,3}\s+)'+ident+r'(?:\b|:)',s): return 3
            if s.startswith(identifier): return 2
            return 1
        if identifier not in target or score(candidate)>score(target[identifier]): target[identifier]=candidate
    for p in sorted((ROOT/'docs/product').glob('*.md')):
        path = p.relative_to(ROOT).as_posix()
        for n, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            if p.name.startswith('03-') and line.startswith('|'):
                m = re.match(r'\|\s*((?:MR|F)\d{2})\s*\|', line)
                if m:
                    target = requirements if 'MUST HAVE' in line else exclusions
                    add(target, m[1], path, n, line, 'MVP' if target is requirements else 'DEFERRED_OR_EXCLUDED')
            if p.name.startswith('00-'):
                m = re.match(r'## (OD\d{2})', line)
                if m: add(requirements, m[1], path, n, line, 'OWNER_DECISION')
            if p.name.startswith('13-'):
                m = re.match(r'\|\s*(OP\d{2})\b', line)
                if m: add(decisions, m[1], path, n, line, 'PRODUCT_GATE')
            # Definitions, not incidental cross-references.
            m = re.match(r'(?:#{2,3}\s+|\|\s*|\*\*)?((?:AC|WF|PF|PER|KPI|K|P|IG|CON|ING|ACT|FB|EXP|COM|AUD|TR|CFG)\d{2})\b', line)
            if m: add(requirements, m[1], path, n, line, 'PRODUCT_CONTRACT')
    p=ROOT/'docs/architecture/02-architecture-style-and-modules.md'
    in_modules=False
    for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
        if line.startswith('## '): in_modules=line=='## Module contracts'
        if in_modules and line.startswith('|'):
            name=line.split('|')[1].strip()
            if name not in ('Module','---') and name and not name.startswith('-'):
                key='MOD-'+re.sub(r'[^A-Z0-9]+','-',name.upper()).strip('-')
                add(requirements,key,p.relative_to(ROOT).as_posix(),n,line,'ARCHITECTURE_MODULE')
    for p in sorted((ROOT/'docs/architecture/adr').glob('*.md')):
        add(requirements,p.name[:7],p.relative_to(ROOT).as_posix(),1,p.read_text(encoding='utf-8').splitlines()[0],'ADR')
    for path,pattern,kind in [
        ('docs/architecture/17-open-architecture-decisions.md',r'\|\s*(A\d{2})\b','ARCHITECTURE_GATE'),
        ('docs/migration/16-open-migration-decisions.md',r'\|\s*(MD\d{2})\b','MIGRATION_GATE')]:
        for n,line in enumerate((ROOT/path).read_text(encoding='utf-8').splitlines(),1):
            m=re.match(pattern,line)
            if m: add(decisions,m[1],path,n,line,kind)
    families={
        '01':r'MI\d{2}', '02':r'IM(?:-T)?\d{2}', '03':r'MP(?:-(?:ACQ|SEED|PRIV|T))?\d{2}|MRUN01',
        '04':r'CL(?:-T)?\d{2}', '05':r'OR(?:-INDEP)?\d{2}', '06':r'GD\d{2}',
        '07':r'KR\d{2}', '08':r'PC-[CSBM]\d{2}', '09':r'EA\d{2}',
        '10':r'(?:TI|AU)\d{2}', '11':r'RV(?:\d{2}|-G[123])',
        '12':r'SH[0-4]', '13':r'CT(?:01(?:-[A-I])?|-T\d{2})',
        '14':r'(?:RE|HC|OT|QI)\d{2}', '15':r'PV\d{2}'}
    for p in sorted((ROOT/'docs/migration').glob('*.md')):
        pattern=families.get(p.name[:2])
        if not pattern: continue
        for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
            for m in re.finditer(r'(?<![A-Z0-9-])(?:'+pattern+r')(?![A-Z0-9])',line):
                add(requirements,m[0],p.relative_to(ROOT).as_posix(),n,line,'VALIDATION')
    critical=[
        ('ARC-RLS','docs/architecture/03-multi-tenancy-and-identity.md','## Ownership and context propagation'),
        ('ARC-SESSION','docs/architecture/03-multi-tenancy-and-identity.md','## Authentication, sessions and invitations'),
        ('ARC-CONTACT','docs/architecture/07-background-jobs-and-reconciliation.md','## Operational attention: persisted versus derived'),
        ('ARC-ENQUEUE','docs/architecture/07-background-jobs-and-reconciliation.md','## Delivery and transactional semantics'),
        ('ARC-RECOVERY','docs/architecture/13-deployment-and-environments.md','## Protecting external effects across backup rollback'),
        ('ARC-RESTORED-ACCESS','docs/architecture/13-deployment-and-environments.md','## Restored authority and privacy access gate'),
        ('ARC-RETENTION','docs/architecture/11-audit-provenance-and-privacy.md','## Practical retention boundaries'),
        ('ARC-CREDENTIALS','docs/architecture/05-integrations.md','## Connection, ownership and credential boundaries'),
        ('ARC-EXPORT','docs/architecture/08-api-and-application-boundaries.md','## Exports'),
        ('ARC-TECH','docs/architecture/15-technology-selection.md','## Remaining stack gates'),
        ('PLAN-ZERO-PILOT','evidence/implementation-prompt-review/phase6-implementation-plan-prompt.md','Build the pilots as production tenants on a $0 pilot offering.'),
    ]
    for ident,path,needle in critical:
        lines=(ROOT/path).read_text(encoding='utf-8').splitlines()
        idx=next(i for i,x in enumerate(lines) if x.startswith(needle))
        add(requirements,ident,path,idx+1,lines[idx],'LOCAL_TRACEABILITY')
    # Explicitly declared ranges supplement individual definitions; no task count participates.
    for prefix,count,path in [
        ('GD',43,'docs/migration/06-golden-datasets.md'),('KR',21,'docs/migration/07-kpi-regression-suite.md'),
        ('EA',26,'docs/migration/09-external-action-safety-validation.md'),
        ('TI',21,'docs/migration/10-tenant-and-authorization-validation.md'),('AU',13,'docs/migration/10-tenant-and-authorization-validation.md'),
        ('RV',21,'docs/migration/11-recovery-validation.md'),('PV',13,'docs/migration/15-privacy-and-test-data.md')]:
        for i in range(1,count+1):
            if f'{prefix}{i:02d}' not in requirements:
                raise ValueError(f'Missing source definition: {prefix}{i:02d} in {path}')
    return {'schema_version':'1.0','method':'Protected source definitions, module table and local critical-section identifiers; independent of task manifest',
        'requirements':list(requirements.values()),'decisions':list(decisions.values()),'deferred_excluded':list(exclusions.values())}

if __name__=='__main__':
    result=derive(); OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:len(result[k]) for k in ('requirements','decisions','deferred_excluded')}))
