import sqlite3

def connect_to_db(db_name):
    """
    Connects to a SQLite database and returns the connection object.
    """
    try:
        conn = sqlite3.connect(db_name)
        print(f"✅ Connected to database: {db_name}")
        return conn
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
