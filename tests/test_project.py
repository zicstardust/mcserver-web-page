def test_home(client):
    response = client.get('/')
    assert b"Home Page</title>" in response.data