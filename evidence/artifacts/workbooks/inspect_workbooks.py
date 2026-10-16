from pathlib import Path
import zipfile, xml.etree.ElementTree as ET, json, re, hashlib, csv, collections
from datetime import datetime, date
from openpyxl.formula.translate import Translator

ROOT=Path(r'D:\Desktop\Opshub')
SOURCE=ROOT/'source'
OUT=ROOT/'evidence/artifacts/workbooks'
OUT.mkdir(parents=True,exist_ok=True)
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
RNS='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
PKG='{http://schemas.openxmlformats.org/package/2006/relationships}'

def colnum(ref):
    letters=re.match(r'\$?([A-Z]+)',ref).group(1)
    val=0
    for c in letters:val=val*26+ord(c)-64
    return val

def collabel(i):
    s=''
    while i:i,r=divmod(i-1,26);s=chr(65+r)+s
    return s

def stringval(cell,ss):
    typ=cell.get('t')
    v=cell.find('m:v',NS)
    if typ=='inlineStr':return ''.join(t.text or '' for t in cell.findall('.//m:t',NS))
    if v is None:return None
    if typ=='s':return ss[int(v.text)]
    if typ in ('str','e'):return v.text
    if typ=='b':return bool(int(v.text))
    try:
        n=float(v.text)
        return int(n) if n.is_integer() else n
    except:return v.text

