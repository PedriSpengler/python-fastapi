import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_connection():
    return psycopg2.connect(
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_DATABASE")
    )

def create_table():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE
            )
        """)
        conn.commit()
    finally:
        conn.close()

# INSERT A NEW USER IN THE TABLE (CREATE OPERATION)

def insert_user(username, email):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id",
            (username, email)
        )
        user_id = cursor.fetchone()[0]
        conn.commit()
        return user_id
    except psycopg2.Error as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

# RETRIEVE DATA FROM THE TABLE (READ OPERATION)

def read_users():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email FROM users")
        rows = cursor.fetchall()
        return [{"id": r[0], "username": r[1], "email": r[2]} for r in rows]
    finally:
        conn.close()

# UPDATE USER EMAIL (UPDATE OPERATION)

def update_user_email(username, new_email):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET email = %s WHERE username = %s",
            (new_email, username)
        )
        rows_affected = cursor.rowcount
        conn.commit()
        return rows_affected  # 0 = não achou o usuário, 1 = atualizou
    except psycopg2.Error as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

# DELETE USER (DELETE OPERATION)

def delete_user(username):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM users WHERE username = %s",
            (username,)
        )
        rows_affected = cursor.rowcount
        conn.commit()
        return rows_affected
    except psycopg2.Error as e:
        conn.rollback()
        raise e
    finally:
        conn.close()