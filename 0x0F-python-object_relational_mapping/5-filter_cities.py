#!/usr/bin/python3
"""
 a script taking in the name of a state as an argument, listing all cities of that state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # checking accuracy of arg num
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
  
    city_query = """SELECT cities.name
                    FROM states
                    INNER JOIN cities ON states.id = cities.state_id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC"""
    cursor.execute(city_query, (argv[4],))
    # get results
    cities = cursor.fetchall()

    # results
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))
    """
    # output
    for city in cities:
        print(city)"""

    # shutting connection
    cursor.close()
    db.close()
