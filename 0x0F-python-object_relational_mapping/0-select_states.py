#!/usr/bin/python3

"""
Script listing all states from the database hbtn
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # securing connection establishment to MySQL.
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # creating a cursor object for runnning SQL queries
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # getting results
    states = cursor.fetchall()

    # displaying.
    for state in states:
        print(state)

    # shutting the connection
    cursor.close()
    db.close()
