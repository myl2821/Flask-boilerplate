import os
import sys
import tempfile
os.environ["FLASK_ENV"] = "config.TestingConfig"
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pytest
from base import app, db
import webservice

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()
    return client


def login(client, username, password):
    return client.get('/sign_in', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


# Start out tests
def test_clean_db(client):
    db.drop_all()
    db.create_all()

def test_index(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert rv.status_code == 200

def test_sign_up(client):
    rv = client.get('/sign_up', query_string=dict(
            username='test',
            password='pass'
        ), follow_redirects=True)
    print rv.data
    assert rv.status_code == 200

    rv = client.get('/sign_up', data=dict(
            username='test',
            password='pass'
        ), follow_redirects=True)
    assert rv.status_code == 400
