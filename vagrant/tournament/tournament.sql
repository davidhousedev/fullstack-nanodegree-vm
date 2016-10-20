-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players (
    id      serial primary key,
    name    text
);

CREATE TABLE matches (
    num     serial primary key,
    winner  integer references players (id),
    loser   integer references players (id)
);


-- select players.name, count(matches.winner) as wins
-- from players left join matches
-- on players.id = matches.winner
-- group by players.name;
/*
select players.name, count(matches.winner) as wins, count(matches.loser) as loses
from players left join matches
on players.id = matches.winner or players.id = matches.loser
group by players.name;*/

-- self join matches
/*select a.winner as id, count(a.winner) as wins, count(b.loser) as loses
from matches as a, matches as b
where a.winner = b.loser
group by a.winner;
*/