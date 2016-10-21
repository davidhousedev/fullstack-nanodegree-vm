#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import tournament


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        conn = psycopg2.connect("dbname=tournament")
        return conn
    except:
        print "Could not connect to database"


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM matches;")
    cur.execute("UPDATE standings "
                "SET wins = 0, matches = 0;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM standings;")
    cur.execute("DELETE FROM players;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT count(id) FROM players;")
    count = cur.fetchone()[0]
    conn.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO players (name)"
                "VALUES (%s);", (name,))  # Add player to players table
    conn.commit()
    cur.execute("INSERT INTO standings "
                "VALUES ((SELECT id FROM players "
                "WHERE name like %s), 0, 0);",
                (name,))  # Add player to standings table
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    cur = conn.cursor()
    query = """
        SELECT players.id, players.name,
               standings.wins, standings.matches
        FROM players, standings
        WHERE players.id = standings.id;
        """  # Joins players (for name) with standings (for win record)
    cur.execute(query)
    standings = []
    for row in cur:
        standings.append(row)  # Populate a list of standings tuples
    conn.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO matches (winner, loser) "
                "VALUES (%s,%s);", (winner, loser))  # Record results of match
    cur.execute("UPDATE standings "
                "SET wins=wins + 1 "
                "WHERE id = %s;", (winner,))  # Update winner in standings
    cur.execute("UPDATE standings "
                "SET matches = matches + 1 "
                "WHERE id = %s or id = %s;", (winner, loser))  # Update matches
    conn.commit()
    conn.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    cur = conn.cursor()
    cur.execute("select players.id, players.name "
                "FROM players join standings "
                "ON players.id = standings.id "
                "ORDER BY wins desc;")  # Sort players by wins
    rows = []
    for row in cur:
        rows.append(row[0])  # Append list with player id
        rows.append(row[1])  # Append list with player name

    # Iterate over every four items in rows list
    # Creates a tuple of every four items
    iteration = iter(rows)
    results = zip(iteration, iteration, iteration, iteration)

    conn.close()
    return results
