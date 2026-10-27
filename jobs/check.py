import json, glob, re, sys, urllib.request, urllib.error
UA={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
def get(u, data=None):
    req=urllib.request.Request(u, data=data, headers={**UA, **({'Content-Type':'application/json'} if data else {})})
    try:
        with urllib.request.urlopen(req, timeout=30) as r: return r.status, r.read().decode('utf-8','replace')
    except urllib.error.HTTPError as e: return e.code, e.read().decode('utf-8','replace')
    except Exception as e: return 0, str(e)
ashby={}
def check(u):
    m=re.search(r'greenhouse\.io/(\w+)/jobs/(\d+)',u)
    if m:
        s,_=get(f'https://boards-api.greenhouse.io/v1/boards/{m[1]}/jobs/{m[2]}'); return 'open' if s==200 else f'closed({s})'
    m=re.search(r'ashbyhq\.com/([\w-]+)/([0-9a-f-]{36})',u)
    if m:
        if m[1] not in ashby:
            s,b=get(f'https://api.ashbyhq.com/posting-api/job-board/{m[1]}'); ashby[m[1]]={j['id'] for j in json.loads(b)['jobs']} if s==200 else None
        ids=ashby[m[1]]; return 'unknown' if ids is None else ('open' if m[2] in ids else 'closed')
    m=re.search(r'myworkdayjobs\.com/en-US/(\w+)/details/(.+)',u)
    if m:
        s,b=get(f'https://intel.wd1.myworkdayjobs.com/wday/cxs/intel/{m[1]}/job/{m[2]}')
        if s!=200: return f'closed({s})'
        return 'open' if json.loads(b).get('jobPostingInfo',{}).get('canApply',True) else 'closed(canApply=false)'
    m=re.search(r'amazon\.jobs/en/jobs/(\d+)',u)
    if m:
        s,b=get(u); return 'open' if s==200 and 'apply' in b.lower() and 'no longer' not in b.lower() else f'check({s})'
    s,b=get(u); low=b.lower()
    flag=[w for w in ['no longer','not found','expired','has been filled','closed'] if w in low]
    return f'http {s} len={len(b)} flags={flag}'
for f in sorted(glob.glob((sys.argv[1] if len(sys.argv)>1 else 'db/jobs')+'/*.json')):
    x=json.load(open(f)); print(f.split('/')[-1][:-5], x['status'], check(x['url']), sep=' | ', flush=True)
