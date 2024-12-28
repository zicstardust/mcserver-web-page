from os import environ
from flask import Flask, render_template
from lib.background_image import define_background_image
from lib.serverlog import get_serverlog
from lib.server_status import get_server_status

define_background_image()

app = Flask(__name__)

@app.context_processor
def inject_global_vars():
    server_name=environ.get("SERVER_NAME","Minecraft Server")
    server_map_url=environ.get("SERVER_MAP_URL","")
    discord_link=environ.get("DISCORD_LINK","")
    crafty_url=environ.get("CRAFTY_URL","")
    crafty_api_key=environ.get("CRAFTY_API_KEY","")
    crafty_server_id=environ.get("CRAFTY_SERVER_ID","")

    if crafty_server_id != "" and crafty_api_key != "" and crafty_url != "":
        crafty_config_status = "ok"
    else:
        crafty_config_status = "not config"

    return dict(server_name=server_name,
                server_map_url=server_map_url,
                discord_link=discord_link,
                crafty_config_status=crafty_config_status
                )


@app.route("/")
def index():
    server_status = get_server_status()
    return render_template("index.html",
                           server_status=server_status,
                           server_uri_java=environ.get("SERVER_URI_JAVA","localhost"),
                           server_uri_bedrock=environ.get("SERVER_URI_BEDROCK","")
                           )

@app.route("/serverlog")
def serverlog():
    serverlog = get_serverlog()
    return render_template("serverlog.html",
                           serverlog=serverlog
                           )

def production():
    return app


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    app.run(debug=True)
