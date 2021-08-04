import requests
import os
import json
import pandas as pd


#Authorization stuff, connecting to API, and sandwich it all together. 
def create_headers():
    """
    create the request headers, includes the token
    """
    headers = {"Authorization": "Bearer {}".format(os.environ.get("BEARER_TOKEN"))}
    return headers

def connect_to_endpoint(url, headers):
    """
    connect to the API and return the json response
    """
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def main():
    headers = create_headers()
    json_response = connect_to_endpoint(search_url, headers)
    #return json.dumps(json_response, indent=4, sort_keys=True)
    return json_response

def 


