
from secrets import token_urlsafe
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required

from lib.models import *
from lib.utils import password_to_hash


admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    if request.method == 'POST':
        user = request.form['userForm']
        password = request.form['passwordForm']

        u = database.session.query(User).filter_by(id=1).first()
        if user:
            u.user = user
        if password:
            salt_key = token_urlsafe(64)
            u.salt_key = salt_key
            u.password = password_to_hash(password, salt_key)
        database.session.commit()

        craftyurl = request.form['craftyurlForm']
        craftyserverid = request.form['serverIdForm']
        craftyapi = request.form['craftyapiForm']
        

        c = database.session.query(Craftyapi).filter_by(id=1).first()
        c.url = craftyurl
        c.server_id = craftyserverid
        if craftyapi:
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
        return redirect((url_for('index.index')))
    
    if request.method == 'GET':
        u = database.session.query(User).filter_by(id=1).first()
        c = database.session.query(Craftyapi).filter_by(id=1).first()
        i = database.session.query(Infos).filter_by(id=1).first()
        data = dict(
                    user=u.user,

                    craftyurl=c.url,
                    craftyserverid=c.server_id,


                    server_java=i.server_java,
                    server_bedrock=i.server_bedrock,
                    server_map=i.server_map,
                    discord_link=i.discord_link)
        return render_template("admin.html", data=data)