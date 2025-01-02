from .extensions import database
from flask_login import UserMixin

class User(UserMixin, database.Model):
    __tablename__ = 'user'

    id = database.Column(database.Integer, primary_key=True)
    user = database.Column(database.String(40), nullable=False, unique=True)
    password = database.Column(database.String(), nullable=False)
    salt_key = database.Column(database.String(), nullable=False)


class Craftyapi(database.Model):
    __tablename__ = 'craftyapi'

    id = database.Column(database.Integer, primary_key=True)
    url = database.Column(database.String(40), nullable=True)
    api_key = database.Column(database.String(40), nullable=True)
    server_id = database.Column(database.String(40), nullable=True)


class Infos(database.Model):
    __tablename__ = 'infos'

    id = database.Column(database.Integer, primary_key=True)
    server_java = database.Column(database.String(40), nullable=True)
    server_bedrock = database.Column(database.String(40), nullable=True)
    server_map = database.Column(database.String(40), nullable=True)
    discord_link = database.Column(database.String(40), nullable=True)