import hashlib
from os import mkdir, chmod
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from os.path import exists
from lib.models import *
from secrets import token_urlsafe

def resolve_path():
    path = Path().resolve()
    if exists(f'{path}/main.py'):
        return Path().resolve()
    else:
        return f'{Path().resolve()}/app'

def password_to_hash(password:str, salt_key:str):
    password_salt = str(password) + str(salt_key)
    hash = hashlib.sha512(password_salt.encode(encoding = 'UTF-8'))
    return hash.hexdigest()

def get_secret_key(testing=False):
    path=f'{resolve_path()}/data'
    if testing:
        filename = f"{path}/TEST.secret.key"
    else:
        filename = f"{path}/.secret.key"
    
    if not exists(path):
        mkdir(path) 
    
    if exists (filename):
        file = open(filename, "r")
        secret_key = file.read()
        file.close()
    else:
        secret_key = token_urlsafe(16)
        try:
            with open(filename, 'w') as file_object:
                print(secret_key, file=file_object)
        except PermissionError:
            print('Permission denied: /data')
            exit(13)
    chmod(filename, 0o600)
    return secret_key


def get_database_path(filename, testing=False):
    path=f'{resolve_path()}/data'
    if not exists(path):
        mkdir(path)
     
    if testing:
        return f"{path}/TEST.db"
    else:
        return f"{path}/{filename}"

def create_default_database_register(database:SQLAlchemy):
    u = database.session.query(User).all()
    if not u:
        salt_key = token_urlsafe(64)
        u = User(user='admin',
                 password=password_to_hash('admin', salt_key),
                 salt_key = salt_key)
        database.session.add(u)
        database.session.commit()

    c = database.session.query(Craftyapi).all()
    if not c:
        c = Craftyapi(url='https://crafty.exemple.com',
                      server_id='',
                      api_key='')
        database.session.add(c)
        database.session.commit()
    
    i = database.session.query(Infos).all()
    if not i:
        i = Infos(server_java= 'play.exemple.com',
                  server_bedrock='',
                  server_map='',
                  discord_link='')
        database.session.add(i)
        database.session.commit()
