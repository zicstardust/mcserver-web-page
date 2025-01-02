from os import chmod
import pytest

from app.lib.background_image import define_background_image
from app.lib.utils import create_default_database_register, get_database_path
from app.main import create_app, database

@pytest.fixture()
def app():
    app = create_app(testing=True)
    app.config.update({
        "TESTING": True,
    })
    with app.app_context():
        database.create_all()
        create_default_database_register(database)
    define_background_image()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()