<div align="center">
  <h1>SmartChat Sales Enablement</h1>
  <p>
    <strong>A comprehensive sales enablement platform for SmartChat resellers</strong>
  </p>
  <p>
    <a href="#features">Features</a> •
    <a href="#getting-started">Getting Started</a> •
    <a href="#project-structure">Project Structure</a> •
    <a href="#database-configuration">Database</a> •
    <a href="#testing">Testing</a>
  </p>
</div>

## 📋 Overview

SmartChat Sales Enablement is a robust platform designed to empower SmartChat resellers with comprehensive training, product knowledge, and sales resources. The platform features an intuitive interface with interactive training modules, progress tracking, and user management capabilities.

## ✨ Features <a name="features"></a>

### Interactive Training Program
- **Progress Tracking**
  - Visual progress indicators
  - Persistent session tracking using cookies
  - Section completion status
  - Quiz completion tracking
- **Interactive Elements**
  - Collapsible sections for better navigation
  - Reinforcement questions with show/hide answers
  - Dynamic content loading
  - Responsive design for all devices

### User Management
- Email-based registration and verification
- Session management with UUID cookies
- Admin dashboard for user management
- Progress tracking per user

### Content Management
- Markdown-driven content system
- Easy content updates without code changes
- Version-controlled training materials
- Interactive quizzes and knowledge checks

## 🚀 Getting Started <a name="getting-started"></a>

### Prerequisites

- Python 3.8+
- PostgreSQL 13+ (local or Aiven)
- Node.js 16+ (for frontend assets)
- Git

### Quick Start

1. **Clone and set up the repository**
   ```bash
   # Clone the repository
   git clone https://github.com/christopheryeo/sales-enablement.git
   cd sales-enablement
   
   # Set up Python virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configure environment**
   Create a `.env` file with the following variables:
   ```env
   # Application
   FLASK_APP=src/app.py
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   
   # Database
   AIVEN_DB_URI=postgres://user:password@host:port/dbname?sslmode=require
   
   # Optional: Email Configuration
   MAIL_SERVER=smtp.example.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@example.com
   MAIL_PASSWORD=your-email-password
   ```

3. **Initialize the database**
   ```bash
   flask db upgrade
   ```

4. **Run the application**
   ```bash
   # Development server
   flask run --port 8000
   
   # Production (using Gunicorn)
   gunicorn "src.app:create_app()" -b :8000
   ```
   Visit `http://localhost:8000` in your browser.

## 🏗️ Project Structure <a name="project-structure"></a>

```
sales-enablement/
├── src/                    # Application source code
│   ├── app.py             # Flask application factory
│   ├── config.py          # Configuration management
│   ├── models/            # Database models
│   ├── routes/            # Application routes
│   ├── services/          # Business logic
│   └── utils/             # Helper functions
│
├── static/               # Static assets
│   ├── css/               # Stylesheets
│   ├── js/                # Client-side scripts
│   └── images/            # Image assets
│
├── templates/            # Jinja2 templates
│   ├── base.html          # Base template
│   ├── auth/              # Authentication templates
│   └── training/          # Training section templates
│
├── tests/                # Test suite
│   ├── e2e/              # End-to-end tests
│   ├── integration/       # Integration tests
│   └── unit/             # Unit tests
│
├── plans/                # Project documentation
│   ├── 0_backlog/        # Future features
│   ├── 1_planning/       # Upcoming versions
│   ├── _reference/       # Documentation
│   └── _templates/       # Documentation templates
│
├── migrations/           # Database migrations
├── content/              # Dynamic content (Markdown)
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## 🔧 Database Configuration <a name="database-configuration"></a>

The application uses PostgreSQL as its primary database. You can use either a local PostgreSQL instance or Aiven's managed PostgreSQL service.

### Option 1: Local PostgreSQL

1. **Install PostgreSQL**
   ```bash
   # Ubuntu/Debian
   sudo apt update
   sudo apt install postgresql postgresql-contrib
   
   # macOS (using Homebrew)
   brew install postgresql
   ```

2. **Create Database and User**
   ```bash
   sudo -u postgres createuser -P your_username
   sudo -u postgres createdb -O your_username your_database
   ```

3. **Update `.env`**
   ```env
   AIVEN_DB_URI=postgresql://your_username:your_password@localhost:5432/your_database
   ```

### Option 2: Aiven PostgreSQL

1. **Create Aiven Service**
   - Log in to [Aiven Console](https://console.aiven.io/)
   - Create a new PostgreSQL service
   - Wait for the service to be provisioned

2. **Get Connection String**
   - Go to your service overview
   - Click on "Connection information"
   - Copy the "Connection URI"

3. **Update `.env`**
   ```env
   AIVEN_DB_URI=your_aiven_connection_string
   ```

### Database Migrations

The project uses Flask-Migrate for database migrations:

```bash
# Initialize migrations (first time only)
flask db init

# Create new migration
flask db migrate -m "Your migration message"

