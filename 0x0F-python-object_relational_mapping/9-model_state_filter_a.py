#!/usr/bin/python3
"""
a script listing all State objects containing the letter a from the database
"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check for accuracy of number of arguments
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    # Creating connection.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Objects containing (a)
    filtered_states = session.query(State).filter(State.name.like(
        '%a%')).order_by(State.id).all()
    # results
    for state in filtered_states:
        print("{:d}: {:s}".format(state.id, state.name))

    # shut session
    session.close()
