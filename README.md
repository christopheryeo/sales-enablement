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
-   `tests/list_records.py`: Connects to the DB and lists all records currently present in the `email_registrations` table.
-   `tests/delete_records.py`: Deletes all records from the `email_registrations` table for testing purposes.
-   `tests/add_column.py`: Adds the "Organisation" column to the `email_registrations` table if it doesn't exist.
-   `tests/get_schema.py`: Shows the current schema of the project tables.

### Running Tests

Navigate to the project root directory in your terminal and run a script using:

```bash
python tests/<script_name>.py
# Example:
python tests/list_records.py
```

## Git Versions and Tags

| Tag                        | Commit ID | Description                                                      |
|----------------------------|-----------|------------------------------------------------------------------|
| V1.0.2g                    | <pending>   | Closed off on V1.0.2f                                           |
| V1.0.2f                    | ec791a6   | Built interactive training section                               |
| V1.0.2e                    | e4fefad   | Reviewed training content                                        |
| V1.0.2d                    | 041ff28   | Checked training content                                         |
| V1.0.2c                    | 1cbaaaa   | Tidied up readme.md                                              |
| V1.0.2b                    | a011ad5   | Tidied up V1.0.2 directory structure                             |
| V1.0.2                     | 02c3bab   | V1.0.2: User Cookies Persistent session with UUID cookies        |
| planning-docs-created      | bdf11c2   | Created planning documents for this project                      |
| V1.0.1                     | b81eb11   | Added an admin page to manage database                           |
| V0.0.21                    | b5e31c9   | Integrate git commit history into Audit Trail section            |
| V0.0.20                    | fb70011   | Add Audit Trail section to README.md                             |
| V0.0.19                    | e2352de   | Fix file serving for Vercel deployment and rename hero image     |
| V0.0.18                    | c10629d   | Add Vercel deployment configuration                              |
| V0.0.17                    | 3783d3f   | Cleaned up database access                                       |
| V0.0.16                    | d3d64f4   | Update README with Flask setup and email verification            |
| V0.0.15                    | 4faf051   | User registration confirmation                                   |
| V0.0.14                    | 352861e   | Docs: Add section on database test scripts to README             |
| V0.0.13                    | 861d0bc   | Add test script to list all email registrations                  |
| V0.0.12                    | f19de1e   | Refine DB test scripts                                           |
| V0.0.11                    | dfeaf76   | Create tests dir, add DB tests using .env for URI                |
| V0.0.10                    | c4b3553   | Created training quizzes                                         |
| V0.0.9                     | 9e7ebbc   | Update README with recent features                               |
| V0.0.8                     | 5667de6   | Added hero image                                                 |
| V0.0.7                     | f56af89   | Refactor content, add progress bar, fix styling/interactivity    |
| V0.0.6                     | be900d4   | Added training checklist to track progress                       |
| V0.0.5                     | 5ed36ee   | Verified that the training page reflects content.md              |
| V0.0.4                     | 3c7e971   | Improved collapsible training page                               |
| V0.0.3                     | bb4259e   | Sync content.md and index.html                                   |
| V0.0.2                     | 603068c   | Update README and add images                                     |
| V0.0.1                     | 2c8f98a   | Initial commit: Sales enablement website setup                   |

## Next version to be implemented

The next version to be implemented is **V1.0.3**.

*This section should be auto-incremented as features are moved from backlog to planning/implementation. As versions are incremented, ensure the Audit Trail section is also updated with relevant information about the changes or features added in each version.*

## Audit Trail

### May 10, 2025
- **Project Audit & Feature Documentation (V1.0.2f):**
  - Conducted a comprehensive review of the project structure, directory contents, and key files (`README.md`, `content.md`, `templates/index.html`).
  - Verified the presence and purpose of the `node_modules` directory, confirming its use for front-end tooling (e.g., Tailwind CSS, JavaScript bundling).
  - Documented all interactive training features: collapsible sections, progress tracking, reinforcement questions, and dynamic markdown-driven content rendering.
  - Summarized the integration of Flask backend, markdown content pipeline, and rich front-end interactivity.
  - Updated completed features log and ensured all findings are reflected in project documentation.

