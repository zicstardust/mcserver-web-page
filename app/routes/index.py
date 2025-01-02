from flask import Blueprint, render_template
from lib.extensions import database
from lib.api_consumer import get_server_icon, get_server_status
from lib.models import *

index_bp = Blueprint('index', __name__)

@index_bp.route("/")
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
