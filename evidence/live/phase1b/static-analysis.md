# Phase 1B delivered-client static analysis

This static review covers 13 retained JavaScript assets from 14 exact observed asset GET attempts, plus the known `/orders` GET in `public-http-observations.json` (15 HTTP observations total). Four retained components extend the initial nine-asset collection. An earlier CallSheetUpload reference returned 404; a fresh exact observed chunk later returned 200 and was analyzed. Delivered bundles are client evidence, not backend source. This worker executed no application JavaScript, navigated no route, fetched no asset or alternate URL, used no credentials and called no action.

All 13 retained assets match recorded SHA-256 hashes and byte counts, totaling 607,054 bytes. Their GETs returned 200 with JavaScript content type and public immutable caching. The failed asset GET returned 404 with text/plain content type (HTTP01). The known `/orders` GET returned 307 to `/login?from=%2Forders` without Set-Cookie. These responses do not establish permission behavior for every route or role.

## Reading the evidence

Locators use zero-based raw-byte offsets with an exclusive end. JSON retains exact snippets, hashes and limitations; ledger evidence also cites a zero-based JSON array pointer. Files are relative to this Phase 1B directory. Code presence is distinct from live execution.

## Asset coverage

| Retained asset | Bytes | Content classification | Ledger match |
|---|---:|---|---|
| `assets/0ay527mnq1105.js` | 31,328 | Framework: React DOM shared exports, Flight client codec and action dispatcher. | True |
| `assets/0cz1d0mv5g_q7.js` | 112,594 | Library: core-js global polyfills and feature tests. | True |
| `assets/14x5k9f0fswg1.js` | 2,624 | Gentry component: DateRangePicker and enclosing-form submission. | True |
| `assets/15qydxckj0uxx.js` | 12,955 | Mixed: Next Link/URL helpers; Gentry navigation and theme modules. | True |
| `assets/1986ffcy11vyr.js` | 13,034 | Mixed: Next Link/URL helpers; additional Gentry navigation/theme variant. | True |
| `assets/19mx3mg6lkumu.js` | 28,907 | Framework: React, Next routing/error helpers and contexts. | True |
| `assets/1t_el1w5uiobt.js` | 1,938 | Mixed: server-reference helper exports; CallSheetUpload client state and action identity. | True |
| `assets/27t_qfc-3_lzs.js` | 229,156 | Framework: Next App Router bootstrap and React DOM renderer. | True |
| `assets/2bub_m4veo3fm.js` | 134,529 | Framework: Next router queue/cache/navigation and action protocol. | True |
| `assets/310vm2bl3xxpt.js` | 5,364 | Framework: Next default global error page and styles. | True |
| `assets/356upgw1p449j.js` | 9,269 | Mixed: Next Link/URL helpers; PrintButton browser-print control. | True |
| `assets/3fntmmi971322.js` | 14,377 | Framework: client roots, layout router and access-error fallbacks. | True |
| `assets/turbopack-3bohnvk-2ex_3.js` | 10,979 | Framework: Turbopack runtime and chunk loader. | True |

Failed exact asset attempt: `/_next/static/chunks/1kudf3dkhdpbd.js`; `public-http-observations.json#/11`; 404; body not retained. Later exact observed `1t_el1w5uiobt.js` succeeded (`#/14`). No guessed alternative was inspected; the cause of the earlier failure is unresolved.

## Gentry component findings

### APP01 — Shared application navigation

**Verified fact (static delivered-client code); gentry-specific.** Module 56850 exports Icon, Logo, SideNav and TabNav. Logo renders a link to / labeled Gentry Ops. SideNav and TabNav render items supplied through props. Selected navigation uses exact match or the longest matching non-root path prefix.

No actual navigation item list is embedded here. A link string proves client-code intent, not route availability or authorization. Icon names, including users, are drawing options, not role rules.

Evidence: `S01 assets/15qydxckj0uxx.js bytes [8983, 9185)`; `S02 assets/15qydxckj0uxx.js bytes [10197, 11492)`.

### APP02 — Navigation overflow behavior

**Verified fact (static delivered-client code); gentry-specific.** TabNav scrolls its selected aria-current=page item into view when the selected path changes.

This display behavior neither inspects record state nor enforces access.

Evidence: `S03 assets/15qydxckj0uxx.js bytes [11236, 11836)`.

### APP03 — Theme preference

**Verified fact (static delivered-client code); gentry-specific.** ThemeToggle takes initialDark and toggles the document dark class on click. It writes theme=dark or light with path=/, max-age=31536000 and samesite=lax, then updates local state.

This is a presentation cookie. It does not identify a login cookie, token, session backend or permission implementation. No theme click was performed by this worker.

Evidence: `S04 assets/15qydxckj0uxx.js bytes [11969, 12653)`.

### APP04 — Additional shared-navigation asset variant

**Verified fact (static delivered-client code); gentry-specific.** The newly retained 1986ffcy11vyr.js again exports module 56850 Icon/Logo/SideNav/TabNav and module 94013 ThemeToggle. It includes a check drawing in the icon map, alongside existing icons. SideNav receives items and direction; TabNav receives items. Both map supplied items to links and select by pathname; neither filters them by a role/permission prop or predicate in these functions.

The variant does not supply a route or label list. An upstream server may select props before rendering; this client module cannot establish that server policy. A check icon establishes a drawing option, not a named workflow, feature flag or permission. Different hashed assets with the same module IDs do not establish deployment chronology.

Evidence: `S33 assets/1986ffcy11vyr.js bytes [9226, 9344)`; `S34 assets/1986ffcy11vyr.js bytes [10664, 12111)`; `S35 assets/1986ffcy11vyr.js bytes [12048, 12481)`.

### APP05 — DateRangePicker props and preset submission

**Verified fact (static delivered-client code); gentry-specific.** Module 16340 exports DateRangePicker with period, from, to, today, min, presets, weeks and note props. It keeps period and To in component state. Choosing a preset or nonempty week sets local period, writes that value immediately to its hidden period input, disables date inputs within the component, and calls requestSubmit on the closest enclosing form.

The component does not declare the enclosing form method or action. GET filtering requires separately observed rendered-form evidence. No fetch, server-action identity, integration or data mutation is defined in this component. Disabling date controls excludes them from normal form submission; backend interpretation of the remaining period is not exposed.

Evidence: `S36 assets/14x5k9f0fswg1.js bytes [165, 623)`.

### APP06 — Custom dates and native input limits

**Verified fact (static delivered-client code); gentry-specific.** From is a date input named from with defaultValue from, min=min and max=today. To is named to with controlled state, the same bounds, and onChange updating To and selecting custom. Editing From also selects custom. The till today button appears when To differs from today and sets To=today plus period=custom without calling requestSubmit.

