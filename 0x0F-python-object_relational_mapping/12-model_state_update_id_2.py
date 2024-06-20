#!/usr/bin/python3
"""
a script changing the name of a State object from the database
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
    # State Object
    state_to_update = session.query(State).filter_by(id=2).first()
    # update
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
    else:
        print("Not found")

    # shut session
    session.close()
