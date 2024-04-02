from api.model.db_initialization import db
from api.model.db_models import UserAccountTable
from sqlalchemy.sql import func

#Name: create_user
#Expects: Two Strings. User and Pass correlating to the Username and Password of the signup
#Returns: a true or false to be interpreted by the routing
#Desc: Takes the username and passwork of the signup form and uses it to check via a number of credibility tests
def create_user(User,Pass):
    #hasing both the username and password sent by the form so that I can check to see if their hashed values already exist in the table
    hashed_userpass = hash(User,Pass)
    if (not user_exists(hashed_userpass[0])):

        #if the user doesn't already exist, we make the user
        db.session.add(UserAccountTable(username=hashed_userpass[0],password=hashed_userpass[1]))
        db.session.commit()
        return True
    
    #simple database query to see if the user already exists (we only need the user not the pass)
    def user_exists(usr):
        existsTest = db.session.execute(db.select(UserAccountTable).filter_by(username=usr)).scalar()
        return (existsTest != None)
    
    #need to do this in person
    def authenticate(usr,ps):
        pass