These are client input attributes and state updates. No from<=to comparison, date arithmetic, timezone conversion, invalid-date parser or server validation is shown. Today and min arrive as props, so their computation and values cannot be inferred. From uses defaultValue; both inputs should not be described as controlled.

Evidence: `S37 assets/14x5k9f0fswg1.js bytes [1151, 1816)`; `S38 assets/14x5k9f0fswg1.js bytes [1482, 1857)`.

### APP07 — Week selection and preset display logic

**Verified fact (static delivered-client code); gentry-specific.** The week select displays period when it starts with w, otherwise an empty value; it submits only a nonempty selection. Week options and preset buttons come from supplied arrays. A preset is highlighted when its key equals period, or when key=last-week and period is empty. Optional note is rendered as text.

The startsWith("w") convention does not establish week definitions, date boundaries, inclusivity or server presets. The selected last-week appearance for empty period is display logic, not proof of a backend default. No feature flag or role-dependent option filtering appears.

Evidence: `S39 assets/14x5k9f0fswg1.js bytes [713, 737)`; `S40 assets/14x5k9f0fswg1.js bytes [1919, 2624)`.

### APP08 — PrintButton one-shot timer and manual printing

**Verified fact (static delivered-client code); gentry-specific.** Module 44026 exports PrintButton with auto defaulting false. Its effect returns immediately unless auto is true; when true it schedules window.print after 400 ms and clears that timer on effect cleanup. The Save as PDF button calls window.print immediately on click.

This is browser print UI, not a server PDF-generation endpoint. Browser/user controls output destination and saving. auto is a presentation prop, not evidence of a business feature flag or permission. The 400 ms timeout is a one-shot print delay, not recurring refresh or an integration job. This worker triggered no print or download.

Evidence: `S41 assets/356upgw1p449j.js bytes [8919, 9269)`.

### APP09 — Local persistence and refresh coverage limits

**Verified fact (static delivered-client code); bounded-static-coverage.** The retained app-specific navigation, DateRangePicker, PrintButton and CallSheetUpload functions contain no localStorage/sessionStorage, draft save/restore, recurring setInterval, role predicate or client integration request. DateRangePicker keeps current selections in React state; ThemeToggle writes a presentation cookie; PrintButton uses a one-shot timeout; CallSheetUpload uses React action state.

This is limited to retained client functions. It does not establish absent server jobs, absent application-wide autosave, absent scheduled integrations or no refresh elsewhere. CallSheetUpload exposes no explicit local-draft implementation; its server handler and any other component remain outside this analysis.

### APP10 — CallSheetUpload server-reference identity

**Verified fact (static delivered-client code); gentry-specific.** The newly retained 1t_el1w5uiobt.js module 4773 exports CallSheetUpload. It creates a server reference with the literal identity 603a2551faaf2a276b438c3b70de362ad8e990c011 and the symbol uploadCallSheet, using the framework callServer/findSourceMapURL helpers. The generic first-byte decoder (FW12) reads 0x60 as server-action, used argument positions 0 and 1, and no rest-arguments bit.

This is a public delivered-client action identity and symbol, not server-handler source or an authorization credential. Its name is not proof of row matching, duplicate detection, import limits, transactions or side effects. No action was invoked, file selected or production row imported. The association is scoped to these observed bytes; future builds may change the identity.

Evidence: `S42 assets/1t_el1w5uiobt.js bytes [537, 691)`.

### APP11 — Call importer state and response feedback

**Verified fact (static delivered-client code); gentry-specific.** CallSheetUpload calls useActionState on that reference with an empty initial object. Its returned action function is assigned to the form. The pending value disables the Import button and changes its label from Import calls to Importing. Truthy state.error renders as error text. Truthy state.result renders added, alreadyThere, noCallStatus and unmatched.length, with unmatched examples limited to the first 15 entries.

The client expects this result shape; no actual import response was observed. alreadyThere suggests server-reported duplicate handling but does not prove its key or algorithm. noCallStatus is feedback labeled rows without a call status skipped, not a client validation implementation. The list entries are returned strings; none were fetched or retained in this review. No explicit reset, success-triggered router.refresh or file-input disable appears in the component.

Evidence: `S43 assets/1t_el1w5uiobt.js bytes [710, 1373)`; `S44 assets/1t_el1w5uiobt.js bytes [1315, 1938)`.

### APP12 — Call importer file chooser and validation boundary

**Verified fact (static delivered-client code); gentry-specific.** The importer file input is named file and has accept=".csv,text/csv". Its component has no required attribute, size limit, explicit client CSV parser, content/schema checks or row validation. The form is bound to the server-action function; the surrounding shared framework handles action transport.

accept is a chooser hint rather than evidence of server validation. Importing safely and determining required columns, matching rules, duplicate keys and write consequences requires server source or a separately approved test. A component-level lack of role props does not prove the server action lacks permission enforcement. Local draft persistence is not exposed by this component.

Evidence: `S45 assets/1t_el1w5uiobt.js bytes [928, 1169)`.

## Shared framework findings

### FW01 — Turbopack bootstrap

**Verified fact (static delivered-client code); framework-generic.** The bootstrap registers delivered chunks and runtime module 94553. The chunk-loader base path defaults to /_next/.

A bundle manifest is not a backend inventory. Unseen chunks may carry page components. This worker fetched no chunk referenced only in code strings.

Evidence: `S05 assets/turbopack-3bohnvk-2ex_3.js bytes [112, 430)`; `S06 assets/turbopack-3bohnvk-2ex_3.js bytes [5454, 5633)`.

### FW02 — Delivered Next.js version declaration

**Verified fact (static delivered-client code); framework-generic.** The bootstrap assigns window.next={version:"16.3.5",appDir:!0}. This identifies the version declaration shipped in these bytes and App Router mode.

This is not package.json, a lockfile, backend source, or independent proof of every server dependency.

Evidence: `S07 assets/27t_qfc-3_lzs.js bytes [12063, 12103)`.

### FW03 — Delivered React version declarations

**Verified fact (static delivered-client code); framework-generic.** React and React DOM declare 19.3.0-canary-cbb046ab-20260731. React DOM also checks the React version against that literal.

These are delivered runtime declarations, not a recommendation for a replacement system.

Evidence: `S08 assets/19mx3mg6lkumu.js bytes [26442, 26485)`; `S09 assets/27t_qfc-3_lzs.js bytes [223881, 224013)`; `S10 assets/0ay527mnq1105.js bytes [7494, 7537)`.

### FW04 — Polyfill library

