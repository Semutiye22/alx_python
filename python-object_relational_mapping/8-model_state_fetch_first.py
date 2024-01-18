# A script that prints the first State object from the database hbtn_0e_6_usa
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Get MySQL username, password, and database name from command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Define the MySQL connection URL
connection_url = f'mysql://{username}:{password}@localhost:3306/{database}'

# Create the SQLAlchemy engine
engine = create_engine(connection_url)

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Retrieve the first State object based on states.id
first_state = session.query(State).order_by(State.id.asc()).first()

# Display the result
if first_state:
    print(f"{first_state.id}: {first_state.name}")
else:
    print("Nothing")

