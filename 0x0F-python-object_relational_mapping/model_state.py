#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Connect to the MySQL server running on localhost at port 3306
engine = create_engine('mysql://localhost:3306')

# Create all tables defined by the classes that inherit from Base
Base.metadata.create_all(engine)
