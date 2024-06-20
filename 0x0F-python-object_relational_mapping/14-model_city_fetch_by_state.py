#!/usr/bin/python3
"""
Script printing all City objects from the database
"""
from model_city import City
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv

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
    # Query
    cities = session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id).order_by(City.id)

    # results
    for city in cities:
        print("{:s}: ({:d}) {:s}".format(city[0], city[1], city[2]))

    # shut session
    session.close()
