from flask import Flask, render_template
from .api_consumer import get_server_log, get_server_status, check_api, get_server_name
from .load_env import server_map_url, discord_link, server_uri_java, server_uri_bedrock


app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')

@app.context_processor
def inject_global_vars():
    api_status = check_api()
    server_name=get_server_name()
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
