import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
DB_URI = os.environ.get("AIVEN_DB_URI")
if not DB_URI:
    raise ValueError("AIVEN_DB_URI not found in .env file or environment variables.")

# Specify the table you want to drop
TABLE_NAME = "training_registrations" 

def drop_table():
    conn = None
    cursor = None
    try:
        # Connect to the database
        print(f"Connecting to the database...")
        conn = psycopg2.connect(DB_URI)
        cursor = conn.cursor()
        print("Connection successful!")

        # Check if table exists
        cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s);", (TABLE_NAME,))
        if not cursor.fetchone()[0]:
            print(f"Table '{TABLE_NAME}' does not exist.")
            return

        # Ask for confirmation before dropping
        confirm = input(f"WARNING: This will DROP the '{TABLE_NAME}' table and ALL its data. Continue? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation cancelled.")
            return

        # Drop the table
        drop_sql = f"DROP TABLE {TABLE_NAME};"
        print(f"Dropping table '{TABLE_NAME}'...")
        cursor.execute(drop_sql)
        conn.commit()
        
        print(f"Table '{TABLE_NAME}' has been dropped successfully.")

    except psycopg2.Error as e:
        print(f"\nDatabase error: {e}")
        if conn:
            conn.rollback()  # Rollback changes on error
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
            print("\nCursor closed.")
        if conn:
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    drop_table()
