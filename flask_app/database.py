"""
Database models and setup for user authentication and data storage
"""

import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import json

DATABASE = 'mental_health_screening.db'


def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize database with tables"""
    conn = get_db()
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP
        )
    ''')

    # Screening responses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS screening_responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            responses TEXT NOT NULL,
            risk_result TEXT NOT NULL,
            routing TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()
    conn.close()


# ============================================================================
# USER FUNCTIONS
# ============================================================================

def create_user(email, password, first_name=None, last_name=None):
    """Create a new user"""
    try:
        conn = get_db()
        cursor = conn.cursor()

        password_hash = generate_password_hash(password)

        cursor.execute('''
            INSERT INTO users (email, password_hash, first_name, last_name)
            VALUES (?, ?, ?, ?)
        ''', (email, password_hash, first_name, last_name))

        conn.commit()
        user_id = cursor.lastrowid
        conn.close()

        return user_id
    except sqlite3.IntegrityError:
        return None  # User already exists


def get_user_by_email(email):
    """Get user by email"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()

    conn.close()
    return dict(user) if user else None


def get_user_by_id(user_id):
    """Get user by ID"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()

    conn.close()
    return dict(user) if user else None


def verify_password(email, password):
    """Verify user password"""
    user = get_user_by_email(email)
    if user and check_password_hash(user['password_hash'], password):
        return user
    return None


def update_last_login(user_id):
    """Update user's last login timestamp"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE users
        SET last_login = ?
        WHERE id = ?
    ''', (datetime.now(), user_id))

    conn.commit()
    conn.close()


# ============================================================================
# SCREENING RESPONSE FUNCTIONS
# ============================================================================

def save_screening_response(user_id, responses, risk_result, routing):
    """Save a screening response for a user"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO screening_responses (user_id, responses, risk_result, routing)
        VALUES (?, ?, ?, ?)
    ''', (
        user_id,
        json.dumps(responses),
        json.dumps(risk_result),
        json.dumps(routing)
    ))

    conn.commit()
    response_id = cursor.lastrowid
    conn.close()

    return response_id


def get_user_screening_history(user_id):
    """Get all screening responses for a user"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM screening_responses
        WHERE user_id = ?
        ORDER BY created_at DESC
    ''', (user_id,))

    responses = cursor.fetchall()
    conn.close()

    # Parse JSON fields
    result = []
    for response in responses:
        result.append({
            'id': response['id'],
            'user_id': response['user_id'],
            'responses': json.loads(response['responses']),
            'risk_result': json.loads(response['risk_result']),
            'routing': json.loads(response['routing']),
            'created_at': response['created_at']
        })

    return result


def get_latest_screening(user_id):
    """Get user's most recent screening"""
    history = get_user_screening_history(user_id)
    return history[0] if history else None


def get_all_screening_responses():
    """Get all screening responses (for analytics)"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM screening_responses ORDER BY created_at DESC')
    responses = cursor.fetchall()
    conn.close()

    # Parse JSON fields
    result = []
    for response in responses:
        result.append({
            'timestamp': response['created_at'],
            'responses': json.loads(response['responses']),
            'risk_result': json.loads(response['risk_result']),
            'routing': json.loads(response['routing'])
        })

    return result


# ============================================================================
# STATISTICS FUNCTIONS
# ============================================================================

def get_user_stats(user_id):
    """Get statistics for a specific user"""
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) as total_screenings,
               MIN(created_at) as first_screening,
               MAX(created_at) as last_screening
        FROM screening_responses
        WHERE user_id = ?
    ''', (user_id,))

    stats = cursor.fetchone()
    conn.close()

    return dict(stats) if stats else None