**Verified fact (static delivered-client code); framework-generic.** The polyfill chunk records core-js version 3.38.1 in global mode with license/source URLs.

Polyfill URLs and URL-parser test values are library content, not Gentry integrations or production endpoints.

Evidence: `S11 assets/0cz1d0mv5g_q7.js bytes [2828, 3100)`.

### FW05 — Flight transport headers

**Verified fact (static delivered-client code); framework-generic.** The framework declares rsc, next-action, next-router-state-tree, next-router-prefetch, next-router-segment-prefetch, next-hmr-refresh, next-url and text/x-component constants. It also declares _rsc, action-not-found and action-revalidated markers.

These define transport implementation available in this build. Actual authenticated requests and response values require separate browser/network observations.

Evidence: `S12 assets/2bub_m4veo3fm.js bytes [1713, 2242)`.

### FW06 — Initial Flight hydration

**Verified fact (static delivered-client code); framework-generic.** The bootstrap consumes self.__next_f into a ReadableStream. Tag 0 initializes a queue, 1 carries encoded text, 2 sets form state, and 3 decodes base64 binary bytes. It then calls createFromReadableStream, or createFromFetch for client-resume/test paths.

Protocol support exposes no domain status transition or per-user access rule. No Flight payload was inspected within this delegated input scope.

Evidence: `S13 assets/27t_qfc-3_lzs.js bytes [5945, 6709)`; `S14 assets/27t_qfc-3_lzs.js bytes [6664, 7057)`; `S15 assets/27t_qfc-3_lzs.js bytes [7635, 7810)`.

### FW07 — Flight navigation requests

**Verified fact (static delivered-client code); framework-generic.** Navigation fetch prepares RSC and router-state headers, optionally next-url, and requests with credentials:same-origin. Non-Flight, failed, bodyless or mismatched-build responses fall back to browser navigation.

The generic credentials option does not prove cookie names, expiry, session backend or which Gentry routes were requested.

Evidence: `S16 assets/2bub_m4veo3fm.js bytes [18328, 18901)`; `S17 assets/2bub_m4veo3fm.js bytes [20429, 20633)`.

### FW08 — Server-action dispatch

**Verified fact (static delivered-client code); framework-generic.** callServer returns a Promise and dispatches ACTION_SERVER_ACTION with actionId, actionArgs, resolve and reject inside startTransition.

Identity and arguments are supplied dynamically. This dispatcher names no Gentry business function.

Evidence: `S18 assets/0ay527mnq1105.js bytes [932, 1240)`.

### FW09 — Server references and bound arguments

**Verified fact (static delivered-client code); framework-generic.** The React client provides createServerReference, which wraps an identifier and callback. It resolves streamed references through id and bound fields, concatenating bound arguments before calling the server callback.

The initial nine assets expose the generic reference machinery. A later retained app-specific chunk supplies uploadCallSheet with a literal action ID (APP10). Rendered forms/Flight may carry other identities separately.

Evidence: `S19 assets/0ay527mnq1105.js bytes [25479, 25653)`; `S20 assets/0ay527mnq1105.js bytes [14519, 14924)`.

### FW10 — Server-action HTTP protocol

**Verified fact (static delivered-client code); framework-generic.** The reducer encodes action arguments with encodeReply, sends a POST to the current canonical URL, and places the dynamic ID in next-action. Accept is text/x-component, router state is encoded, and optional deployment/next-url fields are added.

This does not identify a Gentry-specific /api action route or establish server validation, authorization, side effects, idempotency or successful execution. No action was called.

Evidence: `S21 assets/2bub_m4veo3fm.js bytes [38117, 38966)`.

### FW11 — Server-action response handling

**Verified fact (static delivered-client code); framework-generic.** The reducer checks x-nextjs-action-not-found, parses x-action-redirect with push/replace, parses x-action-revalidated and decodes a Flight response. It rejects an unexpected non-Flight response when no redirect was supplied.

These generic outcomes cannot establish operation-specific Gentry success, retry or audit rules.

Evidence: `S22 assets/2bub_m4veo3fm.js bytes [38651, 39215)`; `S23 assets/2bub_m4veo3fm.js bytes [39188, 39776)`.

### FW12 — Server-reference identifier format

**Verified fact (static delivered-client code); framework-generic.** The helper expects length 42. The first hex byte encodes use-cache versus server-action, six used-argument bits and a rest-arguments bit. omitUnusedArgs builds the outgoing argument list.

One literal 42-character hexadecimal identity appears in the 13 retained assets: uploadCallSheet (APP10). The format decoder does not establish handler semantics or access policy.

Evidence: `S24 assets/2bub_m4veo3fm.js bytes [134133, 134529)`.

### FW13 — Router refresh implementation

**Verified fact (static delivered-client code); framework-generic.** Public app-router refresh dispatches ACTION_REFRESH inside startTransition. The queue may request refresh after a discarded server action revalidated data. Generic error retry also calls context refresh before resetting error state.

No recurring Gentry data-refresh cadence is established by the 13 retained assets. PrintButton has a one-shot print timeout (APP08). Route refresh and server-side integration synchronization remain different questions; server jobs are not ruled out.

Evidence: `S25 assets/2bub_m4veo3fm.js bytes [6427, 6573)`; `S26 assets/2bub_m4veo3fm.js bytes [3327, 3475)`; `S27 assets/19mx3mg6lkumu.js bytes [773, 909)`.

### FW14 — HTTP fallback display does not establish RBAC

**Verified fact (static delivered-client code); framework-generic.** HTTPAccessFallbackBoundary displays supplied notFound/forbidden/unauthorized components when corresponding framework error statuses are thrown. React role matches concern ARIA/DOM attributes.

Fallback display does not prove a Gentry authorization check or role matrix. No app-specific role predicate was identified in retained component functions; upstream prop selection and server authorization remain unknown.

Evidence: `S28 assets/3fntmmi971322.js bytes [3115, 3821)`; `S29 assets/27t_qfc-3_lzs.js bytes [12865, 12911)`; `S30 assets/27t_qfc-3_lzs.js bytes [185470, 185504)`.

### FW15 — Domain-like strings with unrelated framework meaning

**Verified fact (static delivered-client code); framework-generic.** WhatsApp appears in a bot-user-agent regex. cleanup names an LRU/cache export and call. Neither is Gentry WhatsApp integration or order-cleanup workflow evidence.

Meta matches concern metadata/polyfills; users is an icon key. Explicit Shopify/Bosta/Whapi connector configuration or request code was not identified in retained assets; server integrations remain outside this evidence.

Evidence: `S31 assets/2bub_m4veo3fm.js bytes [127917, 128118)`; `S32 assets/2bub_m4veo3fm.js bytes [73275, 73450)`.

