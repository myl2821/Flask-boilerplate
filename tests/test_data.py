import os
import sys
import tempfile
os.environ["FLASK_ENV"] = "config.TestingConfig"
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pytest
from base import app, db
import webservice
import json

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()
    return client

# Start out tests
def test_data(client):
    rv = client.get('/data')
    data = json.loads(rv.data)
    assert rv.status_code == 200
    assert data['number'] == 42
