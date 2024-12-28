import json
import requests
from os import environ

crafty_url=environ.get("CRAFTY_URL","")
crafty_api_key=environ.get("CRAFTY_API_KEY","")
crafty_server_id=environ.get("CRAFTY_SERVER_ID","")

api_url = "{}/api/v2/servers/{}/stats".format(crafty_url,crafty_server_id)
head = {'Authorization': 'Bearer {}'.format(crafty_api_key)}


def get_server_status():
    try:
        response = requests.get(api_url, headers=head)
    except requests.exceptions.ConnectionError:
        return "Connection Error"

    if response.status_code == 200:
        running = (json.dumps(response.json()['data']['running'], indent=4))
        players_online = (json.dumps(response.json()['data']['online'], indent=4))
        return dict(running=running, players_online=players_online)
    return "Response error"