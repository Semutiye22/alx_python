#!/usr/bin/python3
"""
Lists all cities of a state using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

def filter_cities(username, password, database, state_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Query cities with the provided state name and display the results
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))
        results = cursor.fetchall()

        cities_list = ', '.join([row[1] for row in results])

        if cities_list:
            print(cities_list)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))

    finally:
        # Close the cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()

if name == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username, password, database, state_name = sys.argv[1:]

    # Run the filter_cities function with the provided arguments
    filter_cities(username, password, database, state_name)