# A script that takes in the name of a state as an argument and lists all cities of that state, 
import sys
import MySQLdb

# Get MySQL username, password, database name, and state name from command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

# Connect to the MySQL server
db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

# Create a cursor
cursor = db.cursor()

# Execute the query to retrieve all cities of the given state
query = f"""
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
"""
cursor.execute(query, (state_name,))

# Fetch all the results
results = cursor.fetchall()

# Check if any results were found
if len(results) == 0:
    print(f"No cities found for the specified state '{state_name}'.")
else:
    # Print the cities
    cities = [row[0] for row in results]
    print(', '.join(cities))



# Close the cursor and database connection
cursor.close()
db.close()
