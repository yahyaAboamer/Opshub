from inspect_workbooks import *
from datetime import timedelta
from decimal import Decimal,InvalidOperation

def selected_book(path,names=None):
    z=zipfile.ZipFile(path);ss=[]
    if 'xl/sharedStrings.xml' in z.namelist():ss=[''.join(t.text or '' for t in si.findall('.//m:t',NS)) for si in ET.fromstring(z.read('xl/sharedStrings.xml'))]
    rels={x.get('Id'):x.get('Target') for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    wb=ET.fromstring(z.read('xl/workbook.xml'));sheets={}
    for sh in wb.findall('m:sheets/m:sheet',NS):
        name=sh.get('name')
        if names and name not in names:continue
        target=rels[sh.get(RNS+'id')];xmlpath=target.lstrip('/') if target.startswith('/') else 'xl/'+target
        root=ET.fromstring(z.read(xmlpath));cells={};rows={}
        for c in root.findall('m:sheetData/m:row/m:c',NS):
            ref=c.get('r');v=stringval(c,ss)
            if v is None:continue
            cells[ref]=v;r=int(re.search(r'\d+$',ref).group());rows.setdefault(r,{})[colnum(ref)]=v
        sheets[name]={'name':name,'cells':cells,'rows':rows}
    z.close();return sheets

def clean(v):return '' if v is None else (str(int(v)) if isinstance(v,float) and v.is_integer() else str(v)).strip()
def xtrim(v):return re.sub(' +',' ',clean(v))
def numeric(v):return isinstance(v,(int,float)) and not isinstance(v,bool)
def number(v):
    if numeric(v):return v
    try:return float(clean(v).replace(',','')) if clean(v) else None
    except:return None
def dparse(v):
    if not v:return None
    if numeric(v):return (datetime(1899,12,30)+timedelta(days=int(v))).date()
    txt=clean(v)
    for fmt,size in [('%Y-%m-%d',10),('%m-%d-%Y',10),('%d/%m/%Y',10),('%m/%d/%Y',10),('%d %b %Y',11)]:
        try:return datetime.strptime(txt[:size],fmt).date()
        except:pass
    return None
def counts(xs):return dict(collections.Counter(xs))
def date_stats(xs):
    vs=[x for x in xs if x];return {'min':str(min(vs)),'max':str(max(vs)),'present':len(vs)} if vs else {'present':0}
def key_records(sh,keycol,firstrow):return [(r,row) for r,row in sh['rows'].items() if r>=firstrow and clean(row.get(keycol))]
def idstats(records,col):
    vs=[clean(row.get(col)) for r,row in records if clean(row.get(col))];cs=collections.Counter(vs)
    return {'records':len(records),'nonnull_keys':len(vs),'unique_keys':len(cs),'duplicate_key_values':sum(n>1 for n in cs.values()),'duplicate_rows_beyond_first':sum(n-1 for n in cs.values()),'first_row':min([r for r,row in records] or [0]),'last_row':max([r for r,row in records] or [0])}
def value_equal(a,b):
    sa,sb=clean(a),clean(b)
    if sa==sb:return True
    if re.fullmatch(r'[+-]?\d+(?:\.\d+)?',sa) and re.fullmatch(r'[+-]?\d+(?:\.\d+)?',sb):
        try:return Decimal(sa)==Decimal(sb)
        except InvalidOperation:pass
    return False
def compare_rows(a,b,keycol_a=1,keycol_b=1,firstrow_a=3,firstrow_b=3,width=81):
    ar=key_records(a,keycol_a,firstrow_a);br=key_records(b,keycol_b,firstrow_b)
    ad={clean(row.get(keycol_a)):row for r,row in ar};bd={clean(row.get(keycol_b)):row for r,row in br}
    common=set(ad)&set(bd);fields=collections.Counter();changed=0
    for key in common:
        diffs=[collabel(i) for i in range(1,width+1) if not value_equal(ad[key].get(i),bd[key].get(i))]
        if diffs:changed+=1;fields.update(diffs)
    return {'left':a['name'],'right':b['name'],'key_columns':[collabel(keycol_a),collabel(keycol_b)],'left_records':len(ar),'right_records':len(br),'left_unique_keys':len(ad),'right_unique_keys':len(bd),'shared_keys':len(common),'left_only_keys':len(ad)-len(common),'right_only_keys':len(bd)-len(common),'shared_keys_with_different_last_record_values':changed,'changed_columns_on_shared_keys':dict(fields),'method':'trimmed exact identifier string match; compare last row per key; normalize decimal representation only when comparing field values, never when matching identifiers. For line-item datasets this is a last-row comparison, not a complete item-sequence equivalence test. No names, phones or addresses retained.'}

def summarize_raw(sh):
    out={}
    for name,keycol in [('RAW_Bosta',1),('RAW_Costs',3),('RAW_Intake',4),('RAW_SKU',1),('RAW_Shopify',1)]:
        if name not in sh:continue
        records=key_records(sh[name],keycol,3);o=idstats(records,keycol)
        if name=='RAW_Bosta':
            o.update({'types':counts(xtrim(row.get(2)) for r,row in records),'delivery_states':counts(xtrim(row.get(12)) for r,row in records),'created_dates':date_stats(dparse(row.get(3)) for r,row in records),'business_reference':idstats(records,10),'attempt_counts':counts(clean(row.get(15)) for r,row in records),'cod_total':sum(row.get(20,0) for r,row in records if numeric(row.get(20))),'description_line_counts':counts(len(clean(row.get(22)).split('\n')) for r,row in records),'phone_nonempty':sum(bool(clean(row.get(17))) for r,row in records),'unique_phones_trim_only':len(set(clean(row.get(17)) for r,row in records if clean(row.get(17))))})
        if name=='RAW_Costs':o.update({'total_fees':sum(row.get(32,0) for r,row in records if numeric(row.get(32))),'shipping_fees':sum(row.get(17,0) for r,row in records if numeric(row.get(17))),'vat':sum(row.get(26,0) for r,row in records if numeric(row.get(26))),'order_status':counts(clean(row.get(6)) for r,row in records),'order_types':counts(clean(row.get(4)) for r,row in records),'completed_dates':date_stats(dparse(row.get(11)) for r,row in records)})
        if name=='RAW_Intake':o.update({'call_status':counts(xtrim(row.get(11)) for r,row in records),'root_causes':counts(xtrim(row.get(13)) for r,row in records),'resolutions':counts(xtrim(row.get(15)) for r,row in records),'blank_return_type':sum(not clean(row.get(10)) for r,row in records),'blank_size_detail':sum(not clean(row.get(14)) for r,row in records),'blank_refund':sum(not clean(row.get(16)) for r,row in records),'blank_recoverable':sum(not clean(row.get(17)) for r,row in records)})
        if name=='RAW_SKU':o.update({'unique_products':len(set(clean(row.get(2)) for r,row in records)),'sum_variant_prices':sum(row.get(4,0) for r,row in records if numeric(row.get(4))),'sum_variant_cogs':sum(row.get(5,0) for r,row in records if numeric(row.get(5))),'numeric_prices':sum(numeric(row.get(4)) for r,row in records),'numeric_cogs':sum(numeric(row.get(5)) for r,row in records)})
        if name=='RAW_Shopify':
            headers=[(r,row) for r,row in records if clean(row.get(3))];o.update({'line_item_rows':len(records),'order_header_rows_by_nonblank_financial_status':len(headers),'header_unique_order_refs':len(set(clean(row.get(1)) for r,row in headers)),'created_dates':date_stats(dparse(row.get(16)) for r,row in headers),'financial_status':counts(clean(row.get(3)) for r,row in headers),'fulfillment_status':counts(clean(row.get(5)) for r,row in headers),'shipping_methods':counts(clean(row.get(15)) for r,row in headers),'cancelled_headers':sum(bool(clean(row.get(47))) for r,row in headers),'header_total_value_after_numeric_text_conversion':sum(number(row.get(12)) or 0 for r,row in headers),'header_total_values_stored_as_number':sum(numeric(row.get(12)) for r,row in headers),'header_total_values_stored_as_text':sum(isinstance(row.get(12),str) for r,row in headers),'tag_tokens':counts(t.strip() for r,row in headers for t in clean(row.get(57)).split(',') if t.strip())})
        out[name]=o
    return out

def parse_product_slots(desc):
    replaced=str(desc or '').replace('\n',' '*180);slots=[]
    for idx in range(4):
        line=xtrim(replaced[idx*180:(idx+1)*180])
        if not line:slots.append(('',0));continue
        if line[-1:].isdigit() and (line[-3:-2].upper()=='X' or line[-2:-1].upper()=='X'):
            key=xtrim(line[:-4] if line[-3:-2].upper()=='X' else line[:-3]);qty=int(line[-1])
        else:key=line;qty=1
        slots.append((key,qty))
    return slots

def reconstruct(sh):
    cfg=sh['Config']['cells'];bosta=key_records(sh['RAW_Bosta'],1,3);costs=key_records(sh['RAW_Costs'],3,3);intake=key_records(sh['RAW_Intake'],4,3);skus=key_records(sh['RAW_SKU'],1,3)
    sku={xtrim(row.get(1)).casefold():row for r,row in skus};fee=collections.defaultdict(float)
    for r,row in costs:
        if r<=2002 and numeric(row.get(32)):fee[clean(row.get(3))]+=row[32]
    intakemap={}
    for r,row in intake:intakemap.setdefault(clean(row.get(4)),(r,row))
    cities={clean(cfg.get('B'+str(r))):clean(cfg.get('C'+str(r))) for r in range(59,90)}
    taxonomy={clean(cfg.get('B'+str(r))):clean(cfg.get('C'+str(r))) for r in range(93,118)}
    channels={clean(cfg.get('B'+str(r))):clean(cfg.get('C'+str(r))) for r in range(136,140)}
    masters=[];aovs=[]
    for r,row in bosta:
        if r>2002:continue
        typ=xtrim(row.get(2));state=xtrim(row.get(12));ident=xtrim(row.get(1));chan=channels.get(typ,'Other')
        group='Returned' if typ=='RTO' else ('Customer return' if typ=='CUSTOMER_RETURN_PICKUP' else ('Exchange return' if typ=='EXCHANGE_return' else ('Delivered' if 'deliver' in state.lower() else ('Cancelled' if 'cancel' in state.lower() else 'In transit'))))
        slots=parse_product_slots(row.get(22));sp=sc=0;missing=0
        for key,qty in slots:
            if not key:continue
            sr=sku.get(key.casefold())
            if sr:
                sp+=qty*(sr.get(4,0) if numeric(sr.get(4)) else 0);sc+=qty*(sr.get(5,0) if numeric(sr.get(5)) else 0)
            else:missing+=1
        cod=row.get(20,0) if numeric(row.get(20)) else 0
        if group=='Delivered' and cod>0:aovs.append(cod)
        ir=intakemap.get(ident);intakerow=ir[1] if ir else {};created=dparse(row.get(3));complete=dparse(row.get(14)) or dparse(row.get(13));attempts=row.get(15)
        masters.append({'source_row':r,'dm_row':r+1,'id':ident,'ref':xtrim(row.get(10)),'type':typ,'state':state,'group':group,'channel':chan,'city':xtrim(row.get(19)),'zone':cities.get(xtrim(row.get(19)),'Unmapped'),'created':created,'completed':complete,'attempts':attempts,'excess':max(0,attempts-2) if chan=='Outbound' and numeric(attempts) else 0,'cycle':max(0,(complete-created).days) if complete and created else None,'call':xtrim(intakerow.get(11)),'cause':xtrim(intakerow.get(13)),'cause_owner':taxonomy.get(xtrim(intakerow.get(13)),'UNMAPPED CAUSE') if xtrim(intakerow.get(13)) else '', 'resolution':xtrim(intakerow.get(15)),'intake_found':ir is not None,'cod':cod,'sku_value':sp,'sku_cogs':sc,'qty':sum(q for k,q in slots),'sku_missing_slots':missing,'fee':fee.get(ident) if fee.get(ident,0)>0 else None,'description_lines':len(clean(row.get(22)).split('\n')),'phone':xtrim(row.get(17))})
    aov=sum(aovs)/len(aovs) if aovs else None
    ps=sum(row.get(4,0) for r,row in skus if numeric(row.get(4)));cs=sum(row.get(5,0) for r,row in skus if numeric(row.get(5)));gm=1-cs/ps if ps and cs else None
    for m in masters:
        m['value']=m['cod'] if m['cod']>0 else (m['sku_value'] if m['sku_value']>0 else aov)
        m['value_source']='COD' if m['cod']>0 else ('SKU list' if m['sku_value']>0 else ('AOV proxy' if aov is not None else 'none'))
        m['margin_lost']=(max(0,m['value']-m['sku_cogs']) if m['sku_cogs']>0 else m['value']*gm) if m['group'] in ['Returned','Customer return'] and m['value'] is not None and gm is not None else None
    references=collections.defaultdict(list)
    for m in masters:references[m['ref']].append(m)
    om=[]
    if 'RAW_Shopify' in sh:
        headers=[(r,row) for r,row in key_records(sh['RAW_Shopify'],1,3) if clean(row.get(3)) and r<=5002][:2000]
        asof=max([dparse(row.get(16)) for r,row in headers if dparse(row.get(16))] or [date(1900,1,1)])
        for r,row in headers:
            ref=clean(row.get(1));placed=dparse(row.get(16));fin=clean(row.get(3));cancel=dparse(row.get(47));method=clean(row.get(15));legs=references.get(ref,[]);tags=clean(row.get(57));val=number(row.get(12))
            channel='Office pickup' if method==clean(cfg.get('C195')) else ('Bosta' if legs else ('Pickup - unrecorded' if fin=='paid' and not cancel and val and placed and placed<=asof-timedelta(days=cfg.get('C205',2)) else 'Not fulfilled'))
            confirmed=clean(cfg.get('C183','confirmed omar')).lower() in tags.lower() or clean(cfg.get('C182','Confirmed')).lower() in tags.lower()
            by='Omar' if confirmed and clean(cfg.get('C183','confirmed omar')).lower() in tags.lower() else ('Hadeer / auto' if confirmed else 'n/a')
            wh='Disconnected' if clean(cfg.get('C185','Whatsapp Disconnected')).lower() in tags.lower() else ('Template error' if clean(cfg.get('C186','WHAPI-Template-Error')).lower() in tags.lower() else ('Undeliverable' if clean(cfg.get('C187','Message Undeliverable')).lower() in tags.lower() else 'No failure logged'))
            outcome='n/a' if not legs else ('RTO' if any(m['state']=='Returned to origin' for m in legs) else ('Delivered' if any(m['state']=='Delivered' for m in legs) else 'In transit / other'))
            pickup='Collected (inferred)' if channel=='Pickup - unrecorded' else ('n/a' if channel!='Office pickup' else ('Collected' if fin=='paid' else ('No-show' if fin in ['voided','refunded'] else ('Open' if fin=='pending' else 'Other'))))
            age=(asof-placed).days if pickup=='Open' and placed else None
            flag='KILL' if age is not None and age>=cfg.get('C203',7) else ('FLAG' if age is not None and age>=cfg.get('C202',3) else ('OK' if age is not None else ''))
            om.append({'ref':ref,'source_row':r,'placed':placed,'financial_status':fin,'channel':channel,'confirmed':confirmed,'confirmed_by':by,'whappi':wh,'bosta_legs':len(legs),'outcome':outcome,'cancel_stage':'none' if not cancel else ('Post-dispatch' if legs else 'Pre-dispatch'),'pickup_status':pickup,'pickup_age':age,'pickup_flag':flag,'value':val})
    retgroups=['Returned','Customer return','Exchange return'];returned=[m for m in masters if m['group'] in retgroups]
    summary={'method':'Independent Python reproduction of inspected formula semantics from raw input values. No Excel engine, no workbook recalculation, no saved transformed records. Aggregates are evidence about supplied artifacts, not live application results. Case-insensitive SKU matching and trimmed identifiers reproduce MATCH/SUMIF intention; Excel edge coercion is a residual limit.','references':['DATA_Master!A4:BC2003','Orders_Master!A4:X2003','Config!C34:C40','RAW_Bosta!A3:AC571','RAW_Costs!C3:AF1383','RAW_SKU!A3:E62'], 'shipments':len(masters),'status_groups':counts(m['group'] for m in masters),'channels':counts(m['channel'] for m in masters),'created_dates':date_stats(m['created'] for m in masters),'completed_dates':date_stats(m['completed'] for m in masters),'value_sources':counts(m['value_source'] for m in masters),'courier_fee_rows':sum(m['fee'] is not None for m in masters),'courier_fee_sum':sum(m['fee'] or 0 for m in masters),'wallet_rows_without_bosta_match':len(set(clean(row.get(3)) for r,row in costs)-set(m['id'] for m in masters)),'sku_value_sum':sum(m['sku_value'] for m in masters),'order_value_sum':sum(m['value'] or 0 for m in masters),'margin_lost_sum':sum(m['margin_lost'] or 0 for m in masters),'aov_delivered_positive_cod':aov,'blended_cogs_pct':1-gm if gm is not None else None,'gross_margin_pct':gm,'saved_return_margin_proxy':aov*gm if aov is not None and gm is not None else None,'unmapped_city_count':sum(m['zone']=='Unmapped' for m in masters),'intake_joined_shipments':sum(m['intake_found'] for m in masters),'return_groups':len(returned),'return_group_with_root_cause':sum(bool(m['cause']) for m in returned),'return_root_cause_counts':counts(m['cause'] or '[blank]' for m in returned),'return_call_status_counts':counts(m['call'] or '[blank]' for m in returned),'sku_missing_shipments':sum(m['sku_missing_slots']>0 for m in masters),'sku_missing_slots':sum(m['sku_missing_slots'] for m in masters),'descriptions_over_four_lines':sum(m['description_lines']>4 for m in masters),'outbound_numeric_attempts_mean':sum(m['attempts'] for m in masters if m['channel']=='Outbound' and numeric(m['attempts']))/max(1,sum(m['channel']=='Outbound' and numeric(m['attempts']) for m in masters)),'excess_attempts_sum':sum(m['excess'] for m in masters)}
    if om:
        summary['orders']={'count':len(om),'placed_dates':date_stats(o['placed'] for o in om),'fulfillment_channels':counts(o['channel'] for o in om),'confirmed_by':counts(o['confirmed_by'] for o in om),'confirmation_coverage_hadeer_auto':sum(o['confirmed_by']=='Hadeer / auto' for o in om)/len(om),'confirmation_coverage_all':sum(o['confirmed'] for o in om)/len(om),'whappi_signal':counts(o['whappi'] for o in om),'cancel_stage':counts(o['cancel_stage'] for o in om),'outbound_outcome':counts(o['outcome'] for o in om),'pickup_status':counts(o['pickup_status'] for o in om),'pickup_flags':counts(o['pickup_flag'] for o in om),'office_pickup_with_bosta_legs':sum(o['channel']=='Office pickup' and o['bosta_legs']>0 for o in om),'order_value_sum':sum(o['value'] or 0 for o in om),'bosta_dispatched':sum(o['bosta_legs']>0 for o in om),'asof':str(asof)}
    return summary,masters,om

def csv_profile(path,live=False):
    with path.open(encoding='utf-8-sig',newline='') as f:reader=csv.DictReader(f);rows=list(reader);headers=reader.fieldnames
    if live:
        return {'source':str(path),'headers':headers,'rows':len(rows),'order_keys':len(set(clean(r.get('Order')) for r in rows)),'date_range':date_stats(dparse(r.get('Date')) for r in rows),'channel_counts':counts(r.get('Channel','') for r in rows),'outcome_counts':counts(r.get('Outcome','') for r in rows),'status_counts':counts(r.get('Status','') for r in rows),'confirmed_by_counts':counts(r.get('Confirmed by','') for r in rows),'bosta_state_counts':counts(r.get('Bosta state','') for r in rows)},rows
    first=[r for r in rows if clean(r.get('Financial Status'))]
    return {'source':path.name,'headers':headers,'line_item_rows':len(rows),'unique_order_refs':len(set(clean(r.get('Name')) for r in rows)),'order_header_rows':len(first),'date_range':date_stats(dparse(r.get('Created at')) for r in first),'financial_status_counts':counts(r.get('Financial Status','') for r in first),'fulfillment_status_counts':counts(r.get('Fulfillment Status','') for r in first),'tag_tokens':counts(t.strip() for row in first for t in row.get('Tags','').split(',') if t.strip())},rows

if __name__=='__main__':
    books={};summary={};calc={};order_sets={};master_sets={}
    names=['Config','RAW_Bosta','RAW_Costs','RAW_Intake','RAW_SKU','RAW_Shopify']
    files=['02_Gentry_Delivery_Performance_System.xlsx','02_Gentry_Delivery_Performance_System_v2.0_BACKUP_2026-08-28.xlsx','02_Gentry_Delivery_Performance_System_v3.0_BACKUP_2026-09-08.xlsx']
    for file in files:
        print('Reconciling',file,flush=True);sh=selected_book(SOURCE/file,names);books[file]=sh;summary[file]=summarize_raw(sh);calc[file],master_sets[file],order_sets[file]=reconstruct(sh)
    cur=books[files[0]];comparisons=[]
    for file in files[1:]:
        for s,key in [('RAW_Bosta',1),('RAW_Costs',3),('RAW_Intake',4),('RAW_SKU',1),('RAW_Shopify',1)]:
            if s in books[file]:comparisons.append({'left_workbook':files[0],'right_workbook':file,**compare_rows(cur[s],books[file][s],key,key,width=81 if s=='RAW_Shopify' else (36 if s=='RAW_Costs' else 29))})
    stages=[]
    for file,sheet,target,key,w in [('2026-09-08_RAW_Bosta_STAGED_20May-06Sep.xlsx','RAW_Bosta_PASTE','RAW_Bosta',1,29),('2026-09-08_RAW_Shopify_STAGED_18Jun-08Sep.xlsx','RAW_Shopify_PASTE','RAW_Shopify',1,81),('2026-09-08_RAW_SKU_ADDITIONS.xlsx','RAW_SKU_ADDITIONS','RAW_SKU',1,5),('2026-09-08_Hadeer_CallQueue_TopUp_27rows.xlsx','PASTE_AT_A102','RAW_Intake',4,5)]:
        stage=selected_book(SOURCE/file)[sheet];stages.append({'staged_source':file,**compare_rows(cur[target],stage,key,key,3,2,w)})
    csvp,csvrows=csv_profile(SOURCE/'2026-08-28_Shopify_orders_18Jun-17Aug.csv');csvrefs=set(clean(r.get('Name')) for r in csvrows)
    csvp['workbook_order_key_overlap']={file:{'shared':len(csvrefs&set(o['ref'] for o in order_sets[file])),'csv_only':len(csvrefs-set(o['ref'] for o in order_sets[file])),'workbook_only':len(set(o['ref'] for o in order_sets[file])-csvrefs)} for file in [files[0],files[2]]}
    livepath=Path(r'D:\Downloads\orders-2026-10-13.csv');live=None
    if livepath.exists():
        live,liverows=csv_profile(livepath,True);livemap={clean(r.get('Order')):r for r in liverows};liveset=set(livemap)
        live['key_match_method']='Exact trimmed Order vs Shopify Name/order_ref strings only. No match based on customer or phone, no numeric identifier inference.'
        live['source_order_overlap']={}
        for file in [files[0],files[2]]:
            om=order_sets[file];osm={o['ref']:o for o in om};oss=set(osm);common=liveset&oss;date_mismatches=[key for key in common if dparse(livemap[key].get('Date'))!=osm[key]['placed']]
            live['source_order_overlap'][file]={'source_orders':len(oss),'live_orders':len(liveset),'exact_shared_keys':len(common),'source_only_keys':len(oss-liveset),'live_only_keys':len(liveset-oss),'date_comparable_shared_keys':sum(dparse(livemap[key].get('Date')) is not None and osm[key]['placed'] is not None for key in common),'date_mismatch_count':len(date_mismatches),'source_only_placed_date_range':date_stats(osm[key]['placed'] for key in oss-liveset),'shared_source_placed_date_range':date_stats(osm[key]['placed'] for key in common),'live_only_date_range':date_stats(dparse(livemap[key].get('Date')) for key in liveset-oss),'live_outcomes_on_shared_keys':counts(livemap[key].get('Outcome','') for key in common),'source_formula_outcomes_on_shared_keys':counts(osm[key]['outcome'] for key in common)}
    output={'privacy':'Only aggregate statistics, schema, formula/cell references and control values retained. Raw customer names, emails, phones, addresses and private transaction identifiers are never output. Source and live CSV opened read-only.','raw_workbook_profiles':summary,'backup_input_comparisons':comparisons,'staged_input_comparisons':stages,'source_csv_profile':csvp,'independent_formula_reconstruction':calc,'live_csv_comparison':live}
    (OUT/'reconciliation.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf-8');print('Wrote sanitized reconciliation.json',flush=True)
