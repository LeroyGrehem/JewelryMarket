import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='1029384756'
)

# prepare a cursor object
cursorObject = database.cursor()

# Create a dataBase
cursorObject.execute("CREATE DATABASE jewelmarket")

# indicator
print("done")
