from python_http_client import Client
import os
import json
import time

all_repos = [
    'sendgrid/sendgrid-nodejs',
    'twilio/twilio-node'
]

def get_prs(repo):
    client = Client(host="http://{}".format(os.environ.get('GITHUB_MANAGER_IP')))
    query_params = {
        "repo":repo
    }
    response = client.github.prs.get(query_params=query_params)
    return json.loads(response.body)

total_prs_to_review = 0
for repo in all_repos:
    prs = get_prs(repo)
    for pr in prs:
        print('{0}: {1} - {2}'.format(pr['number'], pr['title'], pr['url']))
        total_prs_to_review += 1

print("There are a total of {} open prs needing a code review across all repos".format(total_prs_to_review))