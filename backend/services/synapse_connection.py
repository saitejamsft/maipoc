
import json
import requests


token_url = "https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47/oauth2/v2.0/token"


def get_token():
    response = requests.post(
        token_url,
        data={
            "grant_type": "client_credentials",
            "client_id": "cb083852-20f5-4008-9929-e9058b39810b",
            "client_secret": "ylO7Q~CntcDcDDuUWWmAfpQNJbmwNobKp6UT9",
            "scope": "https://dev.azuresynapse.net/.default"
        },
        # headers=headers
    )
    return response.json()['access_token']


def run_job(pipeline_name, body={}):
    token = get_token()
    headers = {
        'Authorization': 'Bearer ' + token
    }
    response = requests.post(
        f"https://maipocaa.dev.azuresynapse.net/pipelines/{pipeline_name}/createRun?api-version=2020-12-01",
        data=json.dumps(body),
        headers=headers
    )
    return response.json()
