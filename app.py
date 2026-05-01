import streamlit as st
import pickle
import pandas as pd
import requests

# Function to get posters with error handling
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        # Adding a timeout of 5 seconds to prevent the app from freezing
        response = requests.get(url, timeout=5)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            # If no poster path exists in the database
            return "https://via.placeholder.com/500x750?text=No+Image+Found"
    except Exception:
        # If internet is disconnected or API is blocked, show a clean placeholder
        return "https://via.placeholder.com/500x750?text=Poster+Unavailable"

# Load the data
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    names = []
    posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))
    return names, posters

# UI Styling
st.set_page_config(page_title="Movie Matcher", layout="wide")
st.title('🎬 Movie Recommender System')
st.markdown("Select a movie you like, and we'll find 5 similar ones for you!")

selected_movie = st.selectbox('Type or select a movie:', movies['title'].values)

if st.button('Get Recommendations'):
    with st.spinner('Searching the database...'):
        names, posters = recommend(selected_movie)
        
        # Create 5 clean columns
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.write(f"**{names[i]}**")
                st.image(posters[i])