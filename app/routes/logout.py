from flask import Blueprint, redirect, url_for
from flask_login import login_required, logout_user



logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect((url_for('index.index')))