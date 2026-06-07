import psycopg
from psycopg.rows import dict_row

# connection string to local database
DATABASE_URL = "postgresql://angelhernandez@localhost:5432/angelhernandez"

def get_db_connection():
    # opens direct pipe to postgreSQL, returning rows as dictionaries
    conn = psycopg.connect(DATABASE_URL, row_factory=dict_row)
    try:
        yield conn
    finally:
        conn.close()

