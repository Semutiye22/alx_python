# A script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Get MySQL username, password, and database name from command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to the MySQL server
engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

# Bind the engine to the metadata of the Base class
Base.metadata.bind = engine

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Query the State objects that contain the letter 'a' and order by id
states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

# Print the states
for state in states:
    print(f"{state.id}: {state.name}")

# Close the session
session.close()

