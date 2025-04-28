import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
DB_URI = os.environ.get("AIVEN_DB_URI")
if not DB_URI:
    raise ValueError("AIVEN_DB_URI not found in .env file or environment variables.")

# Specify the table you want to list records from
TABLE_NAME = "email_registrations" 

def list_all_records():
    conn = None
    cursor = None
    try:
        # Connect to the database
        print(f"Connecting to the database...")
        conn = psycopg2.connect(DB_URI)
        cursor = conn.cursor()
        print("Connection successful!")

        # Check if table exists (optional, but good practice)
        cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s);", (TABLE_NAME,))
        if not cursor.fetchone()[0]:
            print(f"Table '{TABLE_NAME}' does not exist.")
            return

        # Select all records from the table
        select_sql = f"SELECT id, email, timestamp FROM {TABLE_NAME} ORDER BY timestamp DESC;"
        print(f"Fetching all records from '{TABLE_NAME}'...")
        cursor.execute(select_sql)
        records = cursor.fetchall()

        if records:
            print(f"\n--- Records in '{TABLE_NAME}' ---")
            for record in records:
                record_id, email, timestamp = record
                print(f"ID: {record_id}, Email: {email}, Timestamp: {timestamp}")
            print("-----------------------------------")
        else:
            print(f"No records found in table '{TABLE_NAME}'.")

    except psycopg2.Error as e:
        print(f"\nDatabase error: {e}")
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
    list_all_records()
