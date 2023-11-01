import sqlite3

# Establish a connection to the SQLite database file
connection = sqlite3.connect('student-py.db')

# Create a cursor to interact with the database
cursor = connection.cursor()

# Define a list of SQL statements to create the tables
create_table_statements = [
    """
    CREATE TABLE IF NOT EXISTS User (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name   TEXT UNIQUE,
        email  TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Course (
        id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title  TEXT UNIQUE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS Member (
        user_id     INTEGER,
        course_id   INTEGER,
        role        INTEGER,
        PRIMARY KEY (user_id, course_id)
    )
    """
]

# Execute the list of SQL statements to create the tables
for create_table_sql in create_table_statements:
    cursor.execute(create_table_sql)

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()
