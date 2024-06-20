#!/usr/bin/python3
"""
Script adding the State object “Louisiana” to the data
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check accuracy of number of arguments
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()
    # connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Session
    Session = sessionmaker(bind=engine)
    session = Session()
    # State Object
    new_state = State(name="Louisiana")
    # session commitment
    session.add(new_state)
    session.commit()

    # id
    print("{}".format(new_state.id))
    # shut session
    session.close()
