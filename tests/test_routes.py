def test_route_not_exist(client):
    response = client.get('/route_not_exist')
    assert response.status_code == 404

def test_index(client):
    response = client.get('/')
    assert b"Home Page</title>" in response.data

def test_login(client):
    response = client.get('/login')
    assert b"Login</title>" in response.data

def test_serverlog(client):
    response = client.get('/serverlog')
    assert b"Server Log</title>" in response.data

#def test_admin(client):
#    response = client.get('/admin')
#    assert b"Admin</title>" in response.data



