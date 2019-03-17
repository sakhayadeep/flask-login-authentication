from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///userdata.db', echo=True)
Base = declarative_base()
 
########################################################################
class User(Base):
    __tablename__ = "users"
 
    id = Column("id", Integer, primary_key = True)
    username = Column("username", String, unique = True)
    password = Column("password", String)
    email = Column("email", String, nullable = False, unique = True)
    degree = Column("degree", String)
    register = Column("register", Integer, unique = True)
    age = Column("age", Integer)
    city = Column("city", String)
 
#----------------------------------------------------------------------
    def __init__(self, username, password, email, degree, register, age, city):
        self.username = username
        self.password = password
        self.email = email
        self.degree = degree
        self.register = register
        self.age = age
        self.city = city

# create tables
Base.metadata.create_all(engine)