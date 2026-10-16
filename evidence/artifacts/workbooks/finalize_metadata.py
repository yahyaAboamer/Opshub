from inspect_workbooks import *
import posixpath

def rel_targets(z,part):
    rp=posixpath.dirname(part)+'/_rels/'+posixpath.basename(part)+'.rels'
    if rp not in z.namelist():return {}
    return {r.get('Id'):(r.get('Target').lstrip('/') if r.get('Target').startswith('/') else posixpath.normpath(posixpath.join(posixpath.dirname(part),r.get('Target')))) for r in ET.fromstring(z.read(rp)) if r.get('TargetMode')!='External'}

checks=[]
for fp in OUT.glob('*.structure.json'):
    info=json.loads(fp.read_text(encoding='utf-8'));path=SOURCE/info['source'];z=zipfile.ZipFile(path);parts=z.namelist();wb=ET.fromstring(z.read('xl/workbook.xml'));rels=rel_targets(z,'xl/workbook.xml');shpaths={s.get('name'):rels[s.get(RNS+'id')] for s in wb.findall('m:sheets/m:sheet',NS)}
    info['chart_parts']=[p for p in parts if re.fullmatch(r'xl/charts/chart\d+\.xml',p)]
    info['table_parts']=[p for p in parts if re.fullmatch(r'xl/tables/table\d+\.xml',p)]
    info['pivot_parts']=[p for p in parts if 'pivotTable' in p or 'pivotCache' in p]
    info['connection_parts']=[p for p in parts if p.endswith('connections.xml') or 'queryTables/' in p]
    info['vba_present']=any(p.lower().endswith('vbaproject.bin') for p in parts)
    info['workbook_protection_present']=wb.find('m:workbookProtection',NS) is not None
    for s in info['sheets']:
        part=shpaths[s['name']];root=ET.fromstring(z.read(part));s['charts']=[];s['sheet_protection_present']=root.find('m:sheetProtection',NS) is not None
        sheetrels=rel_targets(z,part)
        for drawing in root.findall('m:drawing',NS):
            drawpart=sheetrels.get(drawing.get(RNS+'id'))
            if drawpart and drawpart in parts:
                droot=ET.fromstring(z.read(drawpart));dre=rel_targets(z,drawpart)
                for chart in droot.iter('{http://schemas.openxmlformats.org/drawingml/2006/chart}chart'):
                    target=dre.get(chart.get(RNS+'id'))
                    if target:s['charts'].append(target)
    currenthash=hashlib.sha256(path.read_bytes()).hexdigest();checks.append({'source':path.name,'sha256_unchanged_since_initial_read':currenthash==info['sha256'],'zip_integrity_error':z.testzip(),'chart_parts':len(info['chart_parts']),'table_parts':len(info['table_parts']),'sheets_with_charts':[s['name'] for s in info['sheets'] if s['charts']]});z.close()
    fp.write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf-8')

# This lookup evaluates privacy of retained evidence without outputting source PII.
sourcepii=set()
from reconcile_workbooks import selected_book,clean
for filename in ['02_Gentry_Delivery_Performance_System.xlsx','02_Gentry_Delivery_Performance_System_v2.0_BACKUP_2026-08-28.xlsx','02_Gentry_Delivery_Performance_System_v3.0_BACKUP_2026-09-08.xlsx']:
    ss=selected_book(SOURCE/filename,['RAW_Bosta','RAW_Costs','RAW_Intake','RAW_Shopify'])
    for name,columns in [('RAW_Bosta',[16,17,18]),('RAW_Costs',[9,10]),('RAW_Intake',[2,3]),('RAW_Shopify',[2,25,26,27,28,34,35,36,37,38,44,71])]:
        if name not in ss:continue
        for r,row in ss[name]['rows'].items():
            if r<3:continue
            for c in columns:
                v=clean(row.get(c))
                if len(v)>=8:sourcepii.add(v)
privacy=[]
for path in list(OUT.glob('*.json'))+list(OUT.glob('*.md')):
    txt=path.read_text(encoding='utf-8');found=[v for v in sourcepii if v in txt]
    if found and path.name.endswith('.controls.json'):
        data=json.loads(txt)
        for rows in data.values():
            for row in rows:
                for cell in row['cells']:
                    if isinstance(cell.get('value'),str):
                        for value in found:cell['value']=cell['value'].replace(value,'[customer identity redacted]')
        txt=json.dumps(data,ensure_ascii=False,indent=2);path.write_text(txt,encoding='utf-8');found=[v for v in sourcepii if v in txt]
    # Only counts and filenames retained; matching values are never emitted.
    if found:privacy.append({'file':path.name,'source_pii_substring_matches':len(found)})
result={'source_files_read_only_verification':checks,'source_input_pii_token_scan':{'tokens_checked':len(sourcepii),'matched_evidence_files':privacy,'limit':'Exact source values of length at least eight. Generic identical human names can cause false positives; this is not a privacy guarantee for arbitrary natural-language identifiers.'}}
(OUT/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
