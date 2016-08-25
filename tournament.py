import psycopg2


"""Connect to the PostgreSQL database.
Returns a database connection."""
def connect():
    return psycopg2.connect("dbname=tournament")


"""Returns the number of players
currently registered."""
def countPlayers():
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count (*) FROM players_tournament")
    player_count = c.fetchall()[0][0]
    DB.close()
    return player_count


"""Remove all the match records
from the database."""
def deleteMatches():
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches_tournament")
    DB.commit()
    DB.close()

"""Remove all the player records
from the database."""
def deletePlayers():
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players_tournament")
    DB.commit()
    DB.close()


"""Adds a player to the
tournament database."""
def registerPlayer(name):
    """
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players_tournament (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


"""Returns a list of the players
and their win records, sorted by wins."""
def playerStandings():
    """"
    The first entry in the list should be the player in first place,
    or a playertied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT * FROM standings")
    rows = c.fetchall()
    DB.close()
    return rows


"""Records the outcome of a
single match between two players."""
def reportMatch(winner_player, loser_player):
    """
    Args:
      winner_player:  the id number of the player who won
      loser_player:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO matches_tournament (winner_player, loser_player) VALUES (%s,%s)",
              (winner_player, loser_player,))
    DB.commit()
    DB.close()


"""Returns a list of pairs of
players for the next round of a match."""
def swissPairings():
    """
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
    standings = playerStandings()
    pairs = []

    for p1, p2 in zip(standings[0::2], standings[1::2]):
        pairs.append((p1[0], p1[1], p2[0], p2[1]))

    return pairs
