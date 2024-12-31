from flask import Flask, redirect, render_template, request, url_for
from lib.database import database
from lib.utils import create_default_database_register
from lib.api_consumer import get_server_log, get_server_status, check_api, get_server_name, get_server_icon
from lib.models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
database.init_app(app)

@app.context_processor
def inject_global_vars():
    i = database.session.query(Infos).filter_by(id=1).first()
    c = database.session.query(Craftyapi).filter_by(id=1).first()
    api_status = check_api(c.url, c.api_key, c.server_id)
    server_name=get_server_name(c.url, c.api_key, c.server_id)

    return dict(server_name=server_name,
                server_map_url=i.server_map,
                discord_link=i.discord_link,
                api_status=api_status
                )


@app.route("/")
def index():
    create_default_database_register(database)
    c = database.session.query(Craftyapi).filter_by(id=1).first()
    i = database.session.query(Infos).filter_by(id=1).first()
    server_status = get_server_status(c.url, c.api_key, c.server_id)
    server_icon = get_server_icon(c.url, c.api_key, c.server_id)
    return render_template("index.html",
                           server_status=server_status,
                           server_uri_java=i.server_java,
                           server_uri_bedrock=i.server_bedrock,
                           server_icon=server_icon
                           )

@app.route("/serverlog")
def serverlog():
    c = database.session.query(Craftyapi).filter_by(id=1).first()
    server_log = get_server_log(c.url, c.api_key, c.server_id)
    
    return render_template("server_log.html",
                           server_log=server_log
                           )

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['userForm']
        password = request.form['passwordForm']
    return render_template("login.html")


@app.route("/admin", methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        user = request.form['userForm']
        password = request.form['passwordForm']

        u = database.session.query(User).filter_by(id=1).first()
        u.user = user
        u.password = password
        database.session.commit()

        craftyurl = request.form['craftyurlForm']
        craftyserverid = request.form['serverIdForm']
        craftyapi = request.form['craftyapiForm']
        

        c = database.session.query(Craftyapi).filter_by(id=1).first()
        c.url = craftyurl
        c.server_id = craftyserverid
        c.api_key = craftyapi
        database.session.commit()

        server_java = request.form['JavaURLForm']
        server_bedrock = request.form['BedrockURLForm']
        server_map = request.form['MapURLForm']
        discord_link = request.form['DiscordLinkForm']

        i = database.session.query(Infos).filter_by(id=1).first()
        i.server_java = server_java
        i.server_bedrock = server_bedrock
        i.server_map = server_map
        i.discord_link = discord_link
        database.session.commit()
        return redirect((url_for('index')))
    
    if request.method == 'GET':
        u = database.session.query(User).filter_by(id=1).first()
        c = database.session.query(Craftyapi).filter_by(id=1).first()
        i = database.session.query(Infos).filter_by(id=1).first()
        data = dict(
                    user=u.user,
                    password=u.password,

                    craftyurl=c.url,
                    craftyserverid=c.server_id,
                    craftyapi=c.api_key,

                    server_java=i.server_java,
                    server_bedrock=i.server_bedrock,
                    server_map=i.server_map,
                    discord_link=i.discord_link)
        return render_template("admin.html", data=data)



def production():
    with app.app_context():
        database.create_all()
    return app


if __name__ == "__main__":
    with app.app_context():
        database.create_all()
    from dotenv import load_dotenv
    from os import environ
    load_dotenv()
    app.run(debug=True, port=environ.get("PORT",5000))
