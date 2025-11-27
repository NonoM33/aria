import sqlite3
import os
import json

DATABASE_PATH = os.getenv("DATABASE_URL", "sqlite:///./system_void.db").replace("sqlite:///", "")

def migrate_installed_packages():
    if not os.path.exists(DATABASE_PATH):
        print(f"Database {DATABASE_PATH} does not exist. It will be created on first run.")
        return
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT installed_packages FROM players LIMIT 1")
        print("Column installed_packages already exists.")
    except sqlite3.OperationalError:
        print("Adding installed_packages column...")
        try:
            cursor.execute("ALTER TABLE players ADD COLUMN installed_packages TEXT DEFAULT '[]'")
            conn.commit()
            print("Migration successful: installed_packages column added.")
        except Exception as e:
            print(f"Migration error: {e}")
            conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_installed_packages()

