#!/usr/bin/python3
"""
script listing all states with a name starting with upper N.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # secure connection.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # cursor object for execution
    cursor = db.cursor()

    # recover states
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # getting results
    states = cursor.fetchall()

    # show output
    for state in states:
        if state[1][0] == 'N':
            print(state)

    # shutting connection
    cursor.close()
    db.close()
