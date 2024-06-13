import os
import sys
import tempfile
import pytest
import uuid
from flask import Flask
from flask.testing import FlaskClient 
# Add the root directory to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app import app, db


@pytest.fixture
def client():
    # Create a temporary file to act as the test database
    db_fd, db_path = tempfile.mkstemp()
    
    app.config['DATABASE'] = db_path
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, hash TEXT NOT NULL, cash NUMERIC NOT NULL DEFAULT 10000.00)")
            db.execute("CREATE TABLE IF NOT EXISTS history (user_id INTEGER NOT NULL, symbol TEXT NOT NULL, shares INTEGER NOT NULL, transacted DATETIME DEFAULT CURRENT_TIMESTAMP, price NUMERIC NOT NULL)")
        yield client

    os.close(db_fd)
    os.unlink(db_path)

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"health": "ok"}

def test_register(client):
    # Test registration
    new_username = str(uuid.uuid4())[:8]
    rv = client.post('/register', data={
        'username': new_username,
        'password': 'password',
        'confirmation': 'password'
    })
    assert rv.status_code == 302  # Redirect to the home page
    assert b'Redirecting' in rv.data

def test_login(client):
    # Register first
    new_username = str(uuid.uuid4())[:8]
    client.post('/register', data={
        'username': new_username,
        'password': 'password',
        'confirmation': 'password'
    })
    
    # Test login
    rv = client.post('/login', data={
        'username': new_username,
        'password': 'password'
    })
    assert rv.status_code == 302  # Redirect to the home page
    assert b'Redirecting' in rv.data

def test_buy(client):
    # Register and login first
    new_username = str(uuid.uuid4())[:8]
    client.post('/register', data={
        'username': new_username,
        'password': 'password',
        'confirmation': 'password'
    })
    client.post('/login', data={
        'username': new_username,
        'password': 'password'
    })
    
    # Test buy endpoint
    response = client.get("/buy")
    assert response.status_code == 200
    #rv = client.post('/buy', data={
    #    'symbol': 'AAPL',
    #    'shares': '1'
    #})
    #assert rv.status_code == 200
    #assert b'You have bought 1 shares of AAPL' in rv.data

def test_sell(client):
    # Register and login first
    new_username = str(uuid.uuid4())[:8]
    client.post('/register', data={
        'username': new_username,
        'password': 'password',
        'confirmation': 'password'
    })
    client.post('/login', data={
        'username': new_username,
        'password': 'password'
    })
    
    """Tests the sell endpoint"""
    response = client.get("/sell")
    assert response.status_code == 200
    #assert response.json() == {"msg": "sell endpoint"}
    # Buy some stocks first
    #client.post('/buy', data={
    #    'symbol': 'AAPL',
    #    'shares': '1'
    #})

    # Test sell route
    #rv = client.post('/sell', data={
    #    'symbol': 'AAPL',
    #    'shares': '1'
    #})
    #assert rv.status_code == 200
    #assert b'You have sold 1 shares of AAPL' in rv.data

def test_logout(client):
    # Register and login first
    new_username = str(uuid.uuid4())[:8]
    client.post('/register', data={
        'username': new_username,
        'password': 'password',
        'confirmation': 'password'
    })
    client.post('/login', data={
        'username': new_username,
        'password': 'password'
    })
    
    # Test logout
    rv = client.get('/logout')
    assert rv.status_code == 302  # Redirect to the login page
    assert b'Redirecting' in rv.data
