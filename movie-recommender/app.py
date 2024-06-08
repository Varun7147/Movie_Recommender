import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get('http://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list1 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for j in movies_list1:
        # movie_id = j[0]
        recommended_movies.append(movies_list.iloc[j[0]].id)
        # recommended_movies_posters.append(fetch_poster(movies_list.iloc[j[0]].id))
    return recommended_movies


similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = movies_list['title'].values
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'Pick a movie you liked',
    (movies)
)

movid = recommend(selected_movie_name)
poster_id = []
for i in range(5):
    poster_id.append(movies_list[movies_list['id'] == movid[i]].index[0])
# poster = []
# for i in poster_id:
#     poster.append(fetch_poster(i))
if st.button('Recommend'):
    for i in poster_id:
        st.write(movies_list['title'][i])
        # st.image(fetch_poster(i))