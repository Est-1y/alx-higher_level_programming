#!/usr/bin/python3
"""
 a script printing the State object with name passed as argument from the database
"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check accuracy of number of arguments.
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        exit()
    # connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # State Objects
    state_name = argv[4]
    queried_state = session.query(State).filter(
        State.name == state_name).first()

    # results
    if queried_state:
        print("{:d}".format(queried_state.id))
    else:
        print("Not found")

    # shutting session
    session.close()
