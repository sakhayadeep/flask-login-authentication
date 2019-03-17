import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
 
engine = create_engine('sqlite:///userdata.db', echo=True)
 
# create a Session
def insertDb(username, password, email, degree, register, age, city):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    user = User(username, password, email, degree, register, age, city)
    session.add(user)

    # commit the record the database
    session.commit()
    
    session.commit()

if __name__ == "__main__":
    user = input("Insert username : ")
    password = input("Insert password : ")
    email = input("Insert email : ")
    degree = input("Insert degree : ")
    register = int(input("Insert register number : "))
    age = int(input("Insert age : "))
    city = input("Insert city : ")

    insertDb(user, password, email, degree, register, age, city)