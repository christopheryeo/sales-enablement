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

@app.route('/check_registration', methods=['GET', 'POST'])
def check_registration():
    """Handles user registration check.
    GET: Shows the registration form.
    POST: Checks email against the database.
    """
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            flash('Email is required.', 'error')
            return redirect(url_for('check_registration'))

        conn = get_db_connection()
        if conn:
            try:
                with conn.cursor() as cur:
                    # Use the table name confirmed by the test script
                    cur.execute("SELECT email FROM email_registrations WHERE email = %s", (email,))
                    user = cur.fetchone()

                if user:
                    # Email found, mark session as registered and redirect to training
                    session['registered'] = True
                    session['user_email'] = email # Store email for potential future use
                    flash(f"Welcome, {email}! Access granted.", "success")
                    return redirect(url_for('training'))
                else:
                    # Email not found
                    flash('Email address not found in our records. Please contact support.', 'error')
                    return redirect(url_for('check_registration')) # Redirect back to form
            except Exception as e:
                print(f"Database query error: {e}")
                flash("An error occurred while checking your email. Please try again later.", "error")
                return redirect(url_for('check_registration'))
            finally:
                if conn:
                    conn.close()
        else:
            # Error connecting to DB already handled by get_db_connection
            return redirect(url_for('check_registration'))

    # GET request: show the registration form
    return render_template('register.html')

@app.route('/training')
def training():
    """Displays the training page, only if the user is marked as registered in the session."""
    if session.get('registered'):
        # User is registered, render index.html with training visible
        return render_template('index.html', show_training=True)
    else:
        # User not registered or session expired
        flash('You must verify your email to access the training.', 'warning')
        return redirect(url_for('check_registration'))

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
