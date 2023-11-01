import sqlite3

# Establish a connection to the SQLite database file (creates a new one if it doesn't exist)
connection = sqlite3.connect('user-email-py.db')

# Create a cursor to interact with the database
cursor = connection.cursor()

# Drop the Users table if it exists
#cursor.execute("DROP TABLE IF EXISTS 'Users'")

# Create the Users table with "name" and "email" columns
cursor.execute("CREATE TABLE 'Users' ('name' TEXT, 'email' TEXT)")

# Retrieve and print all data from the Users table
cursor.execute("SELECT * FROM Users")
data = cursor.fetchall()
for row in data:
    print(row)

# Close the cursor and the database connection
cursor.close()
connection.close()
