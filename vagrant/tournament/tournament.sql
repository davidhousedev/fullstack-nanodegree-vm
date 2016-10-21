-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament; -- Creates database

\c tournament; -- Connect to database

/* Create table for storing players by their full names */
CREATE TABLE players (
    id      serial primary key,
    name    text
);

/* Create table for storing win/loss records of each match */
CREATE TABLE matches (
    num     serial primary key,
    winner  integer references players (id),
    loser   integer references players (id)
);

/* Create table containing each player's win record by id */
CREATE TABLE standings (
    id      integer references players (id),
    wins    integer,
    matches integer
);
