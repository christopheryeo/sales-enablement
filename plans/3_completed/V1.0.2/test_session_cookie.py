"""
Automated tests for User Session Cookies (V.1.0.2)
- Backend: Flask test client
- Tests cookie creation, persistence, and security flags
"""
import uuid
from flask import Flask
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from app import app as flask_app

def test_session_cookie_creation_and_persistence():
    client = flask_app.test_client()

    # First visit: should set a new session_id cookie
    response = client.get('/')
    cookies = response.headers.getlist('Set-Cookie')
    session_cookie = [c for c in cookies if 'session_id=' in c]
    assert session_cookie, 'session_id cookie should be set on first visit.'
    cookie_value = session_cookie[0].split('session_id=')[1].split(';')[0]
    # Should be a valid UUID
    uuid.UUID(cookie_value)
    # Check Secure, HttpOnly, SameSite flags
    assert 'HttpOnly' in session_cookie[0]
    assert 'Secure' in session_cookie[0]
    assert 'SameSite=Lax' in session_cookie[0]

    # Second visit with cookie: should persist the same session_id
    client.set_cookie("session_id", cookie_value, domain="localhost")
    response2 = client.get('/')
    # Should not set a new cookie
    cookies2 = response2.headers.getlist('Set-Cookie')
    assert not [c for c in cookies2 if 'session_id=' in c], 'Should not reset session_id if already present.'


def test_training_route_sets_cookie():
    client = flask_app.test_client()
    response = client.get('/training')
    cookies = response.headers.getlist('Set-Cookie')
    session_cookie = [c for c in cookies if 'session_id=' in c]
    assert session_cookie, 'session_id cookie should be set on /training if not present.'

if __name__ == '__main__':
    pytest.main([__file__])
