#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """State class inherits from Base"""

    tablename = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if name == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username, password, database = sys.argv[1:]

    # Create engine and link to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
                           pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)