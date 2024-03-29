import pytest
from supply.src.user import User 

@pytest.fixture
def user():
    return User()

def test_get_username(user):
    user.set_username("test_user")
    assert user.get_username() == "test_user"

def test_set_username(user):
    assert user.set_username("new_user") == True
    assert user.get_username() == "new_user"

def test_set_password(user):
    user.set_password("password123")
    assert user.password == "password123"

def test_change_password(user):
    user.set_password("old_pass")
    assert user.change_password("old_pass", "new_pass") == True
    assert user.password == "new_pass"

def test_change_password_invalid_old_password(user):
    user.set_password("old_pass")
    assert user.change_password("wrong_old_pass", "new_pass") == False
    assert user.password == "old_pass"