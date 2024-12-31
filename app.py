from os import environ
from flask import Flask, redirect, render_template, request, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from lib.database import database
from lib.utils import create_default_database_register, password_to_hash, get_secret_key
from lib.api_consumer import get_server_log, get_server_status, check_api, get_server_name, get_server_icon
from lib.models import *

app = Flask(__name__)
app.secret_key = get_secret_key('.secret.key')
lm = LoginManager(app)
lm.login_view = 'login'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
database.init_app(app)

@lm.user_loader
def user_loader(id):
    user = database.session.query(User).filter_by(id=id).first()
    return user
    
@app.context_processor
def inject_global_vars():
    i = database.session.query(Infos).filter_by(id=1).first()
    c = database.session.query(Craftyapi).filter_by(id=1).first()
    api_status = check_api(c.url, c.api_key, c.server_id)
    server_name=get_server_name(c.url, c.api_key, c.server_id)

    return dict(server_name=server_name,
                server_map_url=i.server_map,
                discord_link=i.discord_link,
                api_status=api_status,
                current_user=current_user
                )


@app.route("/")
def index():
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
        password = password_to_hash(request.form['passwordForm'])
        u = database.session.query(User).filter_by(user=user,password=password).first()
        if not u:
            return "User or Password incorret"
        login_user(u)
        return redirect((url_for('admin')))
    if request.method == 'GET':
        return render_template("login.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect((url_for('index')))

@app.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    if request.method == 'POST':
        user = request.form['userForm']
        password = request.form['passwordForm']

        u = database.session.query(User).filter_by(id=1).first()
        if user:
            u.user = user
        if password:
            u.password = password_to_hash(password)
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
        create_default_database_register(database)
    from dotenv import load_dotenv
    from os import environ
    load_dotenv()
    app.run(debug=True, port=environ.get("PORT",5000))
