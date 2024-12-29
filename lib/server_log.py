import json
import requests
from .load_env import crafty_url, crafty_api_key, crafty_server_id
from .check_api import check_api

api_status = check_api(crafty_url, crafty_api_key, crafty_server_id)

def get_server_log():
    if api_status == "Ok":
        api_url = "{}/api/v2/servers/{}/logs".format(crafty_url,crafty_server_id)
        head = {'Authorization': 'Bearer {}'.format(crafty_api_key)}
        response = requests.get(api_url, headers=head)
        json_data = (json.dumps(response.json()['data'], indent=0))
        return json_data.splitlines()
    return api_status
