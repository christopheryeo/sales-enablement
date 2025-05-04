import os
import psycopg2
import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory, jsonify, make_response
import uuid  # For generating session UUIDs
from dotenv import load_dotenv
import secrets # For generating a secret key if not set
import json # For handling JSON data

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
    # User Session Cookie logic (V.1.0.2)
    session_id = request.cookies.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        resp = make_response(render_template('index.html', show_training=False))
        resp.set_cookie('session_id', session_id, httponly=True, secure=True, samesite='Lax')
        # Optionally: log or use session_id for backend logic here
        return resp
    # Optionally: validate session_id format here
    # Optionally: use session_id for backend logic here
    return render_template('index.html', show_training=False)

@app.route('/training', methods=['GET', 'POST'])
def training():
    """Handles registration (if POST) and displays training page for registered users."""
    # User Session Cookie logic (V.1.0.2)
    session_id = request.cookies.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        resp = make_response(render_template('index.html', show_training=True))
        resp.set_cookie('session_id', session_id, httponly=True, secure=True, samesite='Lax')
        return resp
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
        print(f"[DEBUG] POST /training session: {dict(session)} | show_training=True")
        return render_template('index.html', show_training=True)
    # GET request
    if session.get('registered'):
        print(f"[DEBUG] GET /training session: {dict(session)} | show_training=True")
        return render_template('index.html', show_training=True)
    print(f"[DEBUG] GET /training session: {dict(session)} | show_training=False (showing register)")
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

# Add explicit route for static files to ensure they work in Vercel's serverless environment
@app.route('/static/<path:filename>')
def serve_static(filename):
    """Explicitly serve files from the static directory."""
    return send_from_directory('static', filename)

# Admin route to view user progress statistics

@app.route('/admin/clear', methods=['POST'])
def clear_records():
    # Only allow if admin
    if session.get('user_email') not in ['christopher.yeo@gmail.com', 'chris@sentient.com']:
        flash('Unauthorized', 'error')
        return redirect(url_for('admin'))
    conn = get_db_connection()
    if not conn:
        flash('Database connection error', 'error')
        return redirect(url_for('admin'))
    try:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM email_registrations;')
            conn.commit()
        flash('All records deleted.', 'success')
    except Exception as e:
        flash(f'Error deleting records: {e}', 'error')
    finally:
        conn.close()
    return redirect(url_for('admin'))
@app.route('/admin')
def admin():
    """Admin page to view user progress statistics."""
    # For a real application, you would add authentication here
    # For this demo, we'll just display the data
    
    conn = get_db_connection()
    if not conn:
        flash('Database connection error', 'error')
        return redirect(url_for('home'))
    
    try:
        with conn.cursor() as cur:
            # Get all users with their progress
            cur.execute("""
                SELECT email, "Organisation", sections_completed, quizzes_completed, last_active 
                FROM email_registrations 
                ORDER BY last_active DESC
            """)
            users_data = cur.fetchall()
            
            # Get total counts
            cur.execute("""
                SELECT 
                    COUNT(*) as total_users,
                    SUM(sections_completed) as total_sections,
                    SUM(quizzes_completed) as total_quizzes
                FROM email_registrations
            """)
            totals = cur.fetchone()
            
            # Format the data for the template
            users = []
            for user in users_data:
                users.append({
                    'email': user[0],
                    'organisation': user[1],
                    'sections_completed': user[2],
                    'quizzes_completed': user[3],
                    'last_active': user[4].strftime('%Y-%m-%d %H:%M:%S') if user[4] else 'Never'
                })
            
            total_users = totals[0] if totals else 0
            total_sections = totals[1] if totals else 0
            total_quizzes = totals[2] if totals else 0
            
            return render_template('admin.html', 
                                 users=users, 
                                 total_users=total_users, 
                                 total_sections=total_sections, 
                                 total_quizzes=total_quizzes)
    except Exception as e:
        print(f"Error in admin page: {e}")
        flash(f'Error: {e}', 'error')
        return redirect(url_for('home'))
    finally:
        conn.close()

# Add route for tracking user progress
@app.route('/track_progress', methods=['POST'])
def track_progress():
    """Track user progress with training sections and quizzes."""
    # Check if user is registered
    if not session.get('registered'):
        return jsonify({'status': 'error', 'message': 'User not registered'}), 401
    
    # Get user email from session
    email = session.get('user_email')
    
    # Get progress data from request
    if not request.is_json:
        return jsonify({'status': 'error', 'message': 'Request must be JSON'}), 400
    
    data = request.get_json()
    progress_type = data.get('type')  # 'section' or 'quiz'
    
    if progress_type not in ['section', 'quiz']:
        return jsonify({'status': 'error', 'message': 'Invalid progress type'}), 400
    
    # Connect to database
    conn = get_db_connection()
    if not conn:
        return jsonify({'status': 'error', 'message': 'Database connection error'}), 500
    
    try:
        with conn.cursor() as cur:
            # Get current progress values
            cur.execute(
                "SELECT sections_completed, quizzes_completed FROM email_registrations WHERE email = %s",
                (email,)
            )
            result = cur.fetchone()
            
            if not result:
                return jsonify({'status': 'error', 'message': 'User not found'}), 404
            
            sections_completed, quizzes_completed = result
            
            # Update progress based on type
            if progress_type == 'section':
                sections_completed += 1
                update_column = 'sections_completed'
                new_value = sections_completed
            else:  # quiz
                quizzes_completed += 1
                update_column = 'quizzes_completed'
                new_value = quizzes_completed
            
            # Update database
            cur.execute(
                f"UPDATE email_registrations SET {update_column} = %s, last_active = CURRENT_TIMESTAMP WHERE email = %s",
                (new_value, email)
            )
            conn.commit()
            
            return jsonify({
                'status': 'success', 
                'message': f'{progress_type.capitalize()} progress updated',
                'sections_completed': sections_completed,
                'quizzes_completed': quizzes_completed
            })
    except Exception as e:
        print(f"Error tracking progress: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500
    finally:
        conn.close()


if __name__ == '__main__':
    # Use debug=True for development; it enables auto-reloading and detailed error pages.
    # Set host='0.0.0.0' to make the server accessible on your network.
    app.run(debug=True, host='0.0.0.0', port=8000) # Changed port to 8000
