"""Read saved bundle bytes; never import, evaluate, or execute the JavaScript."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
ASSETS = {p.name: p.read_bytes() for p in sorted((ROOT / 'assets').glob('*.js'))}
OBS = json.loads((ROOT / 'public-http-observations.json').read_text(encoding='utf-8-sig'))
SNIPPETS = []
FINDINGS = []


def snippet(file, needle, before=0, after=0):
    data = ASSETS[file]
    position = data.find(needle.encode('utf-8'))
    if position < 0:
        raise ValueError((file, needle))
    start = max(0, position - before)
    end = min(len(data), position + len(needle.encode('utf-8')) + after)
    row = dict(id=f'S{len(SNIPPETS) + 1:02}', file='assets/' + file,
               byte_start=start, byte_end_exclusive=end,
               needle_byte_start=position, snippet=data[start:end].decode('utf-8'),
               source_sha256=hashlib.sha256(data).hexdigest())
    SNIPPETS.append(row)
    return row['id']


def add(fid, scope, title, conclusion, limits, evidence=()):
    FINDINGS.append(dict(id=fid, scope=scope, title=title, conclusion=conclusion,
                         limits=limits, evidence_ids=list(evidence),
                         classification='Hypothesis / unresolved question' if scope == 'unresolved'
                         else 'Verified fact (static delivered-client code)'))


add('APP01', 'gentry-specific', 'Shared application navigation',
    'Module 56850 exports Icon, Logo, SideNav and TabNav. Logo renders a link to / labeled Gentry Ops. '
    'SideNav and TabNav render items supplied through props. Selected navigation uses exact match '
    'or the longest matching non-root path prefix.',
    'No actual navigation item list is embedded here. A link string proves client-code intent, '
    'not route availability or authorization. Icon names, including users, are drawing options, not role rules.',
    [snippet('15qydxckj0uxx.js', 'function a(e,t){let r=null;for(let{href:n}of t)', after=155),
     snippet('15qydxckj0uxx.js', 'e.s(["Icon",0,u,"Logo",0,function()', after=1260)])
add('APP02', 'gentry-specific', 'Navigation overflow behavior',
    'TabNav scrolls its selected aria-current=page item into view when the selected path changes.',
    'This display behavior neither inspects record state nor enforces access.',
    [snippet('15qydxckj0uxx.js', '"TabNav",0,function({items:e})', after=570)])
add('APP03', 'gentry-specific', 'Theme preference',
    'ThemeToggle takes initialDark and toggles the document dark class on click. It writes theme=dark '
    'or light with path=/, max-age=31536000 and samesite=lax, then updates local state.',
    'This is a presentation cookie. It does not identify a login cookie, token, session backend or '
    'permission implementation. No theme click was performed by this worker.',
    [snippet('15qydxckj0uxx.js', 'e.s(["ThemeToggle",0,function', after=655)])
add('FW01', 'framework-generic', 'Turbopack bootstrap',
    'The bootstrap registers delivered chunks and runtime module 94553. The chunk-loader base path defaults to /_next/.',
    'A bundle manifest is not a backend inventory. Unseen chunks may carry page components. '
    'This worker fetched no chunk referenced only in code strings.',
    [snippet('turbopack-3bohnvk-2ex_3.js', '{otherChunks:[', after=304),
     snippet('turbopack-3bohnvk-2ex_3.js', 'U="string"==typeof TURBOPACK_CHUNK_BASE_PATH?', after=134)])
add('FW02', 'framework-generic', 'Delivered Next.js version declaration',
    'The bootstrap assigns window.next={version:"16.3.5",appDir:!0}. This identifies the version '
    'declaration shipped in these bytes and App Router mode.',
    'This is not package.json, a lockfile, backend source, or independent proof of every server dependency.',
    [snippet('27t_qfc-3_lzs.js', 'window.next={version:"16.3.5",appDir:!0}')])
add('FW03', 'framework-generic', 'Delivered React version declarations',
    'React and React DOM declare 19.3.0-canary-cbb046ab-20260731. React DOM also checks the '
    'React version against that literal.',
    'These are delivered runtime declarations, not a recommendation for a replacement system.',
    [snippet('19mx3mg6lkumu.js', 'r.version="19.3.0-canary-cbb046ab-20260731"'),
     snippet('27t_qfc-3_lzs.js', 'if("19.3.0-canary-cbb046ab-20260731"!==f9)', after=90),
     snippet('0ay527mnq1105.js', 't.version="19.3.0-canary-cbb046ab-20260731"')])
add('FW04', 'framework-generic', 'Polyfill library',
    'The polyfill chunk records core-js version 3.38.1 in global mode with license/source URLs.',
    'Polyfill URLs and URL-parser test values are library content, not Gentry integrations or production endpoints.',
    [snippet('0cz1d0mv5g_q7.js', 'push({version:"3.38.1",mode:"global"', after=236)])
add('FW05', 'framework-generic', 'Flight transport headers',
    'The framework declares rsc, next-action, next-router-state-tree, next-router-prefetch, '
    'next-router-segment-prefetch, next-hmr-refresh, next-url and text/x-component constants. '
    'It also declares _rsc, action-not-found and action-revalidated markers.',
    'These define transport implementation available in this build. Actual authenticated requests '
    'and response values require separate browser/network observations.',
    [snippet('2bub_m4veo3fm.js', 'let l="rsc",u="next-action"', after=502)])
add('FW06', 'framework-generic', 'Initial Flight hydration',
    'The bootstrap consumes self.__next_f into a ReadableStream. Tag 0 initializes a queue, '
    '1 carries encoded text, 2 sets form state, and 3 decodes base64 binary bytes. It then calls '
    'createFromReadableStream, or createFromFetch for client-resume/test paths.',
    'Protocol support exposes no domain status transition or per-user access rule. '
    'No Flight payload was inspected within this delegated input scope.',
    [snippet('27t_qfc-3_lzs.js', 'function L(e){if(0===e[0])a=[];', after=733),
     snippet('27t_qfc-3_lzs.js', 'let M=self.__next_f=self.__next_f||[];', after=355),
     snippet('27t_qfc-3_lzs.js', 'else l=_(I,{callServer:h.callServer', after=140)])
add('FW07', 'framework-generic', 'Flight navigation requests',
    'Navigation fetch prepares RSC and router-state headers, optionally next-url, and requests '
    'with credentials:same-origin. Non-Flight, failed, bodyless or mismatched-build responses '
    'fall back to browser navigation.',
    'The generic credentials option does not prove cookie names, expiry, session backend '
    'or which Gentry routes were requested.',
    [snippet('2bub_m4veo3fm.js', 'async function v(e,t){let{flightRouterState:r,nextUrl:n}=t', after=515),
     snippet('2bub_m4veo3fm.js', 'let u={credentials:"same-origin",headers:t', after=162)])
add('FW08', 'framework-generic', 'Server-action dispatch',
    'callServer returns a Promise and dispatches ACTION_SERVER_ACTION with actionId, actionArgs, '
    'resolve and reject inside startTransition.',
    'Identity and arguments are supplied dynamically. This dispatcher names no Gentry business function.',
    [snippet('0ay527mnq1105.js', 'async function l(e,n){return new Promise((t,l)=>', after=260)])
add('FW09', 'framework-generic', 'Server references and bound arguments',
    'The React client provides createServerReference, which wraps an identifier and callback. '
    'It resolves streamed references through id and bound fields, concatenating bound arguments '
    'before calling the server callback.',
    'No application-specific server-reference creation with a literal action ID is present in '
    'the initial nine assets. Rendered forms/Flight can carry identities separately.',
    [snippet('0ay527mnq1105.js', 't.createServerReference=function(e,n){', after=136),
     snippet('0ay527mnq1105.js', 'function G(e,n,t,r){if(!e._serverReferenceConfig)', after=356)])
add('FW10', 'framework-generic', 'Server-action HTTP protocol',
    'The reducer encodes action arguments with encodeReply, sends a POST to the current canonical URL, '
    'and places the dynamic ID in next-action. Accept is text/x-component, router state is encoded, '
    'and optional deployment/next-url fields are added.',
    'This does not identify a Gentry-specific /api action route or establish server validation, '
    'authorization, side effects, idempotency or successful execution. No action was called.',
    [snippet('2bub_m4veo3fm.js', 'async function F(e,t,r){let s,d,h,y,g,{actionId:_,actionArgs:R}=r', after=784)])
add('FW11', 'framework-generic', 'Server-action response handling',
    'The reducer checks x-nextjs-action-not-found, parses x-action-redirect with push/replace, '
    'parses x-action-revalidated and decodes a Flight response. It rejects an unexpected '
    'non-Flight response when no redirect was supplied.',
    'These generic outcomes cannot establish operation-specific Gentry success, retry or audit rules.',
    [snippet('2bub_m4veo3fm.js', 'if("1"===s.headers.get(u.NEXT_ACTION_NOT_FOUND_HEADER))', after=509),
     snippet('2bub_m4veo3fm.js', 'let e=s.headers.get("x-action-revalidated")', after=545)])
add('FW12', 'framework-generic', 'Server-reference identifier format',
    'The helper expects length 42. The first hex byte encodes use-cache versus server-action, '
    'six used-argument bits and a rest-arguments bit. omitUnusedArgs builds the outgoing argument list.',
    'No 42-character hexadecimal identity occurs in the initial nine assets. This is format logic, '
    'not a Gentry action catalog.',
    [snippet('2bub_m4veo3fm.js', 'let l=42;function u(e){return e.length===l}', after=453)])
add('FW13', 'framework-generic', 'Router refresh implementation',
    'Public app-router refresh dispatches ACTION_REFRESH inside startTransition. The queue may '
    'request refresh after a discarded server action revalidated data. Generic error retry also '
    'calls context refresh before resetting error state.',
    'No Gentry timer or cadence is established by the initial assets. UI rerender/route refresh '
    'and upstream integration synchronization remain different questions.',
    [snippet('2bub_m4veo3fm.js', 'refresh:()=>{(0,i.startTransition)', after=112),
     snippet('2bub_m4veo3fm.js', 't.payload.type===l.ACTION_SERVER_ACTION&&t.payload.didRevalidate', after=84),
     snippet('19mx3mg6lkumu.js', 'this.retry=()=>{(0,i.startTransition)', after=99)])
add('FW14', 'framework-generic', 'HTTP fallback display does not establish RBAC',
    'HTTPAccessFallbackBoundary displays supplied notFound/forbidden/unauthorized components '
    'when corresponding framework error statuses are thrown. React role matches concern ARIA/DOM attributes.',
    'Fallback display does not prove a Gentry authorization check or role matrix. No app-specific '
    'role comparison or permission predicate was identified in the initial collection.',
    [snippet('3fntmmi971322.js', 'render(){let{notFound:e,forbidden:t,unauthorized:r,children:n}', after=644),
     snippet('27t_qfc-3_lzs.js', 't.id="__next-route-announcer__",t.role="alert"'),
     snippet('27t_qfc-3_lzs.js', 'case"dir":case"role":case"viewBox"')])
add('FW15', 'framework-generic', 'Domain-like strings with unrelated framework meaning',
    'WhatsApp appears in a bot-user-agent regex. cleanup names an LRU/cache export and call. '
    'Neither is Gentry WhatsApp integration or order-cleanup workflow evidence.',
    'Meta matches concern metadata/polyfills; users is an icon key. Explicit Shopify/Bosta/Whapi '
    'connector configuration or request code was not identified in these initial assets.',
    [snippet('2bub_m4veo3fm.js', 'facebookexternalhit|facebookcatalog|Twitterbot', before=40, after=115),
     snippet('2bub_m4veo3fm.js', 'var n={cleanup:function(){return h}', after=140)])
add('GAP01', 'unresolved', 'Page-specific client behavior outside initial coverage',
    'The initial collection confirms shared client shell code and framework transport, '
    'but not Gentry operation-specific actions, role checks, integrations or refresh cadence.',
    'More exact browser-observed page chunks and separately observed rendered forms/Flight may '
    'close these gaps. String discovery never access-verifies a route.')

CLASSIFICATIONS = {
    '0ay527mnq1105.js': 'Framework: React DOM shared exports, Flight client codec and action dispatcher.',
    '0cz1d0mv5g_q7.js': 'Library: core-js global polyfills and feature tests.',
    '15qydxckj0uxx.js': 'Mixed: Next Link/URL helpers; Gentry navigation and theme modules.',
    '19mx3mg6lkumu.js': 'Framework: React, Next routing/error helpers and contexts.',
    '27t_qfc-3_lzs.js': 'Framework: Next App Router bootstrap and React DOM renderer.',
    '2bub_m4veo3fm.js': 'Framework: Next router queue/cache/navigation and action protocol.',
    '310vm2bl3xxpt.js': 'Framework: Next default global error page and styles.',
    '3fntmmi971322.js': 'Framework: client roots, layout router and access-error fallbacks.',
    'turbopack-3bohnvk-2ex_3.js': 'Framework: Turbopack runtime and chunk loader.',
}
MANIFEST = []
for name, data in ASSETS.items():
    indices = [i for i, o in enumerate(OBS) if o.get('path', '').endswith('/' + name)]
    digest = hashlib.sha256(data).hexdigest()
    ledger = OBS[indices[-1]] if indices else {}
    MANIFEST.append(dict(file='assets/' + name, bytes=len(data), sha256=digest,
                         classification=CLASSIFICATIONS.get(name, 'Additional asset; not yet semantically classified'),
                         http_ledger_matches=ledger.get('sha256') == digest and ledger.get('body_bytes') == len(data),
                         http_observation_array_indices=indices))
SCANS = {}
for key, pattern in {
    'literal_42_hex_ids': rb'(?<![0-9a-f])[0-9a-f]{42}(?![0-9a-f])',
    'setInterval': rb'setInterval',
    'sourceMappingURL': rb'sourceMappingURL',
    'explicit_integration_names': rb'Shopify|shopify|Bosta|bosta|Whapi|whapi|Hadeer|Omar',
}.items():
    SCANS[key] = [dict(file='assets/' + name, byte_start=m.start(), matched=m.group().decode('ascii'))
                  for name, data in ASSETS.items() for m in re.finditer(pattern, data)]
RESULT = dict(
    title='Phase 1B delivered-client static analysis', updated_at_utc=datetime.now(timezone.utc).isoformat(),
    input_scope=['assets/*.js', 'public-http-observations.json'],
    method='Read saved byte sequences and inspect static logic only. No application JavaScript '
           'execution, navigation, network fetch, credentials, action call or original-source mutation.',
    offset_convention='Zero-based raw byte offsets; end is exclusive. Snippets are exact contiguous UTF-8 slices.',
    coverage=dict(asset_count=len(ASSETS), total_bytes=sum(map(len, ASSETS.values())),
                  all_assets_match_http_ledger=all(a['http_ledger_matches'] for a in MANIFEST),
                  snapshot='Initial nine browser-observed public assets'),
    assets=MANIFEST, findings=FINDINGS, evidence_snippets=SNIPPETS, bounded_lexical_checks=SCANS,
    public_http_observations_summary=dict(
        asset_requests=sum(bool(o.get('body_retained') and (o.get('content_type') or '').startswith('application/javascript')) for o in OBS),
        known_route_gets=[dict(o, array_index=i) for i, o in enumerate(OBS)
                          if o.get('observation_type') == 'independent unauthenticated known-route GET']),
    unresolved=['Operation-specific action identities and backend behavior', 'Actual role matrix and server enforcement',
                'Client refresh cadence', 'Integration execution and webhook/scheduler behavior',
                'Complete route inventory and access verification'],
    limits=['Delivered client bundles are not backend source.',
            'Missing explicit names in a bounded collection do not establish absent functionality.',
            'Transport and fallback components do not establish application permission checks.',
            'Route/API strings do not establish accessibility.',
            'Version literals are not a complete server dependency inventory.'])
(ROOT / 'static-analysis.json').write_text(json.dumps(RESULT, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

LINES = [
    '# Phase 1B delivered-client static analysis', '',
    'This review is limited to the initial nine saved JavaScript assets and `public-http-observations.json`. '
    'These are delivered client bundles, not backend source. The worker read bytes and inspected static logic; '
    'it did not execute application JavaScript, navigate, fetch additional assets, use credentials or call actions.', '',
    f"All nine assets match their HTTP-ledger SHA-256 hashes and byte counts, totaling {RESULT['coverage']['total_bytes']:,} bytes. "
    'The ledger records unauthenticated GET status 200, JavaScript content type and public immutable caching '
    'for these exact observed chunk URLs. Its known `/orders` GET returned 307 to `/login?from=%2Forders` '
    'without Set-Cookie. This proves the response to that request, not permission behavior for every route or role.', '',
    '## Reading the evidence', '',
    'Locators use zero-based raw-byte offsets, with an exclusive end. JSON retains exact bounded snippets, '
    'source hashes and structured limitations. Files are relative to this Phase 1B directory. '
    'Snippets identify present code, not a live action executed by this worker.', '',
    '## Asset coverage', '',
    '| Asset | Bytes | Content classification | Ledger match |',
    '|---|---:|---|---|',
]
for asset in MANIFEST:
    LINES.append(f"| `{asset['file']}` | {asset['bytes']:,} | {asset['classification']} | {asset['http_ledger_matches']} |")
LINES.extend(['', '## Findings', ''])
BY_ID = {s['id']: s for s in SNIPPETS}
for finding in FINDINGS:
    LINES.extend([f"### {finding['id']} — {finding['title']}", '',
                  f"**{finding['classification']}; {finding['scope']}.** {finding['conclusion']}", '', finding['limits']])
    if finding['evidence_ids']:
        locators = []
        for sid in finding['evidence_ids']:
            s = BY_ID[sid]
            locators.append(f"`{sid} {s['file']} bytes [{s['byte_start']}, {s['byte_end_exclusive']})`")
        LINES.extend(['', 'Evidence: ' + '; '.join(locators) + '.'])
    LINES.append('')
LINES.extend([
    '## App-specific routes, roles, actions and integrations', '',
    'The only literal application destination in the shared Gentry navigation is `/` in the logo. '
    'SideNav and TabNav accept items as props, so their labels and destinations cannot be reconstructed '
    'from this asset alone. Framework roots, `/_next/`, `/_not-found`, cache paths, documentation URLs '
    'and URL-parser test values are not a Gentry route inventory. The HTTP ledger separately verifies '
    'the unauthenticated `/orders` redirect. This worker access-tested no code-discovered route.', '',
    'No app-specific role predicate, literal 42-character action ID, `setInterval` timer, Shopify/Bosta/Whapi '
    'client integration code or source-map URL declaration was identified in this initial collection. '
    'This is a collection limit, not a finding that Gentry lacks these capabilities. '
    'Rendered action identities and page-specific modules can arrive separately.', '',
    'The generic action transport accepts an ID dynamically and posts encoded arguments to the current route. '
    'A rendered `$ACTION_...` identity observed elsewhere should be correlated with its form and observation. '
    'The framework dispatcher cannot name its business function or establish validation, authorization or consequences.', '',
    '## Confidence and remaining gaps', '',
    'Confidence is high for exact shipped code statements, version declarations, byte/hash correspondence '
    'and recorded public HTTP responses. Business-behavior confidence is limited: the initial collection '
    'exposes only shared Gentry navigation and theme controls. Operation-specific transitions, permissions, '
    'action semantics, refresh cadence, integration jobs and database relationships remain unresolved '
    'within this delegated input scope.', '',
    '## Exact bounded evidence snippets', '',
])
for s in SNIPPETS:
    LINES.extend([f"### {s['id']} — `{s['file']}` bytes [{s['byte_start']}, {s['byte_end_exclusive']})", '',
                  '```javascript', s['snippet'], '```', ''])
(ROOT / 'static-analysis.md').write_text('\n'.join(LINES), encoding='utf-8')
print(json.dumps(dict(assets=len(ASSETS), bytes=RESULT['coverage']['total_bytes'],
                      ledger_match=RESULT['coverage']['all_assets_match_http_ledger'],
                      findings=len(FINDINGS), snippets=len(SNIPPETS),
                      scan_counts={k: len(v) for k, v in SCANS.items()}), indent=2))
