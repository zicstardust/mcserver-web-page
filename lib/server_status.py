import json
import requests
from .load_env import crafty_url, crafty_api_key, crafty_server_id
from .check_api import check_api

api_status = check_api(crafty_url, crafty_api_key, crafty_server_id)

def get_server_status():
    if api_status == "Ok":
        api_url = "{}/api/v2/servers/{}/stats".format(crafty_url,crafty_server_id)
        head = {'Authorization': 'Bearer {}'.format(crafty_api_key)}
        response = requests.get(api_url, headers=head)
        running = (json.dumps(response.json()['data']['running'], indent=4))
        players_online = (json.dumps(response.json()['data']['online'], indent=4))
        return dict(running=running, players_online=players_online)
    return api_status
