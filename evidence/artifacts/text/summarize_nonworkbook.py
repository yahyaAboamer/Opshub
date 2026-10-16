"""Static source analysis and evidence packaging only; no source execution."""
import ast,datetime,hashlib,json,re,zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
SRC=Path(r'D:\Desktop\Opshub\source')
OUT=Path(r'D:\Desktop\Opshub\evidence\artifacts\text')
manifest=json.loads((OUT/'nonworkbook-manifest.json').read_text(encoding='utf-8'))
checks=[]; script_summary=[]; metadata=[]
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
for item in manifest:
    p=SRC/item['file']; digest=hashlib.sha256(p.read_bytes()).hexdigest()
    checks.append({'file':item['file'],'sha256_matches_initial_read':digest==item['sha256']})
    if p.suffix=='.py':
        tree=ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p))
        script_summary.append({'file':item['file'],'parse_ok':True,'functions':[{'name':n.name,'start_line':n.lineno,'end_line':n.end_lineno} for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))],'imports':[{'line':n.lineno,'modules':[a.name for a in n.names]} for n in ast.walk(tree) if isinstance(n,ast.Import)]+[{'line':n.lineno,'from':n.module,'modules':[a.name for a in n.names]} for n in ast.walk(tree) if isinstance(n,ast.ImportFrom)]})
    if p.suffix=='.docx':
        with zipfile.ZipFile(p) as z:
            extra=[]
            for name in z.namelist():
                if name.startswith('word/') and name.endswith('.xml') and any(s in name for s in ('header','footer','footnote','endnote','comments')):
                    root=ET.fromstring(z.read(name)); runs=[e.text for e in root.iter(W+'t') if e.text]
                    extra.append({'part':name,'text_run_count':len(runs)})
            root=ET.fromstring(z.read('word/document.xml'))
            metadata.append({'file':item['file'],'supplementary_parts':extra,'nested_tables':sum(1 for t in root.iter(W+'tbl') if t.find('.//'+W+'tbl') is not None),'textboxes':len(root.findall('.//'+W+'txbxContent')),'total_body_text_runs':len(list(root.iter(W+'t')))})
    if 'pyc' in item:
        pyc=item['pyc']; pyc['timestamp_utc']=datetime.datetime.fromtimestamp(pyc['timestamp'],datetime.timezone.utc).isoformat() if pyc['timestamp'] else None
        metadata.append({'file':item['file'],'pyc':pyc})
report=(OUT/'nonworkbook-analysis.md').read_text(encoding='utf-8')
def parse_table_after(marker):
    text=report.split(marker,1)[1]; lines=text.splitlines(); rows=[]; started=False
    for line in lines:
        if line.startswith('|'):
            cells=[s.strip() for s in line.split('|')[1:-1]]
            if all(re.fullmatch(r'[-:]+',s.replace(' ','')) for s in cells):continue
            rows.append(cells);started=True
        elif started:break
    if not rows:return []
    return [dict(zip(rows[0],r)) for r in rows[1:]]
payload={'scope':'Static artifact findings only. No original scripts executed and no live behavior independently observed by this worker.','investigated_on':'2026-10-13','authority':parse_table_after('## Artifact authority and provenance'),'domain':parse_table_after('The historical system is a single apparel merchant operation'),'metrics':parse_table_after('## Calculations and metric definitions'),'discrepancies':parse_table_after('## Contradictions, limitations and reconciliation candidates'),'source_integrity':{'files_checked':len(checks),'all_match':all(c['sha256_matches_initial_read'] for c in checks),'checks':checks}}
(OUT/'nonworkbook-findings.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'static-script-map.json').write_text(json.dumps(script_summary,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'supplementary-metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'source_files_integrity_checked':len(checks),'source_hashes_unchanged':payload['source_integrity']['all_match'],'authority_rows':len(payload['authority']),'domain_rows':len(payload['domain']),'metric_rows':len(payload['metrics']),'discrepancy_rows':len(payload['discrepancies']),'python_files_parsed_without_execution':len(script_summary),'supplementary_metadata':metadata},ensure_ascii=False,indent=2))