## HTTP discrepancy and unresolved coverage

### GAP01 — Server behavior outside retained client coverage

**Hypothesis / unresolved question; unresolved.** The 13 retained assets confirm navigation, date selection, browser printing, CallSheetUpload client state/identity and shared framework transport. They do not establish server import rules, role enforcement, integration jobs or recurring refresh cadence.

The earlier referenced CallSheetUpload chunk returned 404; a freshly observed exact chunk later returned 200. The discrepancy cause is unresolved. More rendered-form/Flight or server evidence may close gaps. String discovery never access-verifies a route.

### HTTP01 — Time-scoped referenced CallSheetUpload asset discrepancy

**Verified fact (recorded HTTP responses); Flight associations supplied by parent investigation; public-http.** The ledger records exact 1kudf3dkhdpbd.js GET at 2026-10-13T16:58:51.804164+00:00 with 404, text/plain content type, a 9-byte response and body_retained=false. The parent investigation reports this was a Calls Flight reference for module 4773 CallSheetUpload. A fresh Calls navigation later reported module 4773 in 1t_el1w5uiobt.js; its exact GET at 2026-10-13T17:00:35.974352+00:00 returned 200 and the code was retained/analyzed.

The corrected HTTP ledger classifies the earlier 404 response as error body; discarded. It remains a failed asset attempt, with no response body retained. Its cause remains unresolved. No deployment, stale cache or transient failure explanation is established. Calls navigation/Flight association is supplied parent context; this worker inspected only the saved JS and ledger. No guessed alternative was fetched.

Evidence: `H01 public-http-observations.json bytes [7015, 7673)` (JSON pointer `/11`); `H02 public-http-observations.json bytes [8996, 9650)` (JSON pointer `/14`).

## Routes, permissions, flags and integrations

Both Gentry navigation variants render supplied items. Their only literal application destination is the logo `/`; their client functions contain no role/permission prop or item filter. Upstream item selection and server authorization remain unknown here. The check icon and PrintButton auto prop are display options, not business feature-flag evidence. Framework routes, cache paths, documentation URLs, parser test URLs and ARIA roles do not form a Gentry route/permission inventory. No discovered route was access-tested.

DateRangePicker submits its enclosing form without declaring method/action; GET semantics require separate rendered-form evidence. Date bounds are supplied props and native input attributes, not proof of server validation, week arithmetic or timezone rules. PrintButton uses browser print and a conditional 400 ms delay; it does not refresh data or identify a server PDF service. The retained components expose no local draft save/restore.

CallSheetUpload identifies the public server-action reference `603a2551faaf2a276b438c3b70de362ad8e990c011` as `uploadCallSheet`, accepts a CSV file chooser and renders action-state feedback. It does not parse rows in the client, enforce schema/size limits or expose server deduplication, matching, transaction or permission logic. Response field labels are expected feedback, not successful-import observations. No import was attempted.

The 13 retained assets contain one literal 42-hex action identity, no setInterval token, no sourceMappingURL declaration and no explicit Shopify/Bosta/Whapi connector name. These bounded checks do not rule out server jobs, unseen components, integrations or authorization. Generic action transport posts a supplied ID to the current canonical URL. Rendered identities should be correlated with their observed form/Flight; client wrappers alone do not establish backend effects.

## Confidence and remaining gaps

Confidence is high for exact component code, version literals, protocol implementation and recorded response/hash facts. Business behavior remains limited to client intent for navigation, dates, printing and importer feedback. Server actions, role enforcement, integration jobs, scheduled refresh, route access and local persistence outside these functions remain unresolved. Calls Flight associations are supplied by the parent investigation; this worker inspected saved JS and the HTTP ledger only.

## Exact bounded evidence snippets

### S01 — `assets/15qydxckj0uxx.js` bytes [8983, 9185)

```javascript
function a(e,t){let r=null;for(let{href:n}of t)(e===n||"/"!==n&&e.startsWith(`${n}/`))&&(!r||n.length>r.length)&&(r=n);return r}let i={home:"M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1
```

### S02 — `assets/15qydxckj0uxx.js` bytes [10197, 11492)

```javascript
e.s(["Icon",0,u,"Logo",0,function(){return(0,t.jsxs)(r.default,{href:"/",className:"flex items-center gap-2.5",children:[(0,t.jsx)("span",{className:"flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-brand-light to-olive text-sm font-bold text-ink",children:"G"}),(0,t.jsx)("span",{className:"text-[15px] font-semibold tracking-tight",children:"Gentry Ops"})]})},"SideNav",0,function({items:e,direction:o="column"}){let i=a((0,n.usePathname)(),e);return(0,t.jsx)("nav",{className:"column"===o?"flex flex-col gap-1":"flex gap-1 overflow-x-auto [scrollbar-width:none] [&::-webkit-scrollbar]:hidden",children:e.map(e=>{let n=e.href===i;return(0,t.jsxs)(r.default,{href:e.href,className:`flex shrink-0 items-center gap-3 rounded-lg px-3 py-2 text-sm transition-colors ${n?"bg-brand/15 font-medium text-accent":"text-fg/60 hover:bg-fg/5 hover:text-fg"}`,children:[e.icon&&(0,t.jsx)(u,{name:e.icon,className:n?"text-brand":"text-fg/40"}),(0,t.jsx)("span",{className:"whitespace-nowrap",children:e.label})]},e.href)})})},"TabNav",0,function({items:e}){let i=a((0,n.usePathname)(),e),u=(0,o.useRef)(null);return(0,o.useEffect)(()=>{u.current?.querySelector("[aria-current=page]")?.scrollIntoView({block:"nearest",inline:"center"})},[i]),(0,t.jsx)("nav",{ref:u,className:"flex ga
```

### S03 — `assets/15qydxckj0uxx.js` bytes [11236, 11836)

