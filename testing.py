

## Prepare for testing
import sqlite3

## Create a connection to the database
conn = sqlite3.connect('games.db')
cursor = conn.cursor()
# Check if the table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='games';")
if cursor.fetchone() is None:
    # fail the test
    print("Table 'games' does not exist")
    exit(1)
else:
    print("Table 'games' exists")

## Test the database
# Check if the table has the correct columns
cursor.execute("PRAGMA table_info(games);")
columns = cursor.fetchall()
if len(columns) != 31:
    # fail the test
    print("Table 'games' does not have the correct number of columns")
    exit(1)
else:
    print("Table 'games' has the correct number of columns")


# ##Insert all data into the new table
# connects = sqlite3.connect('test.db')
# insert_query = 'INSERT INTO users (FIRST_NAME, last_name) VALUES (?, ?)'
# cursor = connection.cursor()
# for name in names:
#     cursor.execute(insert_query, name)
# connects.commit()

##Select each record from the table
# select_query = 'SELECT * FROM users LIMIT 5'
# for i in cursor.execute(select_query):
#     print(i)