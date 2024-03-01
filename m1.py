import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_img(movie_id):
    api_key = "e792017cec91c6964e70f3e510ebb445"
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=US'

    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')

    return "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else None

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    rec_movieIMG = [fetch_img(movies.iloc[i[0]].movie_id) for i in movies_list]
    return recommended_movies, rec_movieIMG

movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie :blue[Recommender] :movie_camera:')

Selected = st.selectbox(
    "Search Movies Here :point_down:",
    movies['title'].values,
    placeholder="Movies...",
)

if st.button('Recommend'):
    names, posters = recommend(Selected)

    for i in range(5):
        movie_id = movies[movies['title'] == names[i]].iloc[0]["movie_id"]
        with st.expander(f"{names[i]} - Watch Now"):
            st.image(posters[i])

            Info = f'For Movie Info :point_down: :'
            st.markdown(Info, unsafe_allow_html=True)
            # HTML links to streaming platforms that open in a new tab
            tmdb_link = f'<a href="https://www.themoviedb.org/movie/{movie_id}" target="_blank">TMDB - {names[i]}</a>'
            st.markdown(tmdb_link, unsafe_allow_html=True)

            Watch = f'To Watch Movies Link :point_down: :'
            st.markdown(Watch, unsafe_allow_html=True)
            netflix_link = f'<a href="https://www.netflix.com/in/title/{names[i]}" target="_blank">Netflix - {names[i]}</a>'
            st.markdown(netflix_link, unsafe_allow_html=True)

            hotstar_link = f'<a href="https://www.hotstar.com/in/explore?search_query={names[i]}" target="_blank">Hotstar - {names[i]}</a>'
            st.markdown(hotstar_link, unsafe_allow_html=True)

            prime_link = f'<a href="https://www.primevideo.com/search/ref=atv_sr_sug_nb_sb_ss_i_5_10?phrase={names[i]}" target="_blank">Prime Video - {names[i]}</a>'
            st.markdown(prime_link, unsafe_allow_html=True)

            soap2day_link = f'<a href="https://ww8.soap2dayhd.co/search/?q={names[i]}" target="_blank">Soap2Day - {names[i]}</a>'
            st.markdown(soap2day_link, unsafe_allow_html=True)
