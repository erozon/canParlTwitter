import requests
import os
import json
import pandas as pd

#Security stuff - set the bearer token as an environment variable on your system for this to work.
bearer_token = os.environ.get("BEARER_TOKEN")



#API requestion generating JSON response for all members of a list
search_url = "https://api.twitter.com/1.1/lists/members.json"

#Details for our specific list - Canadian MPs
parlListId = 864088912087715840
query_params = {'list_id': '{}'.format(parlListId), 'count': '5000'}


#More authentication requirements:
def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r


#Generic connecting to the Twitter database:
def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#Method for getting results we want:
def main():
    json_response = connect_to_endpoint(search_url, query_params)
    return json_response





#A method which combines everything; generate a response, throw it into a pandas dataframe,
#   and pull out a list of twitter handles ('screen_name' is the JSON title). 
def getMembers():
    response = main()
    members = pd.DataFrame.from_dict(response['users'])
    return list(members['screen_name'])
