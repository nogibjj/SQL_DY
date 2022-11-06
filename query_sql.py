#!/usr/bin/env python3


import click
import sqlite3


@click.command()
@click.argument("query", type=click.File("r"))
@click.argument("database", type=click.Path(exists=True))

def main(query='SELECT * FROM games LIMIT 3;', database='/workspaces/SQL_DY/games.db'):
    """Run SQL query on the database."""
    db = sqlite3.connect(database)
    cursor = db.cursor()
    for line in query:
        cursor.execute(line)
    for row in cursor:
        print(row)
    db.close()


if __name__ == "__main__":
    main()
    

# def main(query, database="games.db"):
#     """Execute a SQL query on a SQLite database."""
#     # Open the database
#     db = sqlite3.connect(database)
#     print("Database created and Successfully Connected to SQLite")
#     # Create a cursor to execute SQL commands
#     cursor = db.cursor()
#     # Execute the query
#     cursor.execute(query.read())
#     # Print the results
#     # for row in cursor.fetchall():
#     #     print(row)


#     # select whole table from database "games"
#     cursor.execute("select * from games")
#     rows = cursor.fetchall()

#     # Select first 3 record from the table
#     query_select = "SELECT * FROM games LIMIT 3"
#     for i in cursor.execute(query_select):
#         print(i)

#     #### query 1 : How many 11vs11 games I have officiated between Jan. 2021 and July 2022?
#     # select the game played as 11 vs 11
#     cursor.execute("select * from games where Number_of_Players == '11';")
#     game11v11 = cursor.fetchall()
#     print(
#         f"I have officiated {len(game11v11)} 11 vs 11 games from January 2021 to July 2022."
#     )

#     #### query 2 : How many 8vs8 games I have officiated between Jan. 2021 and July 2022?
#     cursor.execute("select * from games where Number_of_Players == '8';")
#     game8v8 = cursor.fetchall()
#     print(
#         f"I have officiated {len(game8v8)} 8 vs 8 games from January 2021 to July 2022."
#     )

#     #### query 3 : How many games I have officiated as Referee between Jan. 2021 and July 2022?
#     cursor.execute("select * from games where Poisition == 'RR';")
#     RR = cursor.fetchall()
#     print(
#         f"I have officiated {len(RR)} games as referee from January 2021 to July 2022."
#     )

#     #### query 4 : How many games I have officiated as Assistant Referee between Jan. 2021 and July 2022?
#     cursor.execute("select * from games where Poisition like 'AR%';")
#     AR = cursor.fetchall()
#     print(
#         f"I have officiated {len(AR)} games as assistant referee from January 2021 to July 2022."
#     )

#     #### query 5 : How many games I have officiated as 4th Official between Jan. 2021 and July 2022?
#     cursor.execute("select * from games where Poisition == '4th O';")
#     fourthO = cursor.fetchall()
#     print(
#         f"I have officiated {len(fourthO)} games as 4th official from January 2021 to July 2022."
#     )

#     #### query 6 : How many Yellow Cards I have shown as Referee between Jan. 2021 and July 2022?
#     cursor.execute("select sum(YC_Count) from games where Poisition == 'RR';")
#     YC = cursor.fetchall()
#     print(
#         f"I have given {YC[0][0]:.0f} Yellow Cards as a referee from January 2021 to July 2022."
#     )

#     #### query 7 : How many Red Cards I have shown as Referee between Jan. 2021 and July 2022?
#     cursor.execute("select sum(RC_Count) from games where Poisition == 'RR';")
#     RC = cursor.fetchall()
#     print(
#         f"I have given {RC[0][0]:.0f} Red Cards as a referee from January 2021 to July 2022."
#     )

#     #### query 8 : How many Yellow Cards per game when I officiate as Referee between Jan. 2021 and July 2022?
#     cursor.execute("select avg(YC_Count) from games where Poisition == 'RR';")
#     YC_per_game = cursor.fetchall()
#     print(
#         f"I have given {YC_per_game[0][0]:.2f} Yellow Cards per game as a referee from January 2021 to July 2022."
#     )

#     #### query 9 : How many Red Cards per game when I officiate as Referee between Jan. 2021 and July 2022?
#     cursor.execute("select avg(RC_Count) from games where Poisition == 'RR';")
#     RC_per_game = cursor.fetchall()
#     print(
#         f"I have given {RC_per_game[0][0]:.2f} Red Cards per game as a referee from January 2021 to July 2022."
#     )

#     #### query 10 : The most cards shown in a game as a referee
#     cursor.execute(
#         "select Game_Date, YC_Count, YCs_Count, RC_Count, max(YC_Count + RC_Count) as Cards_Max, Team_Home_vs_Away, Game_Type, Stage, Site, Score, Distance, Other_Officials from games where Poisition == 'RR';"
#     )
#     Cards_Max = cursor.fetchall()
#     print(
#         f"The most cards shown in a game as a referee was {Cards_Max[0][4]:.0f}, (YC: {Cards_Max[0][1]}, 2nd YC: {Cards_Max[0][2]}, and RC: {Cards_Max[0][3]}), {Cards_Max[0][5]} (Score:{Cards_Max[0][9]}, {Cards_Max[0][6]}{Cards_Max[0][7]}) on {Cards_Max[0][0]} at {Cards_Max[0][8]}."
#     )
#     print(
#         f"My running distance was {Cards_Max[0][10]} kilometers. Other officials were: {Cards_Max[0][11]}."
#     )

#     #### query 11 : The most distanced covered in a game as a referee
#     cursor.execute(
#         "select Game_Date, YC_Count, YCs_Count, RC_Count, max(Distance) as Distance_Max, Team_Home_vs_Away, Game_Type, Stage, Site, Score, Other_Officials from games where Poisition == 'RR';"
#     )
#     Distance_Max = cursor.fetchall()
#     print(
#         f"The most distance covered in a game as a referee was {Distance_Max[0][4]} kilometers, {Distance_Max[0][5]} (Score:{Distance_Max[0][9]}, {Distance_Max[0][6]} 22 {Distance_Max[0][7]} YC: {Distance_Max[0][1]}, 2nd YC: {Distance_Max[0][2]}, and RC: {Distance_Max[0][3]}) on {Distance_Max[0][0]} at {Distance_Max[0][8]}."
#     )

    # db.close()


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
