from multiprocessing import connection

import psycopg2
from dotenv import load_dotenv
import os   

load_dotenv()

# CREATE A CONNECTION TO THE POSTGRESQL DATABASE

def connect_to_database():
    try:
        connection = psycopg2.connect(
            user=os.getenv("DB_USERNAME"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_DATABASE")
        )
        print("Connection to the database was successful!")
        return connection

    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL:", e)
        return None

# CREATE A NEW TABLE IN THE DATABASE

def create_table(connection):

    try:
        cursor = connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE
        )
        """
        cursor.execute(create_table_query)
        print("Table 'users' created successfully!")

    except psycopg2.Error as e:
        print("Error while creating the table:", e)

# INSERT A NEW USER IN THE TABLE (CREATE OPERATION)

def insert_user(connection, username, email):
    try:
        cursor = connection.cursor()

        insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        users_data = (username, email)

        cursor.execute(insert_query, users_data)
        connection.commit()
        print("Data inserted successfully into the 'users' table!")

    except psycopg2.Error as e:
        print("Error while inserting data into the table:", e)

# RETRIEVE DATA FROM THE TABLE (READ OPERATION)

def read_users(connection):
    try:
        cursor = connection.cursor()

        select_query = "SELECT * FROM users"

        cursor.execute(select_query)

        for row in cursor:
            print(f"ID: {row[0]}, Username: {row[1]}, Email: {row[2]}")

    except psycopg2.Error as e:
        print("Error while retrieving data from the table:", e)

# UPDATE DATA IN THE TABLE (UPDATE OPERATION)

def update_user_email(connection, username, new_email):
    try:
        cursor = connection.cursor()

        update_query = "UPDATE users SET email = %s WHERE username = %s"
        user_data = (new_email, username)

        cursor.execute(update_query, user_data)
        connection.commit()
        print(f"Data updated successfully for user '{username}' in the 'users' table!")

    except psycopg2.Error as e:
        print("Error while updating data in the table:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()

# DELETE DATA FROM THE TABLE (DELETE OPERATION)

def delete_user(connection, username):
    try:
        cursor = connection.cursor()

        delete_query = "DELETE FROM users WHERE username = %s"
        user_data = (username,)
        cursor.execute(delete_query, user_data)
        connection.commit()
        print(f"Data deleted successfully for user '{username}' from the 'users' table!")

    except psycopg2.Error as e:
        print("Error while deleting data from the table:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()

if __name__ == "__main__":
    connection = connect_to_database()
    if connection:
        create_table(connection)
        insert_user(connection, "junior", "jrmoci@example.com")
        read_users(connection)