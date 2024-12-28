from os import environ
from mcstatus import JavaServer

server = JavaServer.lookup(environ.get("SERVER_URI_JAVA","localhost"))

stats_list = [
    {
        "name": "online",
        "get": lambda status: status.players.online,
        "default": 0,
        "text": lambda x: "%d players" % x if x != 1 else "1 player",
        "color": lambda x: "green" if x > 0 else "red",
        "icon": lambda x: ("group" if x > 1 else "person") if x > 0 else "person_off",
    },
    {
        "name": "status",
        "get": lambda status: True,
        "default": False,
        "text": lambda x: "online" if x else "offline",
        "color": lambda x: "green" if x else "red",
        "icon": lambda x: "power" if x else "power_off",
    },
    {
        "name": "latency",
        "get": lambda status: status.latency,
        "default": 9999,
        "text": lambda x: f"{x:.1f}",
        "color": lambda x: "green" if x < 100 else "red",
        "icon": lambda x: "wifi" if x < 9999 else "wifi_off",
    },
]


def construct_stat(stat, value):
    res = {"name": stat["name"]}
    for key in stat:
        if key in ["get", "default", "name"]:
            continue
        res[key] = stat[key](value)
    return res


def get_server_status():
    try:
        status = server.status()
    except:
        status = None

    server_status = []
    if status:
        for stat in stats_list:
            value = stat["get"](status)
            server_status.append(construct_stat(stat, value))
    else:
        for stat in stats_list:
            value = stat["default"]
            server_status.append(construct_stat(stat, value))

    return server_status