```javascript
"TabNav",0,function({items:e}){let i=a((0,n.usePathname)(),e),u=(0,o.useRef)(null);return(0,o.useEffect)(()=>{u.current?.querySelector("[aria-current=page]")?.scrollIntoView({block:"nearest",inline:"center"})},[i]),(0,t.jsx)("nav",{ref:u,className:"flex gap-1 overflow-x-auto rounded-xl border border-line bg-surface p-1 text-sm [scrollbar-width:none] [&::-webkit-scrollbar]:hidden",children:e.map(e=>(0,t.jsx)(r.default,{href:e.href,"aria-current":e.href===i?"page":void 0,className:`shrink-0 whitespace-nowrap rounded-lg px-3 py-1.5 transition-colors ${e.href===i?"bg-brand/15 font-medium text-acce
```

### S04 — `assets/15qydxckj0uxx.js` bytes [11969, 12653)

```javascript
e.s(["ThemeToggle",0,function({initialDark:e,className:n=""}){let[o,a]=(0,r.useState)(e);return(0,t.jsx)("button",{type:"button",onClick:function(){let e=!o;document.documentElement.classList.toggle("dark",e),document.cookie=`theme=${e?"dark":"light"}; path=/; max-age=31536000; samesite=lax`,a(e)},title:o?"Switch to light mode":"Switch to dark mode","aria-label":o?"Switch to light mode":"Switch to dark mode",className:`flex h-8 w-8 items-center justify-center rounded-lg text-fg/60 transition-colors hover:bg-fg/5 hover:text-fg ${n}`,children:(0,t.jsx)("svg",{viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:1.8,strokeLinecap:"round",strokeLinejoin:"round",class
```

### S05 — `assets/turbopack-3bohnvk-2ex_3.js` bytes [112, 430)

```javascript
{otherChunks:["static/chunks/310vm2bl3xxpt.js","static/chunks/19mx3mg6lkumu.js","static/chunks/2bub_m4veo3fm.js","static/chunks/27t_qfc-3_lzs.js","static/chunks/0ay527mnq1105.js"],runtimeModuleIds:[94553]}]),(()=>{let e;if(!Array.isArray(globalThis.TURBOPACK))return;var t,r=function(){if(null!=self.TURBOPACK_ASSET_SU
```

### S06 — `assets/turbopack-3bohnvk-2ex_3.js` bytes [5454, 5633)

```javascript
U="string"==typeof TURBOPACK_CHUNK_BASE_PATH?TURBOPACK_CHUNK_BASE_PATH:"/_next/",P=new Map;l.M=P;let $=new Map,A=new Map,T=new Map;async function E(e,t,r){let n;if("string"==typeo
```

### S07 — `assets/27t_qfc-3_lzs.js` bytes [12063, 12103)

```javascript
window.next={version:"16.3.5",appDir:!0}
```

### S08 — `assets/19mx3mg6lkumu.js` bytes [26442, 26485)

```javascript
r.version="19.3.0-canary-cbb046ab-20260731"
```

### S09 — `assets/27t_qfc-3_lzs.js` bytes [223881, 224013)

```javascript
if("19.3.0-canary-cbb046ab-20260731"!==f9)throw Error(u(527,f9,"19.3.0-canary-cbb046ab-20260731"));if(K.findDOMNode=function(e){var 
```

### S10 — `assets/0ay527mnq1105.js` bytes [7494, 7537)

```javascript
t.version="19.3.0-canary-cbb046ab-20260731"
```

### S11 — `assets/0cz1d0mv5g_q7.js` bytes [2828, 3100)

```javascript
push({version:"3.38.1",mode:"global",copyright:"© 2014-2024 Denis Pushkarev (zloirock.ru)",license:"https://github.com/zloirock/core-js/blob/v3.38.1/LICENSE",source:"https://github.com/zloirock/core-js"})}),nt=function(t,e){return rt[t]||(rt[t]=e||{})},ot=Object,it=funct
```

### S12 — `assets/2bub_m4veo3fm.js` bytes [1713, 2242)

```javascript
let l="rsc",u="next-action",i="next-router-state-tree",o="next-router-prefetch",c="next-router-segment-prefetch",s="next-hmr-refresh",f="next-url",d="text/x-component",h="next-instant-navigation-testing",p=[l,i,o,s,c],y="_rsc",g="x-nextjs-stale-time",_="x-nextjs-postponed",E="x-nextjs-rewritten-path",R="x-nextjs-rewritten-query",P="x-nextjs-prerender",S="x-nextjs-action-not-found",m="x-nextjs-request-id",v="x-nextjs-html-request-id",T="x-action-revalidated";("function"==typeof r.default||"object"==typeof r.default&&null!==r
```

### S13 — `assets/27t_qfc-3_lzs.js` bytes [5945, 6709)

```javascript
function L(e){if(0===e[0])a=[];else if(1===e[0]){if(!a)throw Object.defineProperty(Error("Unexpected server data: missing bootstrap script."),"__NEXT_ERROR_CODE",{value:"E18",enumerable:!1,configurable:!0});o?o.enqueue(C.encode(e[1])):a.push(e[1])}else if(2===e[0])z=e[1];else if(3===e[0]){if(!a)throw Object.defineProperty(Error("Unexpected server data: missing bootstrap script."),"__NEXT_ERROR_CODE",{value:"E18",enumerable:!1,configurable:!0});let n=atob(e[1]),r=new Uint8Array(n.length);for(var t=0;t<n.length;t++)r[t]=n.charCodeAt(t);o?o.enqueue(r):a.push(r)}}let R=function(){o&&!O&&(o.close(),O=!0,a=void 0),T=!0};"loading"===document.readyState?document.addEventListener("DOMContentLoaded",R,!1):setTimeout(R);let M=self.__next_f=self.__next_f||[];M.forEa
```

### S14 — `assets/27t_qfc-3_lzs.js` bytes [6664, 7057)

```javascript
let M=self.__next_f=self.__next_f||[];M.forEach(L),M.length=0,M.push=L;let I=new ReadableStream({start(e){a&&(a.forEach(t=>{e.enqueue("string"==typeof t?C.encode(t):t)}),T&&!O)&&(null===e.desiredSize||e.desiredSize<0?N||e.error(Object.defineProperty(Error("The connection to the page was unexpectedly closed, possibly due to the stop button being clicked, loss of Wi-Fi, or an unstable interne
```

### S15 — `assets/27t_qfc-3_lzs.js` bytes [7635, 7810)

```javascript
else l=_(I,{callServer:h.callServer,findSourceMapURL:g.findSourceMapURL,debugChannel:r,startTime:0});function D({initialRSCPayload:e,actionQueue:t,webSocket:n,staticIndicatorS
```

### S16 — `assets/2bub_m4veo3fm.js` bytes [18328, 18901)

```javascript
async function v(e,t){let{flightRouterState:r,nextUrl:n}=t,a={[o.RSC_HEADER]:"1",[o.NEXT_ROUTER_STATE_TREE_HEADER]:(0,f.prepareFlightRouterStateForRequest)(r,t.isHmrRefresh)};n&&(a[o.NEXT_URL]=n);try{let r=await N(e,a,"auto",!0,t.signal),n=(0,h.urlToUrlWithoutFlightMarker)(new URL(r.url)),l=r.redirected?n:e,u=r.headers.get("content-type")||"",i=!!r.headers.get("vary")?.includes(o.NEXT_URL),c=!!r.headers.get(o.NEXT_DID_POSTPONE_HEADER);if(!u.startsWith(o.RSC_CONTENT_TYPE_HEADER)||!r.ok||!r.body)return e.hash&&(n.hash=e.hash),S(n.toString());let s=r.flightResponsePromi
```

### S17 — `assets/2bub_m4veo3fm.js` bytes [20429, 20633)

```javascript
let u={credentials:"same-origin",headers:t,priority:r||void 0,signal:a},c=new URL(e);await (0,d.setCacheBustingSearchParam)(c,t);let s=(0,i.fetch)(c,u).then(T),f=s.then(({response:e})=>e),h=n?I(f,t):null,
```

### S18 — `assets/0ay527mnq1105.js` bytes [932, 1240)

```javascript
async function l(e,n){return new Promise((t,l)=>{(0,r.startTransition)(()=>{(0,u.dispatchAppRouterAction)({type:o.ACTION_SERVER_ACTION,actionId:e,actionArgs:n,resolve:t,reject:l})})})}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineP
```

### S19 — `assets/0ay527mnq1105.js` bytes [25479, 25653)

```javascript
t.createServerReference=function(e,n){function t(){var t=Array.prototype.slice.call(arguments);return n(e,t)}return O(t,e,null),t},t.createTemporaryReferenceSet=function(){re
```

### S20 — `assets/0ay527mnq1105.js` bytes [14519, 14924)

```javascript
function G(e,n,t,r){if(!e._serverReferenceConfig)return function(e,n){function t(){var e=Array.prototype.slice.call(arguments);return o?"fulfilled"===o.status?n(r,o.value.concat(e)):Promise.resolve(o).then(function(t){return n(r,t.concat(e))}):n(r,e)}var r=e.id,o=e.bound;return O(t,r,o),t}(n,e._callServer);var u=function(e,n){var t="",r=e[n];if(r)t=r.name;else{var u=n.lastIndexOf("#");if(-1!==u&&(t=n.s
```

### S21 — `assets/2bub_m4veo3fm.js` bytes [38117, 38966)

```javascript
async function F(e,t,r){let s,d,h,y,g,{actionId:_,actionArgs:R}=r,P=(0,c.createTemporaryReferenceSet)(),T=(0,E.extractInfoFromServerReferenceId)(_),b=(0,E.omitUnusedArgs)(R,T),C=await (0,c.encodeReply)(b,{temporaryReferences:P}),A={Accept:u.RSC_CONTENT_TYPE_HEADER,[u.ACTION_HEADER]:_,[u.NEXT_ROUTER_STATE_TREE_HEADER]:(0,p.prepareFlightRouterStateForRequest)(e.tree)},M=(0,S.getDeploymentId)();M&&(A["x-deployment-id"]=M),t&&(A[u.NEXT_URL]=t);try{s=await (0,o.fetch)(e.canonicalUrl,{method:"POST",headers:A,body:C})}catch(e){throw e}if("1"===s.headers.get(u.NEXT_ACTION_NOT_FOUND_HEADER))throw Object.defineProperty(new i.UnrecognizedActionError(`Server Action "${_}" was not found on the server. 
Read more: https://nextjs.org/docs/messages/failed-to-find-server-action`),"__NEXT_ERROR_CODE",{value:"E715",enumerable:!1,configurable:!0});let F=s.h
```

### S22 — `assets/2bub_m4veo3fm.js` bytes [38651, 39215)

```javascript
if("1"===s.headers.get(u.NEXT_ACTION_NOT_FOUND_HEADER))throw Object.defineProperty(new i.UnrecognizedActionError(`Server Action "${_}" was not found on the server. 
Read more: https://nextjs.org/docs/messages/failed-to-find-server-action`),"__NEXT_ERROR_CODE",{value:"E715",enumerable:!1,configurable:!0});let F=s.headers.get("x-action-redirect"),[w,j]=F?.split(";")||[];switch(j){case"push":d="push";break;case"replace":d="replace";break;default:d=void 0}let D=!!s.headers.get(u.NEXT_IS_PRERENDER_HEADER),U=O.ActionDidNotRevalidate;try{let e=s.headers.get("x-acti
```

### S23 — `assets/2bub_m4veo3fm.js` bytes [39188, 39776)

```javascript
let e=s.headers.get("x-action-revalidated");if(e){let t=JSON.parse(e);(t===O.ActionDidRevalidateStaticAndDynamic||t===O.ActionDidRevalidateDynamicOnly)&&(U=t)}}catch{}let L=w?(0,f.assignLocation)(w,new URL(e.canonicalUrl,window.location.href)):void 0,H=s.headers.get("content-type"),x=!!(H&&H.startsWith(u.RSC_CONTENT_TYPE_HEADER));if(!x&&!L)throw Object.defineProperty(Error(s.status>=400&&"text/plain"===H?await s.text():"An unexpected response was received from the server."),"__NEXT_ERROR_CODE",{value:"E394",enumerable:!1,configurable:!0});let k=!1;if(x){let e=L?(0,N.processFetch)(s
```

### S24 — `assets/2bub_m4veo3fm.js` bytes [134133, 134529)

```javascript
let l=42;function u(e){return e.length===l}function i(e){let t=parseInt(e.slice(0,2),16),r=t>>1&63,n=Array(6);for(let e=0;e<6;e++){let t=r>>5-e&1;n[e]=1===t}return{type:1==(t>>7&1)?"use-cache":"server-action",usedArgs:n,hasRestArgs:1==(1&t)}}function o(e,t){let r=Array(e.length),n=0;for(let a=0;a<e.length;a++)(a<6&&t.usedArgs[a]||a>=6&&t.hasRestArgs)&&(r[a]=e[a],n=a+1);return r.length=n,r}}]);
```

### S25 — `assets/2bub_m4veo3fm.js` bytes [6427, 6573)

```javascript
refresh:()=>{(0,i.startTransition)(()=>{(0,f.dispatchAppRouterAction)({type:l.ACTION_REFRESH})})},hmrRefresh:()=>{throw Object.defineProperty(Erro
```

### S26 — `assets/2bub_m4veo3fm.js` bytes [3327, 3475)

```javascript
t.payload.type===l.ACTION_SERVER_ACTION&&t.payload.didRevalidate&&(e.needsRefresh=!0),_(e,t,r);return}e.state=n,_(e,t,r),t.resolve(n)}(0,o.isThenabl
```

### S27 — `assets/19mx3mg6lkumu.js` bytes [773, 909)

```javascript
this.retry=()=>{(0,i.startTransition)(()=>{this.context?.refresh(),this.reset()})},this.state={error:null,previousPathname:this.props.pa
```

### S28 — `assets/3fntmmi971322.js` bytes [3115, 3821)

```javascript
render(){let{notFound:e,forbidden:t,unauthorized:r,children:n}=this.props,{triggeredStatus:u}=this.state,a={[o.HTTPAccessErrorStatus.NOT_FOUND]:e,[o.HTTPAccessErrorStatus.FORBIDDEN]:t,[o.HTTPAccessErrorStatus.UNAUTHORIZED]:r};if(u){let d=u===o.HTTPAccessErrorStatus.NOT_FOUND&&e,s=u===o.HTTPAccessErrorStatus.FORBIDDEN&&t,i=u===o.HTTPAccessErrorStatus.UNAUTHORIZED&&r;return d||s||i?(0,l.jsxs)(l.Fragment,{children:[(0,l.jsx)("meta",{name:"robots",content:"noindex"}),!1,a[u]]}):n}return n}}function i({notFound:e,forbidden:t,unauthorized:r,children:n}){let o=(0,a.useUntrackedPathname)(),c=(0,u.useContext)(d.MissingSlotContext);return e||t||r?(0,l.jsx)(s,{pathname:o,notFound:e,forbidden:t,unauthorized:r
```

### S29 — `assets/27t_qfc-3_lzs.js` bytes [12865, 12911)

```javascript
t.id="__next-route-announcer__",t.role="alert"
```

### S30 — `assets/27t_qfc-3_lzs.js` bytes [185470, 185504)

```javascript
case"dir":case"role":case"viewBox"
```

### S31 — `assets/2bub_m4veo3fm.js` bytes [127917, 128118)

```javascript
a_archiver|Bingbot|BingPreview|applebot|facebookexternalhit|facebookcatalog|Twitterbot|LinkedInBot|Slackbot|Discordbot|WhatsApp|SkypeUriPreview|Yeti|googleweblight/i},82604,(e,t,r)=>{"use strict";Objec
```

### S32 — `assets/2bub_m4veo3fm.js` bytes [73275, 73450)

```javascript
var n={cleanup:function(){return h},deleteFromLru:function(){return f},lruPut:function(){return c},updateLruSize:function(){return s}};for(var a in n)Object.defineProperty(r,a
```

### S33 — `assets/1986ffcy11vyr.js` bytes [9226, 9344)

```javascript
check:"M9 11l3 3 8-8M20 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11",target:"M12 21a9 9 0 1 0 0-18 9 9 0 0 0
```

### S34 — `assets/1986ffcy11vyr.js` bytes [10664, 12111)

```javascript
"SideNav",0,function({items:e,direction:o="column"}){let i=a((0,n.usePathname)(),e);return(0,t.jsx)("nav",{className:"column"===o?"flex flex-col gap-1":"flex gap-1 overflow-x-auto [scrollbar-width:none] [&::-webkit-scrollbar]:hidden",children:e.map(e=>{let n=e.href===i;return(0,t.jsxs)(r.default,{href:e.href,className:`flex shrink-0 items-center gap-3 rounded-lg px-3 py-2 text-sm transition-colors ${n?"bg-brand/15 font-medium text-accent":"text-fg/60 hover:bg-fg/5 hover:text-fg"}`,children:[e.icon&&(0,t.jsx)(l,{name:e.icon,className:n?"text-brand":"text-fg/40"}),(0,t.jsx)("span",{className:"whitespace-nowrap",children:e.label})]},e.href)})})},"TabNav",0,function({items:e}){let i=a((0,n.usePathname)(),e),l=(0,o.useRef)(null);return(0,o.useEffect)(()=>{l.current?.querySelector("[aria-current=page]")?.scrollIntoView({block:"nearest",inline:"center"})},[i]),(0,t.jsx)("nav",{ref:l,className:"flex gap-1 overflow-x-auto rounded-xl border border-line bg-surface p-1 text-sm [scrollbar-width:none] [&::-webkit-scrollbar]:hidden",children:e.map(e=>(0,t.jsx)(r.default,{href:e.href,"aria-current":e.href===i?"page":void 0,className:`shrink-0 whitespace-nowrap rounded-lg px-3 py-1.5 transition-colors ${e.href===i?"bg-brand/15 font-medium text-accent":"text-fg/55 hover:bg-fg/5 hover:text-fg"}`,children:e.label},e.href))})}])},94013,e=>{"use strict";var t=e.i(43476),r=e.i(71645);e.s(["ThemeToggle",0,function({initialDark:e,className:n=""}){l
```

### S35 — `assets/1986ffcy11vyr.js` bytes [12048, 12481)

```javascript
e.s(["ThemeToggle",0,function({initialDark:e,className:n=""}){let[o,a]=(0,r.useState)(e);return(0,t.jsx)("button",{type:"button",onClick:function(){let e=!o;document.documentElement.classList.toggle("dark",e),document.cookie=`theme=${e?"dark":"light"}; path=/; max-age=31536000; samesite=lax`,a(e)},title:o?"Switch to light mode":"Switch to dark mode","aria-label":o?"Switch to light mode":"Switch to dark mode",className:`flex h-8 w
```

### S36 — `assets/14x5k9f0fswg1.js` bytes [165, 623)

```javascript
e.s(["DateRangePicker",0,function({period:e,from:s,to:a,today:n,min:r,presets:o,weeks:i,note:c}){let x=(0,l.useRef)(null),[d,u]=(0,l.useState)(e),[m,f]=(0,l.useState)(a),p=e=>{u(e);let t=x.current,l=t?.closest("form");t&&l&&(t.querySelector('input[name="period"]').value=e,t.querySelectorAll('input[type="date"]').forEach(e=>e.disabled=!0),l.requestSubmit())},g="w-full min-w-0 rounded-lg border border-line bg-surface-2 px-3 py-2 text-sm text-foreground tra
```

### S37 — `assets/14x5k9f0fswg1.js` bytes [1151, 1816)

```javascript
type:"date",name:"from",defaultValue:s,min:r,max:n,onChange:()=>u("custom"),className:g})]}),(0,t.jsxs)("label",{className:"flex min-w-0 flex-col gap-1.5 text-sm",children:[(0,t.jsxs)("span",{className:"flex items-center justify-between gap-2 text-xs font-medium text-fg/55",children:["To",m!==n&&(0,t.jsx)("button",{type:"button",onClick:()=>{f(n),u("custom")},className:"text-[11px] font-normal text-accent hover:underline",children:"till today"})]}),(0,t.jsx)("input",{type:"date",name:"to",value:m,min:r,max:n,onChange:e=>{f(e.target.value),u("custom")},className:g})]}),(0,t.jsxs)("label",{className:"col-span-2 flex min-w-0 flex-col gap-1.5 text-sm",children:
```

### S38 — `assets/14x5k9f0fswg1.js` bytes [1482, 1857)

```javascript
onClick:()=>{f(n),u("custom")},className:"text-[11px] font-normal text-accent hover:underline",children:"till today"})]}),(0,t.jsx)("input",{type:"date",name:"to",value:m,min:r,max:n,onChange:e=>{f(e.target.value),u("custom")},className:g})]}),(0,t.jsxs)("label",{className:"col-span-2 flex min-w-0 flex-col gap-1.5 text-sm",children:[(0,t.jsx)("span",{className:"text-xs fon
```

### S39 — `assets/14x5k9f0fswg1.js` bytes [713, 737)

```javascript
b=d.startsWith("w")?d:""
```

### S40 — `assets/14x5k9f0fswg1.js` bytes [1919, 2624)

```javascript
"select",{value:b,onChange:e=>e.target.value&&p(e.target.value),className:g,children:[(0,t.jsx)("option",{value:"",children:"Pick a week…"}),i.map(e=>(0,t.jsx)("option",{value:e.key,children:e.label},e.key))]})]})]}),(0,t.jsx)("div",{className:"flex flex-wrap gap-1.5",children:o.map(e=>{let l;return(0,t.jsx)("button",{type:"button",onClick:()=>p(e.key),className:(l=d===e.key||"last-week"===e.key&&""===d,`rounded-full border px-3 py-1 text-xs transition-colors ${l?"border-brand/60 bg-brand/15 font-medium text-accent":"border-line bg-surface-2 text-fg/70 hover:border-brand/40 hover:text-fg"}`),children:e.label},e.key)})}),c&&(0,t.jsx)("p",{className:"text-[11px] text-fg/45",children:c})]})}])}]);
```

### S41 — `assets/356upgw1p449j.js` bytes [8919, 9269)

```javascript
e.s(["PrintButton",0,function({auto:e=!1}){return(0,r.useEffect)(()=>{if(!e)return;let t=setTimeout(()=>window.print(),400);return()=>clearTimeout(t)},[e]),(0,t.jsx)("button",{type:"button",onClick:()=>window.print(),className:"rounded-lg bg-[#8eb897] px-4 py-2 text-sm font-semibold text-[#040403] hover:bg-[#9ddbad]",children:"Save as PDF"})}])}]);
```

### S42 — `assets/1t_el1w5uiobt.js` bytes [537, 691)

```javascript
let a=(0,l.createServerReference)("603a2551faaf2a276b438c3b70de362ad8e990c011",l.callServer,void 0,l.findSourceMapURL,"uploadCallSheet");e.s(["CallSheetUp
```

### S43 — `assets/1t_el1w5uiobt.js` bytes [710, 1373)

```javascript
let[e,l,c]=(0,r.useActionState)(a,{}),s=e.result;return(0,t.jsxs)("form",{action:l,className:"flex flex-col gap-2",children:[(0,t.jsxs)("div",{className:"flex flex-wrap items-center gap-3",children:[(0,t.jsx)("input",{type:"file",name:"file",accept:".csv,text/csv",className:"text-sm file:mr-3 file:rounded-lg file:border-0 file:bg-surface-2 file:px-3 file:py-1.5 file:text-sm file:text-fg/80"}),(0,t.jsx)("button",{disabled:c,className:"rounded-lg bg-brand px-4 py-2 text-sm font-semibold text-ink transition-colors hover:bg-brand-light disabled:opacity-50",children:c?"Importing…":"Import calls"})]}),e.error&&(0,t.jsx)("p",{className:"text-sm text-red-600 da
```

### S44 — `assets/1t_el1w5uiobt.js` bytes [1315, 1938)

```javascript
e.error&&(0,t.jsx)("p",{className:"text-sm text-red-600 dark:text-red-400",children:e.error}),s&&(0,t.jsxs)("div",{className:"text-sm text-fg/75",children:[(0,t.jsxs)("p",{children:[s.added," call",1===s.added?"":"s"," added · ",s.alreadyThere," already in the app · ",s.noCallStatus," row",1===s.noCallStatus?"":"s"," without a call status skipped",s.unmatched.length>0&&` \xb7 ${s.unmatched.length} couldn't be matched to an order`,"."]}),s.unmatched.length>0&&(0,t.jsx)("ul",{className:"mt-1 list-disc pl-5 text-xs text-fg/50",children:s.unmatched.slice(0,15).map(e=>(0,t.jsx)("li",{children:e},e))})]})]})}],4773)}]);
```

### S45 — `assets/1t_el1w5uiobt.js` bytes [928, 1169)

```javascript
type:"file",name:"file",accept:".csv,text/csv",className:"text-sm file:mr-3 file:rounded-lg file:border-0 file:bg-surface-2 file:px-3 file:py-1.5 file:text-sm file:text-fg/80"}),(0,t.jsx)("button",{disabled:c,className:"rounded-lg bg-brand p
```

### H01 — `public-http-observations.json` bytes [7015, 7673); JSON pointer `/11`

```json
{
    "observed_at_utc": "2026-10-13T16:58:51.804164+00:00",
    "observation_type": "independent unauthenticated HTTP GET of observed asset",
    "path": "/_next/static/chunks/1kudf3dkhdpbd.js",
    "method": "GET",
    "query_parameter_names": [],
    "status": 404,
    "content_type": "text/plain; charset=utf-8",
    "cache_control": "private, no-cache, no-store, max-age=0, must-revalidate",
    "body_bytes": 9,
    "sha256": "0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5",
    "payload": "none",
    "response_shape": "error body; discarded",
    "credential_pattern_detected": false,
    "body_retained": false
  }
```

### H02 — `public-http-observations.json` bytes [8996, 9650); JSON pointer `/14`

```json
{
    "observed_at_utc": "2026-10-13T17:00:35.974352+00:00",
    "observation_type": "independent unauthenticated HTTP GET of observed asset",
    "path": "/_next/static/chunks/1t_el1w5uiobt.js",
    "method": "GET",
    "query_parameter_names": [],
    "status": 200,
    "content_type": "application/javascript; charset=UTF-8",
    "cache_control": "public, max-age=31536000, immutable",
    "body_bytes": 1938,
    "sha256": "8772c75206b9db716cfdd19be56a78a9b0628f655fb054ee4f3f86e434a2f8fd",
    "payload": "none",
    "response_shape": "JavaScript source bytes",
    "credential_pattern_detected": false,
    "body_retained": true
  }
```
