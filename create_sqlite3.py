import sqlite3
import csv

# Create a database in RAM
db = sqlite3.connect(":memory:")
# Create a database in a file
db = sqlite3.connect("games.db")

# Create a cursor to execute SQL commands
cursor = db.cursor()

# Create a table if not exists

cursor.execute(
    "CREATE TABLE IF NOT EXISTS games (Game_Date,Game_Day,Distance,Game_Number,Game_Number1,FULL_GAME,Distance_From_Home,Time,Game_Type,Level,Competition_System,Stage,Site,Team_Home_vs_Away,Poisition,Other_Officials,Color_Home_vs_Away,Score,Score_Time_Home ,Score_Time_Away,Kick_off,Attack_Direction,Duration,Ball_Size,Number_of_Players,Weather,Temperature_Celsius,Report,YC_Count,YCs_Count,RC_Count);"
)

# Read the CSV file
with open("Game Report.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    # Read data row by row
    for row in reader:
        # Insert data
        cursor.execute(
            "INSERT INTO games VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            row,
        )

# Append 2021 Data
with open("Game Report_2021.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    # Read data row by row
    for row in reader:
        # Insert data
        cursor.execute(
            "INSERT INTO games VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            row,
        )


# Save (commit) the changes
db.commit()

# Close the connection
db.close()
