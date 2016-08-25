/* Create DB and establish schema, drop first to ensure clean file.*/
DROP DATABASE tournament;

CREATE DATABASE tournament;

\c tournament;

/* Create table to store player info */
CREATE TABLE players_tournament (id SERIAL PRIMARY KEY, name TEXT);

/*Create table to store match info */
CREATE TABLE matches_tournament
  (match_id SERIAL PRIMARY KEY,
  winner_player INTEGER REFERENCES players_tournament(id),
  loser_player INTEGER REFERENCES players_tournament(id));

/* Create view to display the matches each player has matchplayed*/
CREATE VIEW matches_done AS
  SELECT id, name,
  COUNT(matches_tournament.match_id)
  AS matchplayed
  FROM players_tournament
  LEFT JOIN matches_tournament
  ON players_tournament.id = matches_tournament.winner_player
  OR players_tournament.id = matches_tournament.loser_player
  GROUP BY players_tournament.id;

/* Create view to display each players winners */
CREATE VIEW player_winners AS
  SELECT id, name,
  COUNT (matches_tournament.winner_player)
  AS winners
  FROM players_tournament
  LEFT JOIN matches_tournament
  ON players_tournament.id = matches_tournament.winner_player
  GROUP BY id
  ORDER BY winners DESC;

/* Create view to display player standings */
CREATE VIEW standings AS
  SELECT matches_done.id, matches_done.name,
  COALESCE (player_winners.winners,0)
  AS winners,
  COALESCE (matches_done.matchplayed,0)
  AS matchplayed
  FROM matches_done
  LEFT JOIN player_winners
  ON matches_done.id = player_winners.id
  ORDER BY winners DESC;

/*Create Unique Index to prevent rematches */
CREATE UNIQUE INDEX matches_unique
  ON matches_tournament
  (greatest(winner_player, loser_player),
  least (winner_player, loser_player));