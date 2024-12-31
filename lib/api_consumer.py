import base64
from os.path import exists
import json
import requests
from html import unescape

def check_api(crafty_url, crafty_api_key, crafty_server_id):
    api_url = f"{crafty_url}/api/v2/servers/{crafty_server_id}"
    head = {'Authorization': f'Bearer {crafty_api_key}'}

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

def get_server_log(crafty_url, crafty_api_key, crafty_server_id ):
    api_status = check_api(crafty_url, crafty_api_key, crafty_server_id)
    if api_status == "Ok":
        api_url = f"{crafty_url}/api/v2/servers/{crafty_server_id}/logs"
        head = {'Authorization': f'Bearer {crafty_api_key}'}
        response = requests.get(api_url, headers=head)
        server_status = unescape(json.dumps(response.json()['data'], indent=0))
        return server_status.splitlines()
    return api_status

def get_server_status(crafty_url, crafty_api_key, crafty_server_id):
    api_status = check_api(crafty_url, crafty_api_key, crafty_server_id)
    if api_status == "Ok":
        api_url = f"{crafty_url}/api/v2/servers/{crafty_server_id}/stats"
        head = {'Authorization': f'Bearer {crafty_api_key}'}
        response = requests.get(api_url, headers=head)
        running = (json.dumps(response.json()['data']['running']))
        motd = json.dumps(response.json()['data']['desc'])
        players_online = (json.dumps(response.json()['data']['online']))
        players = convert_players_to_list(json.dumps(response.json()['data']['players']))
        return dict(running=running,
                    motd=motd.replace("\"",""),
                    players_online=int(players_online),
                    players=players)
    return api_status

def get_server_name(crafty_url, crafty_api_key, crafty_server_id):
    api_status = check_api(crafty_url, crafty_api_key, crafty_server_id)
    if api_status == "Ok":
        api_url = f"{crafty_url}/api/v2/servers/{crafty_server_id}/stats"
        head = {'Authorization': f'Bearer {crafty_api_key}'}
        response = requests.get(api_url, headers=head)
        server_name = json.dumps(response.json()['data']['world_name'])
        return server_name.replace("\"","")
    return "MC Server"

def get_server_icon(crafty_url, crafty_api_key, crafty_server_id):
    api_status = check_api(crafty_url, crafty_api_key, crafty_server_id)
    if api_status == "Ok":
        api_url = f"{crafty_url}/api/v2/servers/{crafty_server_id}/stats"
        head = {'Authorization': f'Bearer {crafty_api_key}'}
        response = requests.get(api_url, headers=head)
        iconb64 = json.dumps(response.json()['data']['icon'])
        if iconb64 != "null":
            e = iconb64[1:-1]
            repair = e.replace('\\n', '')
            imgdata = base64.b64decode(repair)
            file = 'static/img/server-icon.png'
            with open(file, 'wb') as f:
                f.write(imgdata)
            if exists(file):
                return "Ok"
    return ""
