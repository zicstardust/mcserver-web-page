from os import chmod, environ
from flask import Flask
from flask_login import current_user
from lib.extensions import database, lm
from lib.utils import get_secret_key, get_database_path, create_default_database_register
from lib.api_consumer import check_api, get_server_name
from lib.models import User, Craftyapi, Infos
from lib.background_image import define_background_image
from routes.login import login_bp
from routes.logout import logout_bp
from routes.index import index_bp
from routes.server_log import server_log_bp
from routes.admin import admin_bp


def create_app(testing=False):
    app = Flask(__name__)
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(server_log_bp)
    app.register_blueprint(admin_bp)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{get_database_path('database.db', testing)}'
    app.secret_key = get_secret_key(testing)
    database.init_app(app)
    lm.init_app(app)
    lm.login_view = 'login'

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
    return app

def production():
    app = create_app()
    with app.app_context():
        database.create_all()
        chmod(get_database_path('database.db'), 0o600)
        create_default_database_register(database)
    define_background_image()
    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        database.create_all()
        chmod(get_database_path('database.db'), 0o600)
        create_default_database_register(database)
    from dotenv import load_dotenv
    from os import environ
    load_dotenv()
    define_background_image()
    app.run(debug=True, port=environ.get("PORT",5000))
