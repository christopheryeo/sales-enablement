import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
DB_URI = os.environ.get("AIVEN_DB_URI")
if not DB_URI:
    raise ValueError("AIVEN_DB_URI not found in .env file or environment variables.")

# Specify the table you want to modify
TABLE_NAME = "email_registrations"

def add_columns():
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

        # Add Organisation column if it doesn't exist
        print("\nAdding Organisation column if it doesn't exist...")
        cursor.execute(f"""
        ALTER TABLE {TABLE_NAME} 
        ADD COLUMN IF NOT EXISTS "Organisation" VARCHAR(255)
        """)
        
        # Add sections_completed column (integer with default 0)
        print("Adding sections_completed column if it doesn't exist...")
        cursor.execute(f"""
        ALTER TABLE {TABLE_NAME} 
        ADD COLUMN IF NOT EXISTS sections_completed INTEGER DEFAULT 0
        """)
        
        # Add quizzes_completed column (integer with default 0)
        print("Adding quizzes_completed column if it doesn't exist...")
        cursor.execute(f"""
        ALTER TABLE {TABLE_NAME} 
        ADD COLUMN IF NOT EXISTS quizzes_completed INTEGER DEFAULT 0
        """)
        # Add last_active column (timestamp)
        print("Adding last_active column if it doesn't exist...")
        cursor.execute(f"""
        ALTER TABLE {TABLE_NAME} 
        ADD COLUMN IF NOT EXISTS last_active TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
        """)
        
        # Commit the changes
        conn.commit()
        
        print("\nSuccessfully added columns to email_registrations table:")
        print("- Organisation (VARCHAR(255))")
        print("- sections_completed (INTEGER)")
        print("- quizzes_completed (INTEGER)")
        print("- last_active (TIMESTAMP WITH TIME ZONE)")
        
        # Show the updated table schema
        cursor.execute(f"""
            SELECT column_name, data_type, character_maximum_length
            FROM information_schema.columns
            WHERE table_name = '{TABLE_NAME}'
            ORDER BY ordinal_position;
        """)
        
        print("\n--- Current Schema for '{TABLE_NAME}' ---")
        for col in cursor.fetchall():
            col_name, data_type, max_length = col
            type_info = f"{data_type}"
            if max_length:
                type_info += f"({max_length})"
            print(f"- {col_name}: {type_info}")
        print("---------------------------------------")

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
    add_columns()
