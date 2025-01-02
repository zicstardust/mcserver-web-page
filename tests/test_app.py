from app.lib.models import *

def test_database(app):
    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().user == 'admin'
        assert Craftyapi.query.count() == 1
        assert Infos.query.count() == 1
        