import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
DB_URI = os.environ.get("AIVEN_DB_URI")
if not DB_URI:
    raise ValueError("AIVEN_DB_URI not found in .env file or environment variables.")

# Tables used in this project
PROJECT_TABLES = ['email_registrations', 'training_registrations']

def get_schema():
    conn = None
    cursor = None
    try:
        # Connect to the database
        print(f"Connecting to the database...")
        conn = psycopg2.connect(DB_URI)
        cursor = conn.cursor()
        print("Connection successful!")

        # Check if project tables exist
        for table_name in PROJECT_TABLES:
            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' AND table_name = %s
                );
            """, (table_name,))
            
            exists = cursor.fetchone()[0]
            if exists:
                print(f"\nTable '{table_name}' exists in the database.")
            else:
                print(f"\nTable '{table_name}' does NOT exist in the database.")
        
        # Get schema for project tables only
        print("\n--- Schema for Project Tables ---")
        
        # For each project table, get its schema
        for table_name in PROJECT_TABLES:
            # Check if table exists
            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' AND table_name = %s
                );
            """, (table_name,))
            
            if not cursor.fetchone()[0]:
                continue  # Skip if table doesn't exist
                
            print(f"\n--- Table: {table_name} ---")
            
            # Get column information
            cursor.execute("""
                SELECT 
                    column_name, 
                    data_type, 
                    character_maximum_length,
                    column_default,
                    is_nullable
                FROM 
                    information_schema.columns 
                WHERE 
                    table_name = %s
                ORDER BY 
                    ordinal_position;
            """, (table_name,))
            
            columns = cursor.fetchall()
            
            for col in columns:
                col_name, data_type, max_length, default_val, nullable = col
                
                # Format the column type
                type_info = data_type
                if max_length:
                    type_info += f"({max_length})"
                    
                # Format nullable status
                null_status = "NULL" if nullable == "YES" else "NOT NULL"
                
                # Format default value
                default_str = f"DEFAULT {default_val}" if default_val else ""
                
                print(f"  - {col_name}: {type_info} {null_status} {default_str}")
            
            # Get primary key information
            cursor.execute("""
                SELECT 
                    kcu.column_name
                FROM 
                    information_schema.table_constraints tc
                JOIN 
                    information_schema.key_column_usage kcu
                ON 
                    tc.constraint_name = kcu.constraint_name
                WHERE 
                    tc.table_name = %s
                AND 
                    tc.constraint_type = 'PRIMARY KEY';
            """, (table_name,))
            
            pk_columns = [row[0] for row in cursor.fetchall()]
            
            if pk_columns:
                print(f"  PRIMARY KEY: ({', '.join(pk_columns)})")
                
            # Get unique constraints
            cursor.execute("""
                SELECT 
                    kcu.column_name,
                    tc.constraint_name
                FROM 
                    information_schema.table_constraints tc
                JOIN 
                    information_schema.key_column_usage kcu
                ON 
                    tc.constraint_name = kcu.constraint_name
                WHERE 
                    tc.table_name = %s
                AND 
                    tc.constraint_type = 'UNIQUE'
                ORDER BY
                    tc.constraint_name, 
                    kcu.ordinal_position;
            """, (table_name,))
            
            unique_constraints = cursor.fetchall()
            
            if unique_constraints:
                current_constraint = None
                constraint_columns = []
                
                for col, constraint in unique_constraints:
                    if constraint != current_constraint:
                        if current_constraint:
                            print(f"  UNIQUE: ({', '.join(constraint_columns)})")
                            constraint_columns = []
                        current_constraint = constraint
                    
                    constraint_columns.append(col)
                
                if constraint_columns:
                    print(f"  UNIQUE: ({', '.join(constraint_columns)})")
            
            print("----------------------------")

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
    get_schema()
