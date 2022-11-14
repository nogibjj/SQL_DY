## Prepare for testing
import sqlite3

def test_create_sqlite3():
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

def test_insert_data():
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
    # Check if the table has data
    cursor.execute("SELECT * FROM games;")
    if cursor.fetchone() is None:
        # fail the test
        print("Table 'games' has no data")
        exit(1)
    else:
        print("Table 'games' has data")
