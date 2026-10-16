"""Retrieve exact observed public JS URLs without cookies or credentials.

This is an independent HTTP observation, not an authenticated browser trace.
"""
from pathlib import Path
import urllib.request
import urllib.error
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
ORIGIN = 'https://gentry-ops-production.up.railway.app'
CHUNKS = ['19mx3mg6lkumu.js', '2bub_m4veo3fm.js', '27t_qfc-3_lzs.js',
          '0ay527mnq1105.js', 'turbopack-3bohnvk-2ex_3.js', '3fntmmi971322.js',
          '15qydxckj0uxx.js', '0cz1d0mv5g_q7.js', '310vm2bl3xxpt.js',
          '1986ffcy11vyr.js', '1kudf3dkhdpbd.js', '14x5k9f0fswg1.js',
          '356upgw1p449j.js', '1t_el1w5uiobt.js']

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener = urllib.request.build_opener(NoRedirect())
asset_dir = ROOT / 'assets'
asset_dir.mkdir(exist_ok=True)
previous = ROOT / 'public-http-observations.json'
records = json.loads(previous.read_text(encoding='utf-8')) if previous.exists() else []
seen = {record['path'] for record in records}

for name in CHUNKS:
    path = '/_next/static/chunks/' + name
    if path in seen:
        continue
    request = urllib.request.Request(ORIGIN + path, method='GET')
    try:
        response = opener.open(request, timeout=25)
    except urllib.error.HTTPError as error:
        response = error
    body = response.read()
    text = body.decode('utf-8', errors='replace')
    secret_pattern = r'(?:sk-(?:proj-)?[A-Za-z0-9_-]{24,}|AKIA[A-Z0-9]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)'
    credential_flag = bool(re.search(secret_pattern, text))
    record = {'observed_at_utc': datetime.now(timezone.utc).isoformat(),
              'observation_type': 'independent unauthenticated HTTP GET of observed asset',
              'path': path, 'method': 'GET', 'query_parameter_names': [],
              'status': response.status, 'content_type': response.headers.get('Content-Type'),
              'cache_control': response.headers.get('Cache-Control'),
              'body_bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest(),
              'payload': 'none', 'response_shape': 'JavaScript source bytes' if response.status == 200 else 'error body; discarded',
              'credential_pattern_detected': credential_flag,
              'body_retained': response.status == 200 and not credential_flag}
    if record['body_retained']:
        (asset_dir / name).write_bytes(body)
    records.append(record)
    previous.write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(record))

# A single known protected route, without copying the browser session.
if '/orders' not in seen:
    request = urllib.request.Request(ORIGIN + '/orders', method='GET')
    try:
        response = opener.open(request, timeout=25)
    except urllib.error.HTTPError as error:
        response = error
    # Deliberately do not retain cookies, headers or HTML body.
    record = {'observed_at_utc': datetime.now(timezone.utc).isoformat(),
              'observation_type': 'independent unauthenticated known-route GET',
              'path': '/orders', 'method': 'GET', 'query_parameter_names': [],
              'status': response.status, 'content_type': response.headers.get('Content-Type'),
              'location': response.headers.get('Location'),
              'set_cookie_present': bool(response.headers.get('Set-Cookie')),
              'payload': 'none', 'body_retained': False}
    records.append(record)
    previous.write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(record))
