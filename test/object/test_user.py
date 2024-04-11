import pytest
from api.object.user import User

@pytest.fixture
def user():
    #Have to set default username and passwords
    username = None 
    password = None
    return User(username,password)

def test_get_username(user):
    user.set_username("test_user")
    assert user.get_username() == "test_user"

def test_set_username(user):
    assert user.set_username("new_user") == True
    assert user.get_username() == "new_user"

def test_set_not_valid_username(user):
    assert not (user.set_username("new_user!"))
    assert not (user.get_username() == "new_user!") # use 'assert not' in place of assertFalse()

def test_set_password(user):
    user.set_password("Password123!")
    #print(user.password)
    assert user.password == "Password123!"

def test_set_password_not_valid_is_working(user):
    user.set_password("password123")
    #print(user.password)
    assert user.password != "password123"

def test_change_password(user):
    user.set_password("Old_password1!")
    assert user.change_password("Old_password1!", "New_password1!") == True
    assert user.password == "New_password1!"

def test_change_password_invalid_old_password(user):
    user.set_password("Old_password1!")
    assert not (user.change_password("wrong_old_pass", "new_pass"))
    assert user.password == "Old_password1!"