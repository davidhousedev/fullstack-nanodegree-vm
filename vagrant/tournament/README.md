# Swiss-Style Matchmaking Python Module

This module will facilitate the matchmaking for games played in a swiss-style tournament. In this style of tournament, all participants participate in each round, and are paired up with opponents who have similar win percentages.

The module has support for a single tournament with an even number of total participants.

This project was developed in conjunction with the Full Stack Developer Nanodegree program at Udacity.com


## Requirements

* Python 2.7.9
* Psychopg2 - Python interface for PostgreSQL
* PostgreSQL


## Installation

1. Open PostgreSQL console
2. Navigate to directory of module
3. Import Database and Table schema with: `\i tournament.sql`
4. Import tournament.py to your application

## Functions

### Maitenance
* __deleteMatches()__ - Drops all rows from `matches` and sets player `standings` to 0 wins and 0 matches played
* __deletePlayers()__ - Drops all players from `players` and from `standings`

### Introspection
* __countPlayers()__ - Returns the number of players currently registered in the tournament
* __playerStandings()__ - Returns a list of the players and their win records, sorted by wins

### Tournament Facilitation
* __registerPlayer(name)__ - Adds a player to the tournament database, to the `players` and `standings` tables
* __reportMatch(winner, loser)__ - Record the results of a single match in the database
* __swissPairings()__ - Returns a list of pairs of players for the next round of a match


## Author
All python logic and database schema design, were authored by David A. House (davidhousedev)

Project requirements, function docstrings, and tests found in `tournament_test.py` were all authored by Udacity.com, and were provided to facilitate completion of the project.