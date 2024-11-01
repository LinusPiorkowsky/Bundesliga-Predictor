import sqlite3
import click
from flask import current_app, g

# Connect to the database
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

# Close the database connection
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Initialize the database tables
def init_db():
    db = get_db()
    with current_app.open_resource('/Users/linus/Bundesliga-Predictor/Bundesliga-Predictor/sql/create_tables.sql') as f: # Pfad selbst anpassen
        db.executescript(f.read().decode('utf8'))

# Initialize the database 
@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

# Register the database functions with the Flask app
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
