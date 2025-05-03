import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
DB_URI = os.environ.get("AIVEN_DB_URI")
if not DB_URI:
    raise ValueError("AIVEN_DB_URI not found in .env file or environment variables.")

# Specify the table you want to delete records from
TABLE_NAME = "email_registrations" 

def delete_all_records():
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

        # Ask for confirmation before deleting
        confirm = input(f"WARNING: This will delete ALL records from the '{TABLE_NAME}' table. Continue? (y/n): ")
        if confirm.lower() != 'y':
            print("Operation cancelled.")
            return

        # Delete all records from the table
        delete_sql = f"DELETE FROM {TABLE_NAME};"
        print(f"Deleting all records from '{TABLE_NAME}'...")
        cursor.execute(delete_sql)
        conn.commit()
        
        # Report how many records were deleted
        print(f"Deleted {cursor.rowcount} records from '{TABLE_NAME}'.")

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
    delete_all_records()
