from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_user
from lib import database
from lib.models import *
from lib.utils import password_to_hash


login_bp = Blueprint('login', __name__)

@login_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['userForm']
        u = database.session.query(User).filter_by(id=1).first()
        password = password_to_hash(request.form['passwordForm'], u.salt_key)
        u = database.session.query(User).filter_by(user=user,password=password).first()
        if not u:
            return render_template("login.html", login_failed=True)
        login_user(u)
        return redirect((url_for('admin.admin')))
    if request.method == 'GET':
        return render_template("login.html")
