import streamlit as st
import pickle
import pandas as pd
import  requests

def photo_fetch(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}'
                 '?api_key=f76cf85605f195019d2161a65918de3a&language=en-US'.format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    print(poster_path)
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


#function to recommend top 5 similar movies
def recommended(name):
    movie_index = movie[movie["title"] == name].index[0]
    vector = similarity[movie_index]
    distances = sorted(list(enumerate(vector)),reverse=True,key = lambda x: x[1])[1:6]
    recommended_name = []
    recommended_name_poster = []
    for i in distances:
        recommended_name.append(movie.iloc[i[0]].title)
        # fetch the path of photo
        movie_id = movie.iloc[i[0]].id
        recommended_name_poster.append(photo_fetch(movie_id))
    return recommended_name,recommended_name_poster

similarity = pickle.load(open("similarity.pkl",'rb'))

movie_dict = pickle.load(open("movie_dict.pkl",'rb'))
movie = pd.DataFrame(movie_dict)
# print(movie)

st.markdown("<h1 style='text-align: center; color: white;'>Movie Recommender System</h1>", unsafe_allow_html=True)
# st.title("<h1 style='text-align: center; color: grey;'>Movie Recommander System :sunglasses:</h1>",unsafe)
# sentence = st.text_input('Enter Movie name:')
box = st.selectbox("Enter Movie Name",movie["title"].values)

if st.button('Recommend'):
    name,poster = recommended(box)

    with st.expander(name[0]):
        st.image(poster[0],width=200)

    with st.expander(name[1]):
        st.image(poster[1],width=200)

    with st.expander(name[2]):
        st.image(poster[2],width=200)

    with st.expander(name[3]):
        st.image(poster[3],width=200)

    with st.expander(name[4]):
        st.image(poster[4],width=200)

    #Different ways to display

    # tab1, tab2, tab3, tab4, tab5 = st.tabs(name)
    #
    # with tab1:
    #     st.text(name[0])
    #     st.image(poster[0], width=200)
    #
    # with tab2:
    #     st.text(name[1])
    #     st.image(poster[1], width=200)
    #
    # with tab3:
    #     st.text(name[2])
    #     st.image(poster[2], width=200)
    #
    # with tab4:
    #     st.text(name[3])
    #     st.image(poster[3], width=200)
    #
    # with tab5:
    #     st.text(name[4])
    #     st.image(poster[4], width=200)


    # col1, col2, col3, col4, col5 = st.columns(5,gap = 'medium')
    # with col1:
    #     st.text(name[0])
    #     st.image(poster[0])
    # with col2:
    #     st.text(name[1])
    #     st.image(poster[1])
    #
    # with col3:
    #     st.text(name[2])
    #     st.image(poster[2])
    # with col4:
    #     st.text(name[3])
    #     st.image(poster[3])
    # with col5:
    #     st.text(name[4])
    #     st.image(poster[4])
