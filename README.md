# SmartChat Sales Enablement

A comprehensive sales enablement website for SmartChat resellers. This website provides training materials, product information, and sales resources.

## Features

- Interactive navigation
- Comprehensive training program with:
  - Collapsible sections
  - Visited section indicators (checkboxes)
  - Training progress bar
- Team information
- Product details and differentiators
- Sales process guidelines
- Technical specifications
- Homepage hero image

## Local Development

To run the website locally:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000` in your browser.

## Structure

- `index.html` - Main website content, incorporating details from `content.md`.
- `content.md` - Original source content used to create `index.html`.
- `css/` - Styling files
- `images/` - Image assets

## Database Tests

This project includes scripts to test the connection and functionality with the configured Aiven PostgreSQL database.

### Setup

1.  **Install Dependencies:** Ensure you have `psycopg2-binary` and `python-dotenv` installed:
    ```bash
    pip install psycopg2-binary python-dotenv
    ```
2.  **Create `.env` file:** Create a file named `.env` in the project root directory.
3.  **Add Database URI:** Add your Aiven database connection string to the `.env` file like this:
    ```
    AIVEN_DB_URI="postgres://user:password@host:port/dbname?sslmode=require"
    ```
    *(The `.env` file is included in `.gitignore` to prevent accidental commits.)*

### Test Scripts

The test scripts are located in the `tests/` directory:

-   `tests/aiven_db_test.py`: Connects to the DB, creates the `email_registrations` table (if it doesn't exist), inserts a test email, and reads it back. Uses `ON CONFLICT DO NOTHING` for inserts.
-   `tests/test_registration_timestamp.py`: Connects to the DB, creates the `training_registrations` table (if it doesn't exist), registers a test email with the current timestamp, and reads it back. Uses `ON CONFLICT DO NOTHING`.
-   `tests/list_registrations.py`: Connects to the DB and lists all records currently present in the `email_registrations` table.

### Running Tests

Navigate to the project root directory in your terminal and run a script using:

```bash
python tests/<script_name>.py
# Example:
python tests/list_registrations.py
