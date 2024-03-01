import streamlit as st
import mysql.connector

# Function to create a MySQL connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root12",
        database="MovieReg"
    )

# Function to create a table if it doesn't exist
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)

# Function to insert a new user into the database
def insert_user(cursor, username, password):
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    st.success("User registered successfully!")

# Function to check if a username already exists
def username_exists(cursor, username):
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    return cursor.fetchone() is not None

# Streamlit registration page
def registration_page():
    st.title("User Registration")

    # Input fields
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    confirm_password = st.text_input("Confirm Password:", type="password")

    # Providing unique keys to the st.button widgets
    register_button_key = "register_button"

    if st.button("Register", key=register_button_key):
        if password == confirm_password:
            connection = create_connection()
            cursor = connection.cursor()

            create_table(cursor)

            if not username_exists(cursor, username):
                insert_user(cursor, username, password)
            else:
                st.error("Username already exists. Please choose a different one.")

            connection.commit()
            connection.close()

# Run the registration page
if __name__ == "__main__":
    registration_page()
