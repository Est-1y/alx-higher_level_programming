#!/usr/bin/python3
"""
a script listing all cities from the database.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # establishing connection.
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    # cursor object for execution
    cursor = db.cursor()

    city_query = """SELECT cities.id, cities.name, states.name
                    FROM states
                    INNER JOIN cities ON states.id = cities.state_id
                    ORDER BY cities.id ASC"""
    cursor.execute(city_query)

    # get results
    cities = cursor.fetchall()
    # output
    for city in cities:
        print(city)

    # shutting connection
    cursor.close()
    db.close()
