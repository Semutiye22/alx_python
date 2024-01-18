#import MySQLdb & sys
import MySQLdb
from sys import argv

#connecting to mysqldb
db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

#getting a cursor 
cur = db.cursor()

# executing a script that lists all states with a name starting with N
cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")


#printing result
myresult = cur.fetchall()
for state in myresult:
  print(state)


# Closing all cursors and databases
cur.close()
db.close()