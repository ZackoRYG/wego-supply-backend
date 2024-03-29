from api.model.db_initialization import db
from api.model.db_models import CounterTable
from sqlalchemy.sql import func

#Name: create_user
#Expects: Two Strings. User and Pass correlating to the Username and Password of the signup
#Returns: a true or false to be interpreted by the routing
#Desc: Takes the username and passwork of the signup form and uses it to check via a number of credibility tests
def create_user(User,Pass):
    print("got here lol")
    if (not user_exists(User,Pass)):
        return True

    def user_exists(usr,ps):
        existsTest = db.session.execute(db.select(UserAccountTable).filter_by(username=usr,password=ps)).scalar()
        return (existsTest != None)
    
    def authenticate(usr,ps):
        pass

    def hash(usr,ps):
        pass