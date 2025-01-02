from flask import Blueprint, render_template
from lib.extensions import database
from lib.api_consumer import get_server_log
from lib.models import *

server_log_bp = Blueprint('server_log', __name__)

@server_log_bp.route("/serverlog")
def serverlog():
    c = database.session.query(Craftyapi).filter_by(id=1).first()
    server_log = get_server_log(c.url, c.api_key, c.server_id)
    
    return render_template("server_log.html",
                           server_log=server_log
                           )
