#!/usr/bin/python3
"""
script taking in an argument and displaying all values. 
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # checking accuracy of number of arguments
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        exit()

    # establishing connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # cursor object for execution
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
            argv[4])
    cursor.execute(query)

    # getting results
    states = cursor.fetchall()

    # output
    for state in states:
        if state[1] == argv[4]:
            print(state)

    # shutting connection
    cursor.close()
    db.close()
