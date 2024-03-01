import streamlit as st
import mysql.connector
import subprocess
# Function to create a MySQL connection
def create_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root12",
            database="MovieReg"
        )
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

# Function to authenticate a user
def authenticate_user(cursor, username, password):
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    return cursor.fetchone() is not None

# Streamlit login page
def login_page():
    st.title("User Login")

    # Input fields
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Providing unique keys to the st.button widgets
    login_button_key = "login_button"

    if st.button("Login", key=login_button_key):
        connection = create_connection()

        if connection:
            cursor = connection.cursor()

            if authenticate_user(cursor, username, password):
                st.success(f"Welcome, {username}!")

                # Run the other Python script using subprocess
                subprocess.run(["streamlit","run", "m1.py"])

                # Optionally, you can close the current Streamlit app
                st.stop()

            else:
                st.error("Invalid username or password. Please try again.")

            connection.close()


# Run the login page
if __name__ == "__main__":
    login_page()
