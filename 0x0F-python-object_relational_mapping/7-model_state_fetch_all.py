#!/usr/bin/python3
"""
 a script listing all State objects from the database 
"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Checking accuracy for arguments num
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()
    # database creation.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # sessin creation
    Session = sessionmaker(bind=engine)
    session = Session()
    # state query
    states = session.query(State).order_by(State.id).all()

    # results
    for state in states:
        print("{:d}: {:s}".format(state.id, state.name))

    # shut session
    session.close()
