#!/usr/bin/python3
"""
Script deleting State objects with a name containing the letter a
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check accuracy of the number of arguments
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()
    # connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # State Object for states.
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()

    # deletion
    for state in states_to_delete:
        session.delete(state)

    # committing
    session.commit()

    # shut session
    session.close()
