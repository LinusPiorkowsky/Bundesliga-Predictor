DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE Games (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_date TEXT,
    season INTEGER,
    home_team_id INTEGER,
    away_team_id INTEGER,
    goals_home INTEGER,
    goals_away INTEGER,
    draw BOOLEAN,
    win_home BOOLEAN,
    win_away BOOLEAN,
    complete BOOLEAN DEFAULT FALSE,
    description TEXT NOT NULL,
    FOREIGN KEY (home_team_id) REFERENCES Teams(team_id),
    FOREIGN KEY (away_team_id) REFERENCES Teams(team_id)
);

CREATE TABLE Teams (
    team_id INTEGER PRIMARY KEY,
    team_name TEXT UNIQUE NOT NULL,
    description TEXT
);
