#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Check if all three arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script_name.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine(f"mysql://{mysql_username}:{mysql_password}@localhost:3306/{database_name}")

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects from the database and sort them by states.id in ascending order
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

