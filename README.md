# SmartChat Sales Enablement

A comprehensive sales enablement website for SmartChat resellers. This website provides training materials, product information, and sales resources.

## Features

- Interactive navigation
- Comprehensive training program with:
  - Collapsible sections
  - Visited section indicators (checkboxes)
  - Training progress bar
- Email Registration and Verification:
  - Users access training via an email registration page (`/check_registration`).
  - Entered email is checked against the database.
  - A loading indicator provides feedback during submission.
- Team information
- Product details and differentiators
- Sales process guidelines
- Technical specifications
- Homepage hero image

## Setup and Local Development

1. **Create `.env` file:** See "Database Tests" section below for details on setting up the `.env` file with your `AIVEN_DB_URI`.
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Flask App:**
   ```bash
   python app.py
   ```
   The application will typically run on `http://127.0.0.1:8000`.

## Structure

- `app.py` - Flask application logic (routing, database interaction, session management).
- `requirements.txt` - Python package dependencies.
- `templates/` - HTML templates (`index.html`, `register.html`).
- `static/` - Static assets (CSS, images, JavaScript).
- `content/` - Markdown content files.
- `.env` - Environment variables (database URI - **not committed to Git**).
- `tests/` - Database testing scripts.

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
-   `tests/list_registrations.py`: Connects to the DB and lists all records currently present in the `email_registrations` table.
-   `tests/drop_table.py`: Drops the `training_registrations` table if it exists, to clean up legacy schema.

### Running Tests

Navigate to the project root directory in your terminal and run a script using:

```bash
python tests/<script_name>.py
# Example:
python tests/list_registrations.py
