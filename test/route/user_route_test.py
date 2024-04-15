import pytest
from cs_backend.app import create_app

@pytest.fixture
def app():
    return create_app().test_client()

def test_signup_success(app):
    rv = app.post('/api/user/user-signup', json = {
        'username': 'username',
        'password': 'P@ssw0rd'
    })
    assert rv.get_json() == {
        'status': 'success',
        'HTTP Status': 200
    }

def test_repeated_signup_fail(app):
    rv = app.post('/api/user/user-signup', json = {
        'username': 'username',
        'password': 'P@ssw0rd'
    })
    assert rv.get_json() == {
        'status': 'fail',
        'HTTP Status': 200
    }

def test_invalid_signup_fail(app):
    rv = app.post('/api/user/user-signup', json = {
        'username': 'username',
        'password': 'password'
    })
    assert rv.get_json() == {
        'status': 'fail',
        'HTTP Status': 200
    }

def test_missing_data_signup_fail(app):
    rv = app.post('/api/user/user-signup', json = {
        'username': 'username'
    })
    assert rv.get_json() == {
        'status': 'fail',
        'HTTP Status': 200
    }

    rv = app.post('/api/user/user-signup', json = {
        'password': 'password'
    })
    assert rv.get_json() == {
        'status': 'fail',
        'HTTP Status': 200
    }

def test_user_not_existed_login_fail(app):
    rv = app.post('/api/user/user-login', json = {
        'username': 'IDontExist',
        'password': 'P@ssw0rd'
    })
    assert rv.get_json() == {
        'status': 'fail',
        'HTTP Status': 200
    }

def test_wrong_password_login_fail(app):
    rv = app.post('/api/user/user-login', json = {
        'username': 'username',
        'password': 'password'
    })
    assert rv.get_json() == {
        'status': 'fail',
        'HTTP Status': 200
    }

def test_missing_data_login_fail(app):
    rv = app.post('/api/user/user-login', json = {
        'username': 'username'
    })
    assert rv.get_json() == {
        'status': 'fail',
        'HTTP Status': 200
    }

    rv = app.post('/api/user/user-login', json = {
        'password': 'password'
    })
    assert rv.get_json() == {
        'status': 'fail',
        'HTTP Status': 200
    }

def test_login_success(app):
    rv = app.post('/api/user/user-login', json = {
        'username': 'username',
        'password': 'P@ssw0rd'
    })
    assert rv.get_json() == {
        'status': 'success',
        'HTTP Status': 200
    }

def test_delete_success(app):
    rv = app.delete('/api/user/user-delete', json = {
        'username': 'username',
        'password': 'P@ssw0rd'
    })
    assert rv.get_json() == {
        'status': 'success',
        'HTTP Status': 200
    }