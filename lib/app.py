from flask import Flask, render_template
from .server_log import get_server_log
from .server_status import get_server_status
from .check_api import check_api
from .load_env import *


app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')

@app.context_processor
def inject_global_vars():
    api_status = check_api(crafty_url, crafty_api_key, crafty_server_id)
    return dict(server_name=server_name,
                server_map_url=server_map_url,
                discord_link=discord_link,
                api_status=api_status
                )


@app.route("/")
def index():
    server_status = get_server_status()
    return render_template("index.html",
                           server_status=server_status,
                           server_uri_java=server_uri_java,
                           server_uri_bedrock=server_uri_bedrock
                           )

@app.route("/serverlog")
def serverlog():
    server_log = get_server_log()
    
    return render_template("server_log.html",
                           server_log=server_log
                           )
