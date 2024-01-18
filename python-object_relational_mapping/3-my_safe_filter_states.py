#!/usr/bin/python3
import MySQLdb
import sys

# Extract command line arguments
mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

# Connect to MySQL server
db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=database_name)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Define and execute the safe SQL query with user input
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
cursor.execute(query, (state_name,))

# Fetch all the rows and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the cursor and database connection
cursor.close()
db.close()