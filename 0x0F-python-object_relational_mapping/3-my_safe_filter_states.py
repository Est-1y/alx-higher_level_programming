#!/usr/bin/python3

"""
a script taking in arguments and displaying all values.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # checking for accuracy of argument number
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

    # creating SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (argv[4],))

    # get results.
    states = cursor.fetchall()
    # output
    for state in states:
        print(state)
    # shutting connection
    cursor.close()
    db.close()
