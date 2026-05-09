import mysql.connector
from mysql.connector import Error

import streamlit as st

host = st.secrets["DB_HOST"]
user = st.secrets["DB_USER"]
password = st.secrets["DB_PASSWORD"]
db = st.secrets["DB_NAME"]

def get_connection():
    """Return a new database connection."""
    return mysql.connector.connect(use_pure=True, **DB_CONFIG)

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params or ())
        conn.commit()
        return True
    except Error as e:
        print(f"DB Error: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

def fetch_all(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        return cursor.fetchall()
    except Error as e:
        print(f"DB Error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def fetch_one(query, params=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        return cursor.fetchone()
    except Error as e:
        print(f"DB Error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()
