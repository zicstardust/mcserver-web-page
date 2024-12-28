import json
from os import environ
import requests


crafty_url=environ.get("CRAFTY_URL","")
crafty_api_key=environ.get("CRAFTY_API_KEY","")
crafty_server_id=environ.get("CRAFTY_SERVER_ID","")

api_url = "{}/api/v2/servers/{}/logs".format(crafty_url,crafty_server_id)
head = {'Authorization': 'Bearer {}'.format(crafty_api_key)}

def get_serverlog():
    try:
        response = requests.get(api_url, headers=head)
    except requests.exceptions.ConnectionError:
        return "Connection Error"

    if response.status_code == 200:
        json_data = (json.dumps(response.json()['data'], indent=0))
        return json_data.splitlines()
    return "Response error"