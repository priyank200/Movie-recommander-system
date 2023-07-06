# Movie-recommender-system
this app is help us to recommend movies using content-based filtering. It is done using the Kaggle TMDB dataset.
# INTRODUCTION
The purpose of this report is to provide an overview of the development and implementation of a movie recommendation system using the TMDB dataset. The objective was to create a personalized recommendation system that assists users in discovering movies based on their individual preferences and interests. This report will outline the data preprocessing techniques, similarity calculations, and web application development used to achieve this goal.

# DATA – PREPROCESSING
1.	Libraries such as pandas, scikit-learn, and NLTK were used to handle data manipulation, vectorization, and text processing tasks.
2.	The movie descriptions were transformed into numerical vectors using the CountVectorizer class. This technique allowed the system to capture the presence of words in the movie descriptions, enabling further analysis
3.	To expand the range of word variations considered during vectorization, stemming techniques were applied. This step ensured that variations of the same word were considered identical, resulting in more comprehensive representations of the movie descriptions

# SIMILARITY CALCULATION
To determine the similarity between movies and enable accurate recommendations, cosine similarity was utilized. The following steps were undertaken:
•	Cosine Similarity: By calculating the cosine distance between the movie vectors, the similarity between all pairs of movies was quantified. This measure allowed for the identification of movies that shared similar characteristics, enabling personalized and relevant recommendations based on user preferences.

# WEB APPLICATION
To showcase the movie recommendation system, a user-friendly web application was created. The following technologies were used:
1.	Pickle: The trained recommendation model was serialized using the Pickle library, allowing for easy loading and usage in the web application.
2.	Streamlit: An interactive website was developed to provide seamless movie recommendations to users. The web application was designed to be intuitive and user-friendly, ensuring an engaging user experience.
3.	TMDB API Integration: The TMDB API was leveraged to fetch movie posters, enriching the visual experience and enabling users to make informed choices about the movies they wished to explore further.

# CONCLUSION
The development of the movie recommendation system using the TMDB dataset successfully achieved the goal of providing personalized movie recommendations to users. Through comprehensive data preprocessing, cosine similarity calculations, and web application development, an accurate and user-friendly recommendation system was created. The system showcased the potential of leveraging advanced techniques and technologies to enhance the movie discovery experience for users

