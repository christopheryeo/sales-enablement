import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from dotenv import load_dotenv
import secrets # For generating a secret key if not set

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- Configuration ---
# Secret key for session management.
# IMPORTANT: Set a strong, secret key in your environment variables for production.
# For development, we can generate one if not found.
app.secret_key = os.environ.get('FLASK_SECRET_KEY', secrets.token_hex(16))
DATABASE_URL = os.environ.get('AIVEN_DB_URI') # Use the correct key from .env

if not DATABASE_URL:
    print("Error: AIVEN_DB_URI environment variable not set.") # Update error message
    # Depending on requirements, you might want to exit or provide a default
    # For now, we'll print an error and continue, but DB operations will fail.

# --- Database Helper ---
def get_db_connection():
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        flash(f"Database connection error: {e}", "error")
        return None

# --- Routes ---
@app.route('/')
def home():
    """Renders the main page (index.html) without the training section initially visible."""
    # Pass show_training=False so the Jinja template hides the training section
    return render_template('index.html', show_training=False)

@app.route('/training', methods=['GET', 'POST'])
def training():
    """Handles registration (if POST) and displays training page for registered users."""
    if request.method == 'POST':
        email = request.form.get('email')
        organisation = request.form.get('organisation')
        if not email or not organisation:
            flash('Email and Organisation are required to register.', 'error')
            return render_template('register.html')
        conn = get_db_connection()
        if conn:
            try:
                with conn.cursor() as cur:
                    # Use correct column name with proper casing
                    cur.execute(
                        "INSERT INTO email_registrations (email, \"Organisation\") VALUES (%s, %s)\n"
                        "ON CONFLICT (email) DO UPDATE SET \"Organisation\" = EXCLUDED.\"Organisation\" RETURNING id;",
                        (email, organisation)
                    )
                    conn.commit()
                session['registered'] = True
                session['user_email'] = email
                session['organisation'] = organisation
                flash(f"Welcome, {email}! Access granted.", 'success')
            except Exception as e:
                print(f"Error during registration: {e}")
                flash('Registration failed. Please try again.', 'error')
            finally:
                conn.close()
        return render_template('index.html', show_training=True)
    # GET request
    if session.get('registered'):
        return render_template('index.html', show_training=True)
    return render_template('register.html')

@app.route('/logout')
def logout():
    """Logs the user out by clearing the session."""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

# Note: Flask automatically serves the 'static' folder at /static
# If index.html needs to fetch content.md client-side, we might need a route for it:
@app.route('/content/<path:filename>')
def serve_content(filename):
    """Serves files from the content directory."""
    return send_from_directory('content', filename)


if __name__ == '__main__':
    # Use debug=True for development; it enables auto-reloading and detailed error pages.
    # Set host='0.0.0.0' to make the server accessible on your network.
    app.run(debug=True, host='0.0.0.0', port=8000) # Changed port to 8000
