from api.model.db_initialization import db
from api.model.db_models import UserAccountTable
from sqlalchemy.sql import func
import hashlib
import re
import pdb

#Name: create_user
#Expects: Two Strings. User and Pass correlating to the Username and Password of the signup
#Returns: a true or false to be interpreted by the routing
#Desc: Takes the username and passwork of the signup form and uses it to check via a number of credibility tests
def create_user(User,Pass):
    userCreated = False
    #checks to see if the user exists already and if both the username and password are valid
    if (not user_exists(User) and authenticate(User,Pass)):
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
    
#simple database query to see if the user already exists (we only need the user not the pass)
def user_exists(usr):
    existsTest = db.session.execute(db.select(UserAccountTable).filter_by(username=usr)).scalar()
    return (existsTest != None)

def valid_login(usr, pw):
    hashed_pass = hashlib.sha256(pw.encode()).hexdigest()
    user = db.session.execute(db.select(UserAccountTable).filter_by(username=usr,password=hashed_pass)).scalar()
    return (user != None)

#need to do this in person
def authenticate(usr,ps):
    def check_user(username):
        # Username must be between 3 to 20 characters long
        # and contain only letters, numbers, and underscores
        return (
            (3 <= len(username) <= 20) and
            (re.match(r'^\w+$', username) != None)
            )
    def check_pass(password):
        # Password must be at least 8 characters long
        # and contain at least one digit, one uppercase letter,
        # one lowercase letter, and one special character
        return not (
            (len(password) < 8) or
            (re.search(r'\d', password) == None) or
            (re.search(r'[!@#$%^&*(),.?":{}|<>]', password) == None) or
            (re.search(r'[A-Z]', password) == None) or
            (re.search(r'[a-z]', password) == None)
            )

    #Checks both the username and the password and returns if both of them are valid

    return check_user(usr) and check_pass(ps)