def load_book(path):
    z=zipfile.ZipFile(path)
    ss=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        ss=[''.join(t.text or '' for t in si.findall('.//m:t',NS)) for si in ET.fromstring(z.read('xl/sharedStrings.xml'))]
    rels={x.get('Id'):x.get('Target') for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    sheets=[]
    for sh in wb.findall('m:sheets/m:sheet',NS):
        target=rels[sh.get(RNS+'id')]
        xmlpath=target.lstrip('/') if target.startswith('/') else 'xl/'+target
        root=ET.fromstring(z.read(xmlpath))
        cells={}
        shared={}
        for c in root.findall('m:sheetData/m:row/m:c',NS):
            ref=c.get('r');f=c.find('m:f',NS)
            cells[ref]={'v':stringval(c,ss),'f':f.text if f is not None else None,'ft':f.attrib if f is not None else None,'t':c.get('t'),'style':c.get('s')}
            if f is not None and f.get('t')=='shared' and f.text:
                shared[f.get('si')]=(ref,f.text)
        for ref,c in cells.items():
            if c['ft'] is not None and c['ft'].get('t')=='shared' and c['f'] is None:
                anchor,formula=shared[c['ft']['si']]
                c['f']=Translator('='+formula,origin=anchor).translate_formula(ref)[1:]
        sheets.append({'name':sh.get('name'),'state':sh.get('state','visible'),'xmlpath':xmlpath,'xml':root,'cells':cells})
    return {'path':path,'zip':z,'xml':wb,'sheets':sheets}

def normal_formula(f,ref):
    if not f:return None
    try:return Translator('='+f,origin=ref).translate_formula('A1')
    except:return re.sub(r'(\$?[A-Z]{1,3}\$?)\d+',r'\1#',f)

def safe_cache(value):
    # Formula caches can contain a retrieved customer name, phone or address.
    return '[text cache withheld]' if isinstance(value,str) and not value.startswith('#') else value

def overview(book):
    wb=book['xml'];z=book['zip']
    out={'source':book['path'].name,'sha256':hashlib.sha256(book['path'].read_bytes()).hexdigest(),'size_bytes':book['path'].stat().st_size,'sheets':[]}
    out['calculation_properties']=(wb.find('m:calcPr',NS).attrib if wb.find('m:calcPr',NS) is not None else {})
    out['defined_names']=[{'name':n.get('name'),'scope':n.get('localSheetId'),'expression':n.text} for n in wb.findall('m:definedNames/m:definedName',NS)]
    out['external_link_files']=[p for p in z.namelist() if p.startswith('xl/externalLinks/')]
    for sheet in book['sheets']:
        root=sheet['xml'];cells=sheet['cells']
        formulas={ref:c for ref,c in cells.items() if c['f'] is not None}
        patterns=collections.defaultdict(list)
        funcs=collections.Counter();deps=collections.Counter()
        for ref,c in formulas.items():
            patterns[normal_formula(c['f'],ref)].append(ref)
            funcs.update(re.findall(r'(?<![A-Z0-9_.])([A-Z_][A-Z0-9_.]*)\s*\(',c['f'].upper()))
            deps.update(re.findall(r"(?:'([^']+)'|([A-Za-z_][A-Za-z0-9_ .-]*))!",c['f']))
        headers=[{'cell':ref,'label':c['v']} for ref,c in cells.items() if re.search(r'\d+$',ref).group(0)=='1' and c['v'] is not None and c['f'] is None]
        dims=root.find('m:dimension',NS)
        dvs=[]
        for dv in root.findall('m:dataValidations/m:dataValidation',NS):
            dvs.append({**dv.attrib,'formula1':dv.findtext('m:formula1',namespaces=NS),'formula2':dv.findtext('m:formula2',namespaces=NS)})
        cfs=[]
        for cf in root.findall('m:conditionalFormatting',NS):
            cfs.append({'range':cf.get('sqref'),'rules':[{'type':r.get('type'),'operator':r.get('operator'),'formulas':[f.text for f in r.findall('m:formula',NS)]} for r in cf.findall('m:cfRule',NS)]})
        errors=[{'cell':ref,'value':c['v'],'formula':c['f']} for ref,c in cells.items() if c['t']=='e']
        populated={ref:c for ref,c in cells.items() if c['v'] is not None or c['f'] is not None}
        sr={'name':sheet['name'],'visibility':sheet['state'],'dimension':dims.get('ref') if dims is not None else None,'populated_cells':len(populated),'stored_cells':len(cells),'max_populated_row':max([int(re.search(r'\d+$',x).group()) for x in populated] or [0]),'headers_row1':headers,'formula_count':len(formulas),'formula_patterns':[{'pattern':p,'count':len(refs),'first_cell':refs[0],'last_cell':refs[-1],'example':'='+formulas[refs[0]]['f'],'cached_example':safe_cache(formulas[refs[0]]['v'])} for p,refs in sorted(patterns.items(),key=lambda x:-len(x[1]))],'formula_functions':dict(funcs),'formula_sheet_dependencies':{(a or b).strip():n for (a,b),n in deps.items()},'formula_cache_missing_count':sum(c['v'] is None for c in formulas.values()),'errors':errors,'data_validations':dvs,'conditional_formats':cfs,'auto_filter':root.find('m:autoFilter',NS).attrib if root.find('m:autoFilter',NS) is not None else None,'merged_ranges':[m.get('ref') for m in root.findall('m:mergeCells/m:mergeCell',NS)],'hidden_rows':[r.get('r') for r in root.findall('m:sheetData/m:row',NS) if r.get('hidden')=='1'],'hidden_columns':[c.attrib for c in root.findall('m:cols/m:col',NS) if c.get('hidden')=='1'],'charts':[p for p in z.namelist() if p.startswith('xl/charts/') and p.endswith('.xml')],'freeze_panes':[p.attrib for p in root.findall('m:sheetViews/m:sheetView/m:pane',NS)]}
        # These fields are intrinsically structural. No raw customer records are retained.
        out['sheets'].append(sr)
    return out

if __name__=='__main__':
    allbooks=[]
    for path in sorted(SOURCE.glob('*.xlsx')):
        if path.name.startswith('~$'):continue
        print('Scanning',path.name,flush=True)
        book=load_book(path);info=overview(book)
        (OUT/(path.stem+'.structure.json')).write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf-8')
        allbooks.append(info)
        for sh in info['sheets']:
            print(sh['name'],sh['dimension'],'populated',sh['populated_cells'],'formulas',sh['formula_count'],'errors',len(sh['errors']),'headers',[(h['cell'],h['label']) for h in sh['headers_row1']],flush=True)
        book['zip'].close()
    (OUT/'workbook_inventory.json').write_text(json.dumps([{'source':b['source'],'sha256':b['sha256'],'size_bytes':b['size_bytes'],'sheet_count':len(b['sheets']),'formula_count':sum(s['formula_count'] for s in b['sheets']),'sheets':[{'name':s['name'],'dimension':s['dimension'],'populated_cells':s['populated_cells'],'formula_count':s['formula_count'],'errors':len(s['errors'])} for s in b['sheets']]} for b in allbooks],ensure_ascii=False,indent=2),encoding='utf-8')
