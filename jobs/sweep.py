import json, re, sys, urllib.request, urllib.error, concurrent.futures as cf
UA={'User-Agent':'Mozilla/5.0','Accept':'application/json'}
def get(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30) as r: return json.loads(r.read())
    except Exception: return None
SLUGS = """gitlab newrelic komodohealth reddit tailscale twilio mozilla chainguard natera cloudflare datadog elastic grafanalabs
mongodb cockroachlabs dropbox pinterest stripe figma okta coinbase databricks 10xgenomics tempus flatironhealth recursionpharmaceuticals
insitro twistbioscience ginkgobioworks vercel netlify fastly planetscale temporaltechnologies sourcegraph astronomer prefect sentry supabase
baseten modal posthog linear dagsterlabs render railway flyio airbyte fivetran dbtlabsinc confluent hashicorp redpanda timescale neon
clickhouse zapier gusto instacart lyft doordash discord duolingo samsara anduril brex ramp plaid affirm robinhood toast zillow
color guardanthealth invitae veracyte grail illumina benchling seqera nextflow dnanexus sevenbridges verily calicolabs
jamasoftware vacasa crowdstrike smartsheet puppet perforce cloudsmith pagerduty launchdarkly honeycomb chronosphere
mux rippling airtable notion retool replit anyscale coreweave lambda togetherai fireworksai huggingface weightsandbiases
render upstash turso tigerbeetle buildkite circleci harness jfrog snyk wiz lacework sysdig aquasec teleport strongdm
""".split()
TITLE=re.compile(r'(platform|infrastructure|infra\b|site reliability|\bsre\b|devops|backend|back-end|distributed|cloud|kubernetes|developer (tools|infrastructure|productivity)|data engineer|bioinformatics|research software|software engineer)',re.I)
BAD=re.compile(r'(manager|director|head of|principal|intern|new grad|frontend|front-end|ios|android|mobile|sales|account|recruit|designer|marketing|security analyst|counsel|\bvp\b|staff product|support engineer|solutions engineer|\bml\b|machine learning research)',re.I)
LOC=re.compile(r'(portland|oregon|\bOR\b|beaverton|hillsboro|remote)',re.I)
NONUS=re.compile(r'(emea|europe|\buk\b|united kingdom|london|germany|berlin|canada|toronto|india|apac|brazil|mexico|spain|france|ireland|poland|netherlands|australia|japan|singapore|latam|israel|portugal)',re.I)
def gh(s):
    d=get(f'https://boards-api.greenhouse.io/v1/boards/{s}/jobs')
    return [(s,j['title'],j['location']['name'],j['absolute_url'],j.get('updated_at','')) for j in (d or {}).get('jobs',[])]
def ashby(s):
    d=get(f'https://api.ashbyhq.com/posting-api/job-board/{s}')
    out=[]
    for j in (d or {}).get('jobs',[]):
        loc=j.get('location','')+(' remote' if j.get('isRemote') else '')+' '+' '.join(x.get('location','') for x in j.get('secondaryLocations',[]))
        out.append((s,j['title'],loc,j['jobUrl'],j.get('publishedAt','')))
    return out
def lever(s):
    d=get(f'https://api.lever.co/v0/postings/{s}?mode=json')
    return [(s,j['text'],j['categories'].get('location','')+' '+j.get('workplaceType',''),j['hostedUrl'],'') for j in (d or [])] if isinstance(d,list) else []
rows=[]
with cf.ThreadPoolExecutor(24) as ex:
    for r in ex.map(lambda s: gh(s)+ashby(s)+lever(s), SLUGS): rows+=r
known=set(sys.argv[1:])
seen=set()
for s,t,l,u,d in sorted(rows):
    if u in seen or u in known: continue
    seen.add(u)
    if TITLE.search(t) and not BAD.search(t) and LOC.search(l) and not (NONUS.search(l) and not re.search(r'portland|oregon|\bUS\b|united states|usa|north america|americas',l,re.I)):
        print(f'{s} | {t} | {l[:70]} | {u}')
print('total postings scanned:',len(rows),file=sys.stderr)