# Apply migrations
flask db upgrade
```

## 🧪 Testing <a name="testing"></a>

### Running Tests

The project includes a comprehensive test suite to ensure code quality and functionality.

#### Unit Tests
```bash
# Run all unit tests
pytest tests/unit/

# Run specific test file
pytest tests/unit/test_module.py
```

#### Integration Tests
```bash
# Run all integration tests
pytest tests/integration/

# Run with coverage report
pytest --cov=src tests/
```

#### End-to-End Tests
```bash
# Start the test server
python tests/e2e/start_server.py &


# Run Cypress tests
cd tests/e2e
npm install
npx cypress run
```

### Database Test Scripts

Utility scripts for database testing and maintenance are available in `tests/db/`:

| Script | Purpose |
|--------|---------|
| `test_connection.py` | Verify database connectivity |
| `schema_migration.py` | Apply database schema changes |
| `seed_database.py` | Populate with test data |
| `backup_database.py` | Create database backups |

Example usage:
```bash
# Test database connection
python tests/db/test_connection.py

# Backup production data
python tests/db/backup_database.py --env production
```

### Test Coverage

Generate a coverage report:
```bash
coverage run -m pytest
coverage report -m
coverage html  # Generates HTML report in htmlcov/
```

## 🛠 Development

### Code Style

This project follows [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide. Use the following tools to maintain code quality:

```bash
# Auto-format code with Black
black src/

# Sort imports with isort
isort src/


# Check for common issues
flake8 src/
```

### Pre-commit Hooks

Install pre-commit hooks to automatically check your code before each commit:

```bash
pip install pre-commit
pre-commit install
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📫 Contact

For questions or feedback, please contact [Your Name] at [your.email@example.com]

---

<div align="center">
  <p>Made with ❤️ by Your Team</p>
  <p>Last updated: May 2025</p>
</div>

## Git Versions and Tags

| Tag                        | Commit ID | Description                                                      |
|----------------------------|-----------|------------------------------------------------------------------|
| V1.0.3c                    | 199fbea   | Enhanced git versions section of readme.md                       |
| V1.0.3b                    | 3720176   | Enhanced project documentation and organization                  |
| V1.0.3a                    | 8dad558   | Simplified Progress Tracking with Cookies                       |
| V1.0.2i                    | 83df59c   | Update Git Versions and Tags table for V1.0.2g and V1.0.2h      |
| V1.0.2h                    | e117a26   | Fixed Vercel Deployment                                         |
| V1.0.2g                    | 73c52a8   | Closed off on V1.0.2f                                           |
| V1.0.2f                    | ec791a6   | Built interactive training section                              |
| V1.0.2e                    | e4fefad   | Reviewed training content                                       |
| V1.0.2d                    | 041ff28   | Checked training content                                        |
| V1.0.2c                    | 1cbaaaa   | Tidied up readme.md                                             |
| V1.0.2a                    | 02c3bab   | V1.0.2: User Cookies Persistent session with UUID cookies       |
| V1.0.1b                    | bdf11c2   | Created planning documents for this project                     |
| V1.0.1a                    | b81eb11   | Added an admin page to manage database                          |
| V0.0.21                    | b5e31c9   | Integrate git commit history into Audit Trail section           |
| V0.0.20                    | fb70011   | Add Audit Trail section to README.md                            |
| V0.0.19                    | e2352de   | Fix file serving for Vercel deployment and rename hero image    |
| V0.0.18                    | c10629d   | Add Vercel deployment configuration                             |
| V0.0.17                    | 3783d3f   | Cleaned up database access                                      |
| V0.0.16                    | d3d64f4   | Update README with Flask setup and email verification           |
| V0.0.15                    | 4faf051   | User registration confirmation                                  |
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

The next version to be implemented is **V1.0.4**.

*This section should be auto-incremented as features are moved from backlog to planning/implementation. As versions are incremented, ensure the Audit Trail section is also updated with relevant information about the changes or features added in each version.*

## Audit Trail

### May 15, 2025
- **Simplified Progress Tracking with Cookies (V1.0.3):**
  - Redesigned the progress tracking system to use a simpler, more reliable counter-based approach.
  - Implemented reset of progress counters on each training page load for consistent user experience.
  - Created functions to increment section and quiz counters when users interact with content.
  - Updated cookie storage to use simple numeric values instead of complex data structures.
  - Ensured proper synchronization between client-side tracking and server-side database.
  - Improved visual feedback for users as they progress through training materials.
  - Fixed issues with section count not updating correctly in previous implementation.

### May 15, 2025
- **V1.0.3: Simplified Progress Tracking with Cookies**
  - Implemented a counter-based progress tracking system using cookies for training sections and quizzes, replacing the previous section-ID approach.
  - Counters reset on each training session for a consistent user experience.
  - Updated cookie storage to use simple numeric values (`smartchat_sections_viewed`, `smartchat_quizzes_completed`) for reliability and easier management.
  - Improved visual feedback for users and fixed prior issues with progress not updating correctly.
  - Simplified logic led to a more robust, consistent, and user-friendly tracking experience.

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
