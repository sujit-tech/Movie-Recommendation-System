import streamlit as st
from Register import registration_page
from Login import login_page
def main():
    st.title("Movie :blue[Recommender] :movie_camera:")
    st.write("Welcome to the Movie :blue[Recommender] :pray:")

    # Add some space between the welcome message and buttons
    st.write("\n\n")

    # Create buttons for Register and Login
    if st.button("Register"):
        st.session_state.page = "register"

    if st.button("Login"):
        st.session_state.page = "login"

    if hasattr(st.session_state, 'page'):
        if st.session_state.page == "register":
            registration_page()
        elif st.session_state.page == "login":
            login_page()


if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = "main"
    main()