### May 5, 2025
- **Checked training content (V1.0.2d):**
  - Verified and synchronized all training content between `content.md` and the interactive training sections in `index.html`.
  - Removed the "Market Overview Introduction" section from both `content.md` and `index.html`.
  - Fixed correct answers for reinforcement questions to ensure consistency between markdown documentation and website quizzes.
  - Updated the Git Versions and Tags table with the new version and commit.

### May 4, 2025
- **Renamed planning folders to version tags:** All feature planning folders under `plans/1_planning/` were renamed to use their respective version tags (`V.1.0.2`, `V.1.0.3`, `V.1.0.4`) for improved clarity and traceability in the planning process.
  - Each versioned subdirectory contains:
    - `README.md`: States the feature goal, key requirements, target audience, and open questions.
    - `spec.md`: Outlines intended functionality, technical scope, UI options, and trade-offs.
    - `design.md`: Captures architectural notes, component interactions, visual sketches, and early design considerations.
- **docs directory structure added**: Created high-level documentation directories to organize feature planning and reference materials
  - `plans/0_backlog/`: Raw feature ideas and initial brainstorming
  - `plans/1_planning/`: Features under planning, with specs and designs
  - `plans/2_inprogress/`: Features currently being implemented, with progress notes
  - `plans/3_completed/`: Completed features, with final specs and summaries
  - `plans/4_archived/`: Archived or deprecated features
  - `plans/_reference/`: Architecture, style guides, and completed features log
  - `plans/_templates/`: Templates for specs and design docs
- **admin-page-db-management-1**: Added admin page for database management
  - Introduced `/admin` dashboard for viewing user progress statistics (sections and quizzes completed, last activity)
  - Added `/admin/clear` endpoint for admins to delete all user records
  - Secured admin actions to authorized emails only
  - Enhanced debug logging for admin and training routes
- **User Session Cookies:** Completed 2025-05-04. Enables secure, persistent user session tracking with UUID cookies for personalized experiences and analytics, verified by automated and manual tests.

### May 2, 2025
- **b5e31c9**: Integrated git commit history into Audit Trail section
  - Enhanced Audit Trail with detailed commit information
  - Added commit hashes for better traceability
  - Expanded historical entries with specific changes
  - Organized entries chronologically
- **e2352de**: Fixed static file serving for Vercel deployment and renamed hero image
  - Added explicit route for static files in app.py
  - Renamed "Home page.png" to "home-page.png" to avoid URL encoding issues
  - Updated HTML template to reference the renamed file
- **c10629d**: Added Vercel deployment configuration
  - Created vercel.json with Python serverless function settings
  - Configured proper routing for Flask application
- **fb70011**: Added Audit Trail section to README.md

### May 1, 2025
- **3783d3f**: Cleaned up database access code
  - Fixed SQL query to use proper column name casing ("Organisation")
  - Consolidated registration logic into the /training route
  - Tested database insertion and retrieval
  - Removed obsolete routes and scripts

### April 28, 2025
- **d3d64f4**: Updated README with Flask setup and email verification
  - Added detailed setup instructions for local development
- **4faf051**: Implemented user registration confirmation
  - Added form validation and success messages
- **352861e**: Added section on database test scripts to README
  - Documented test script usage and configuration
- **861d0bc**: Created script to list all email registrations
  - Added functionality to view database records
- **f19de1e**: Refined database test scripts
  - Improved error handling and output formatting
- **dfeaf76**: Created tests directory with database tests using .env for URI
  - Set up environment variable configuration for database access

### April 26, 2025
- **c4b3553**: Created interactive training quizzes
  - Added reinforcement questions to training sections
  - Implemented JavaScript for quiz interaction
  - Added show/hide functionality for answers

### April 25, 2025
- **9e7ebbc**: Updated README with recent features
- **5667de6**: Added hero image to homepage
- **f56af89**: Refactored content, added progress bar, fixed styling/interactivity
- **be900d4**: Added training checklist to track progress
  - Implemented interactive checkboxes that mark completed sections

### April 24, 2025
- **5ed36ee**: Verified that the training page reflects content.md
- **3c7e971**: Improved collapsible training page
  - Enhanced user experience with expandable sections

### April 23, 2025
- **bb4259e**: Synchronized content.md and index.html
- **603068c**: Updated README and added images
- **2c8f98a**: Initial commit: Sales enablement website setup
