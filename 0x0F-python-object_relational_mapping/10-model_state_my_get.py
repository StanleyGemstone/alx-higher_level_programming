#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python script_name.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine(f"mysql://{mysql_username}:{mysql_password}@localhost:3306/{database_name}")

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the State object from the database based on the state name
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()
