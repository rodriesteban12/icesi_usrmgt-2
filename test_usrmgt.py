import pytest
import get_users

@pytest.fixture
def client(request):
    client = get_users.app.test_client()
    return client

def user(client):
	return client.get('/api/v1.0/get_users/users',follow_redirects=True)

def test_get_users(client):
	result = user(client)
	assert b'operativos' in result.data

