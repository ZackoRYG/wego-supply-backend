from api.model.db_initialization import db
from api.model.db_models import UserAccountTable
from sqlalchemy.sql import func
from api.object.user import *
import hashlib
import re
import pdb

#Name: create_user
#Expects: Two Strings. User and Pass correlating to the Username and Password of the signup
#Returns: a true or false to be interpreted by the routing
#Desc: Takes the username and passwork of the signup form and uses it to check via a number of credibility tests
def create_user(user: User):
    User = user.username
    Pass = user.password
    userCreated = False
    #checks to see if the user exists already and if both the username and password are valid
    if (not user_exists(user) and authenticate(user)):
        #if the user doesn't already exist, and both are valid
        hashed_pass = hashlib.sha256(Pass.encode())

        #add the user and commit to database
        db.session.add(
            UserAccountTable(
                username=User,
                password=str(hashed_pass.hexdigest())))
        db.session.commit()
        userCreated = True

    return userCreated #userCreated

def delete_user(user: User):
    usr = user.username
    hashed_pass = hashlib.sha256(user.password.encode()).hexdigest()
    if valid_login(user):
        db.session.delete(db.session.query(UserAccountTable).filter_by(username=usr,password=hashed_pass).one())
        db.session.commit()
        return True
    else:
        return False
    
#simple database query to see if the user already exists (we only need the user not the pass)
def user_exists(user: User):
    usr = user.username
    existsTest = db.session.execute(db.select(UserAccountTable).filter_by(username=usr)).scalar()
    return (existsTest != None)

def valid_login(User: User):
    usr = User.username
    pw = User.password
    user = None
    if authenticate(User):
        hashed_pass = hashlib.sha256(pw.encode()).hexdigest()
        user = db.session.execute(db.select(UserAccountTable).filter_by(username=usr,password=hashed_pass)).scalar()
    return (user != None)

#need to do this in person
def authenticate(user: User):
    usr = user.username
    ps = user.password
    def check_user(username):
        # Username must be between 3 to 20 characters long
        # and contain only letters, numbers, and underscores
        if (username != None):
            return (
                (3 <= len(username) <= 20) and
                (re.match(r'^\w+$', username) != None)
                )
        else:
            return False
    def check_pass(password):
        # Password must be at least 8 characters long
        # and contain at least one digit, one uppercase letter,
        # one lowercase letter, and one special character
        if (password != None):
            return not (
                (len(password) < 8) or
                (re.search(r'\d', password) == None) or
                (re.search(r'[!@#$%^&*(),.?":{}|<>]', password) == None) or
                (re.search(r'[A-Z]', password) == None) or
                (re.search(r'[a-z]', password) == None)
                )
        else:
            return False

    #Checks both the username and the password and returns if both of them are valid

    return check_user(usr) and check_pass(ps)