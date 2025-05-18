import psycopg2
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
# WARNING: Avoid hardcoded credentials in production code.
# Use environment variables loaded from .env
DB_URI = os.environ.get("AIVEN_DB_URI")
if not DB_URI:
    raise ValueError("AIVEN_DB_URI not found in .env file or environment variables.")

TABLE_NAME = "training_registrations"
TEST_EMAIL = "test.user@example.com" # Using a generic test email

def main():
    conn = None
    cursor = None
    try:
        # Connect to the database
        print(f"Connecting to the database...")
        conn = psycopg2.connect(DB_URI)
        cursor = conn.cursor()
        print("Connection successful!")

        # 1. Create table if it doesn't exist
        # The registration_timestamp defaults to the time of insertion
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            registration_timestamp TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """
        print(f"Creating table '{TABLE_NAME}' (if not exists)...")
        cursor.execute(create_table_sql)
        conn.commit() # Commit table creation
        print("Table check/creation complete.")

        # 2. Write (INSERT) data - register the test email
        # The timestamp will be set automatically by the database default
        # ON CONFLICT ensures we don't insert duplicate emails
        insert_sql = f"""
        INSERT INTO {TABLE_NAME} (email)
        VALUES (%s)
        ON CONFLICT (email) DO NOTHING;
        """
        print(f"Attempting to register email: '{TEST_EMAIL}'")
        cursor.execute(insert_sql, (TEST_EMAIL,))
        conn.commit() # Commit the insert attempt
        if cursor.rowcount > 0:
            print(f"Email '{TEST_EMAIL}' registered successfully.")
        else:
            print(f"Email '{TEST_EMAIL}' was already registered.")

        # 3. Read (SELECT) data - retrieve the registration info for the test email
        select_sql = f"SELECT id, email, registration_timestamp FROM {TABLE_NAME} WHERE email = %s;"
        print(f"\nReading registration info for: '{TEST_EMAIL}'")
        cursor.execute(select_sql, (TEST_EMAIL,))
        result = cursor.fetchone()

        if result:
            read_id, read_email, read_timestamp = result
            print("\n--- Registration Data Found ---")
            print(f"ID: {read_id}")
            print(f"Email: {read_email}")
            print(f"Registered At: {read_timestamp}")
            print("-----------------------------")
        else:
            print(f"Could not find registration record for '{TEST_EMAIL}'. This shouldn't happen.")

    except psycopg2.Error as e:
        print(f"\nDatabase error: {e}")
        if conn:
            conn.rollback() # Rollback changes on error
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
    main()
