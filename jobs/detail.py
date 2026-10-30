import json,re,sys,html,urllib.request
UA={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30) as r: return json.loads(r.read())
def text(h): t=re.sub(r'<[^>]+>',' ',html.unescape(h or '')); return re.sub(r'\s+',' ',t)
boards={}
for u in sys.argv[1:]:
    m=re.search(r'ashbyhq\.com/([\w-]+)/([0-9a-f-]{36})',u)
    w=re.search(r'//(\w+)\.(wd\d+)\.myworkdayjobs\.com/(?:en-US/)?(\w+)/(?:details|job)/(.+)',u)
    if w:
        j=get(f'https://{w[1]}.{w[2]}.myworkdayjobs.com/wday/cxs/{w[1]}/{w[3]}/job/{w[4]}')['jobPostingInfo']; t=text(j['jobDescription'])
        loc=f"{j.get('location')} | {j.get('remoteType') or ''} | {j.get('timeType') or ''}"
        pay=re.findall(r'\$\s?[\d,]+(?:\.\d+)?\s?(?:-|–|—|to)\s?\$\s?[\d,]+(?:\.\d+)?(?:\s*(?:per|/)\s*\w+)?',t)[:2]
    elif m:
        if m[1] not in boards: boards[m[1]]=get(f'https://api.ashbyhq.com/posting-api/job-board/{m[1]}?includeCompensation=true')['jobs']
        j=next(x for x in boards[m[1]] if x['id']==m[2]); t=j.get('descriptionPlain') or text(j.get('descriptionHtml'))
        pay=(j.get('compensation') or {}).get('compensationTierSummary') or ''
        loc=f"{j.get('location')} | workplace={j.get('workplaceType')} remote={j.get('isRemote')}"
    else:
        m=re.search(r'(?:greenhouse\.io/|gh_jid=)',u); b=re.search(r'greenhouse\.io/(\w+)/jobs/(\d+)',u) or re.search(r'//(?:www\.)?(\w+)\.com.*gh_jid=(\d+)',u)
        j=get(f'https://boards-api.greenhouse.io/v1/boards/{b[1]}/jobs/{b[2]}?content=true'); t=text(j['content']); loc=j['location']['name']
        p=re.findall(r'\$\s?\d{2,3}[,.]?\d{0,3}\s?[kK]?\s?(?:-|–|—|to)\s?\$\s?\d{2,3}[,.]?\d{0,3}\s?[kK]?',t); pay=p[:2]
    yrs=re.findall(r'[^.]{0,60}\d\+?\s*(?:\+|or more)?\s*years[^.]{0,80}',t)[:3]
    kw=sorted({k for k in ['Go','Golang','Python','Kubernetes','Terraform','AWS','GCP','Azure','Postgres','Rust','C++','Java','Scala','Kafka','Ruby','TypeScript','on-call','hybrid','in-office','relocat'] if re.search(r'\b'+re.escape(k)+r'\b',t,re.I)})
    print(f"\n### {j.get('title')}\n{u}\nloc: {loc}\npay: {pay}\nyears: {yrs}\nkw: {kw}")
