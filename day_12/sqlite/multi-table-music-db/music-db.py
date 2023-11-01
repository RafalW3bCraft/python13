import sqlite3

# Establish a connection to the SQLite database file
connection = sqlite3.connect('music-py.db')

# Create a cursor to interact with the database
cursor = connection.cursor()

# Define a list of SQL statements to create the tables
create_table_statements = [
    """
    CREATE TABLE IF NOT EXISTS "Artist" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        "name" TEXT)
    """,
    """
    CREATE TABLE IF NOT EXISTS "Album" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        artist_id INTEGER,
        "title" TEXT)
    """,
    """
    CREATE TABLE IF NOT EXISTS "Genre" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        "name" TEXT)
    """,
    """
    CREATE TABLE IF NOT EXISTS "Track" (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        album_id INTEGER, genre_id INTEGER, len INTEGER, rating INTEGER,
        "title" TEXT, "count" INTEGER)
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
