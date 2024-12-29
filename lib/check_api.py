import requests


def check_api(crafty_url, crafty_api_key, crafty_server_id):
    api_url = "{}/api/v2/servers/{}".format(crafty_url,crafty_server_id)
    head = {'Authorization': 'Bearer {}'.format(crafty_api_key)}

    try:
        response = requests.get(api_url, headers=head)
    except requests.exceptions.ConnectionError:
        return "Crafty URL invalid"
    
    if response.status_code == 400:
        return "Server ID invalid"
    
    if response.status_code == 403:
        return "API KEY invalid"
    
    if response.status_code == 200:
        return "Ok"