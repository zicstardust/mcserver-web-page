from flask import Flask, render_template
from lib.database import database
from lib.utils import before_start_app, create_default_user
from lib.api_consumer import get_server_log, get_server_status, check_api, get_server_name, get_server_icon
from lib.load_env import server_map_url, discord_link, server_uri_java, server_uri_bedrock
from lib.models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
database.init_app(app)

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
    create_default_user(database, User, 'admin', 'admin')
    server_status = get_server_status()
    server_icon = get_server_icon()
    return render_template("index.html",
                           server_status=server_status,
                           server_uri_java=server_uri_java,
                           server_uri_bedrock=server_uri_bedrock,
                           server_icon=server_icon
                           )

@app.route("/serverlog")
def serverlog():
    server_log = get_server_log()
    
    return render_template("server_log.html",
                           server_log=server_log
                           )



def production():
    with app.app_context():
        database.create_all()
    before_start_app()
    return app


if __name__ == "__main__":
    with app.app_context():
        database.create_all()
    from dotenv import load_dotenv
    from os import environ
    load_dotenv()
    before_start_app()
    app.run(debug=True, port=environ.get("PORT",5000))