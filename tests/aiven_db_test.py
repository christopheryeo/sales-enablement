import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
# WARNING: Avoid hardcoded credentials in production code.
# Use environment variables loaded from .env
DB_URI = os.environ.get("AIVEN_DB_URI")
if not DB_URI:
    raise ValueError("AIVEN_DB_URI not found in .env file or environment variables.")

TABLE_NAME = "email_registrations" # Changed table name

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
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
        );
        """
        print(f"Creating table '{TABLE_NAME}' (if not exists)...")
        cursor.execute(create_table_sql)
        conn.commit() # Commit table creation
        print("Table check/creation complete.")

        # 2. Write (INSERT) data
        user_email = "christopher.yeo@gmail.com" # User's email
        insert_sql = f"INSERT INTO {TABLE_NAME} (email) VALUES (%s) ON CONFLICT (email) DO NOTHING RETURNING id;" # Changed column, added ON CONFLICT
        print(f"Writing email: '{user_email}'")
        cursor.execute(insert_sql, (user_email,))
        inserted_id_result = cursor.fetchone()
        conn.commit() # Commit the insert

        if inserted_id_result:
            inserted_id = inserted_id_result[0]
            print(f"Email inserted or already exists. ID: {inserted_id}")

            # 3. Read (SELECT) data
            select_sql = f"SELECT id, email, timestamp FROM {TABLE_NAME} WHERE id = %s;" # Changed column
            print(f"Reading back record with ID: {inserted_id}")
            cursor.execute(select_sql, (inserted_id,))
            result = cursor.fetchone()

            if result:
                read_id, read_email, read_timestamp = result # Changed variable name
                print("\n--- Data Read ---")
                print(f"ID: {read_id}")
                print(f"Email: {read_email}") # Changed label and variable
                print(f"Timestamp: {read_timestamp}")
                print("-----------------")
            else:
                print("Could not read back the inserted record.")
        else:
            # This happens if the email already existed due to ON CONFLICT DO NOTHING
            print(f"Email '{user_email}' likely already existed in the table. Checking...")
            select_sql = f"SELECT id, email, timestamp FROM {TABLE_NAME} WHERE email = %s;"
            cursor.execute(select_sql, (user_email,))
            result = cursor.fetchone()
            if result:
                read_id, read_email, read_timestamp = result
                print("\n--- Existing Data Found ---")
                print(f"ID: {read_id}")
                print(f"Email: {read_email}")
                print(f"Timestamp: {read_timestamp}")
                print("-------------------------")
            else:
                print("Could not find the existing email record unexpectedly.")

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
