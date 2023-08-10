import sys
import json
import urllib.parse

import requests

def update_query(url, key, org_val, new_val):
    pr = urllib.parse.urlparse(url)
    d = urllib.parse.parse_qs(pr.query)
    d[key] = new_val
    return urllib.parse.urlunparse(pr._replace(query=urllib.parse.urlencode(d, doseq=True)))

if len(sys.argv) != 2 or not sys.argv[1]:
    print("Usage:  python "+sys.argv[0]+" 'https://mdr.nims.go.jp/catalog?...'")
    sys.exit()

url = sys.argv[1]

if "catalog?" in url:
    url = url.replace("catalog", "catalog.json")

# Maybe
last_page = False
id_list = []

## Retrieve all ids
while not last_page:
    response = json.loads(requests.get(url).text)
    current_page = response['response']['pages']['current_page']
    next_page = response['response']['pages']['next_page']
    last_page = response['response']['pages']['last_page?']

    id_sublist = [ sub['id'] for sub in response['response']['docs'] ]
    id_list = id_list + id_sublist
    url = update_query(url, 'page', current_page, next_page)
    print(str(len(id_list)) + " in total")


## Download 
for work_id in id_list:
    download_url = "https://mdr.nims.go.jp/download_all/" + work_id + ".zip"
    print(download_url)
    z = requests.get(download_url, allow_redirects=True)
    open(work_id + '.zip', 'wb').write(z.content)
