import json
import requests
from .load_env import crafty_url, crafty_api_key, crafty_server_id

def check_api(crafty_url=crafty_url, crafty_api_key=crafty_api_key, crafty_server_id=crafty_server_id):
    api_url = "{}/api/v2/servers/{}".format(crafty_url,crafty_server_id)
    head = {'Authorization': 'Bearer {}'.format(crafty_api_key)}

    try:
        response = requests.get(api_url, headers=head)
    except requests.exceptions.MissingSchema:
        return "Crafty URL Missing Schema"
    except requests.exceptions.ConnectionError:
        return "Crafty URL not found"
    
    if response.status_code == 400:
        return "Server ID invalid"
    
    if response.status_code == 403:
        return "API KEY invalid"
    
    if response.status_code == 200:
        return "Ok"


def convert_players_to_list(players:str):
    s = players.replace(']','')
    s = s.replace('"','')
    s = s.replace('\'','')
    l = list(s.split(sep='['))
    l.pop(0)
    return l

def get_server_log():
    api_status = check_api()
    if api_status == "Ok":
        api_url = "{}/api/v2/servers/{}/logs".format(crafty_url,crafty_server_id)
        head = {'Authorization': 'Bearer {}'.format(crafty_api_key)}
        response = requests.get(api_url, headers=head)
        json_data = (json.dumps(response.json()['data'], indent=0))
        return json_data.splitlines()
    return api_status

def get_server_status():
    api_status = check_api()
    if api_status == "Ok":
        api_url = "{}/api/v2/servers/{}/stats".format(crafty_url,crafty_server_id)
        head = {'Authorization': 'Bearer {}'.format(crafty_api_key)}
        response = requests.get(api_url, headers=head)
        running = (json.dumps(response.json()['data']['running'], indent=4))
        players_online = (json.dumps(response.json()['data']['online'], indent=4))
        players = convert_players_to_list(json.dumps(response.json()['data']['players'], indent=4))
        return dict(running=running, players_online=int(players_online), players=players)
    return api_status
