# import streamlit as st
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import difflib

# # App title
# st.title("Movie Recommendation System")

# # File upload
# # movies_file_available=st.text_input("Enter yes if you have movie file or Enter no if you don't have:", placeholder="Y/N").strip().lower()

# # if movies_file_available=="yes":
# #     uploaded_file = st.file_uploader("Upload a movies CSV file if you have some movie file", type=["csv"])
# # else:
# #     uploaded_file="/workspaces/movie_recommendation_system/movies.csv"

# if uploaded_file:
#     # Load the dataset
#     try:
#         movies_data = pd.read_csv(uploaded_file)
#         st.write("File uploaded successfully!")
#         st.dataframe(movies_data.head())

#         # Check required columns
#         required_columns = ['title', 'genres', 'keywords', 'tagline', 'cast', 'director']
#         if all(col in movies_data.columns for col in required_columns):
#             # Preprocessing
#             selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
#             for feature in selected_features:
#                 movies_data[feature] = movies_data[feature].fillna("")
            
#             # Combine features into a single string
#             combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + \
#                                 movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']
            
#             # Convert text data to feature vectors
#             vectorizer = TfidfVectorizer()
#             feature_vectors = vectorizer.fit_transform(combined_features)
            
#             # Calculate similarity scores
#             similarity = cosine_similarity(feature_vectors)

#             # Input movie name
#             movie_name = st.text_input("Enter a movie name to get recommendations:")

#             if movie_name:
#                 # Find a close match
#                 list_of_all_titles = movies_data['title'].tolist()
#                 close_match = difflib.get_close_matches(movie_name, list_of_all_titles, n=1)

#                 if close_match:
#                     closest_match = close_match[0]
#                     st.write(f"Closest match found: {closest_match}")

#                     # Get the index of the matched movie
#                     movie_index = movies_data[movies_data.title == closest_match].index[0]

#                     # Get similarity scores for the movie
#                     similarity_scores = list(enumerate(similarity[movie_index]))
#                     sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

#                     # Display top 10 similar movies
#                     st.subheader("Top Recommendations:")
#                     for i, (index, score) in enumerate(sorted_movies[1:11], start=1):
#                         st.write(f"{i}. {movies_data.iloc[index]['title']}")
#                 else:
#                     st.write("No close match found. Please try another movie name.")
#         else:
#             st.error("The uploaded CSV does not contain the required columns!")
#     except Exception as e:
#         st.error(f"An error occurred: {e}")
# else:
#     st.write("Please upload a CSV file to proceed.")

# import streamlit as st
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import difflib

# import requests

# def get_movie_poster(movie_name, api_key="2d2138d81246f496bae564f66ed0d316"):
#     base_url = "https://api.themoviedb.org/3/search/movie"
#     params = {"query": movie_name, "api_key": api_key}
#     response = requests.get(base_url, params=params).json()
#     if response['results']:
#         movie = response['results'][0]  # Get the first search result
#         poster_path = movie['poster_path']
#         poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
#         return poster_url
#     return None

# # # Example usage
# # poster = get_movie_poster("Inception", api_key="2d2138d81246f496bae564f66ed0d316")
# # if poster:
# #     st.image(poster, caption="Inception", width=200)


# # App title
# st.title("Movie Recommendation System")

# # File upload
# uploaded_file = st.file_uploader("Upload a movies CSV file", type=["csv"])

# if uploaded_file:
#     # Load the dataset
#     try:
#         movies_data = pd.read_csv(uploaded_file)
#         st.write("File uploaded successfully!")
#         st.dataframe(movies_data.head())

#         # Check required columns
#         required_columns = ['title', 'genres', 'keywords', 'tagline', 'cast', 'director']
#         if all(col in movies_data.columns for col in required_columns):
#             # Preprocessing
#             selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
#             for feature in selected_features:
#                 movies_data[feature] = movies_data[feature].fillna("")
            
#             # Combine features into a single string
#             combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + \
#                                 movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']
            
#             # Convert text data to feature vectors
#             vectorizer = TfidfVectorizer()
#             feature_vectors = vectorizer.fit_transform(combined_features)
            
#             # Calculate similarity scores
#             similarity = cosine_similarity(feature_vectors)

#             # Input movie name
#             movie_name = st.text_input("Enter a movie name to get recommendations:")

#             if movie_name:
#                 # Find a close match
#                 list_of_all_titles = movies_data['title'].tolist()
#                 close_match = difflib.get_close_matches(movie_name, list_of_all_titles, n=1)

#                 if close_match:
#                     closest_match = close_match[0]
#                     st.write(f"Closest match found: {closest_match}")

#                     # Get the index of the matched movie
#                     movie_index = movies_data[movies_data.title == closest_match].index[0]

#                     # Get similarity scores for the movie
#                     similarity_scores = list(enumerate(similarity[movie_index]))
#                     sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

#                     # Display top 10 similar movies
#                     st.subheader("Top Recommendations:")
#                     for i, (index, score) in enumerate(sorted_movies[1:31], start=1):
#                         st.write(f"{i}. {movies_data.iloc[index]['title']}")
#                         movie_title = movies_data.iloc[index]['title']
#                         poster_url = get_movie_poster(movie_title, api_key="2d2138d81246f496bae564f66ed0d316")
#                         if poster_url:
#                             col1, col2 = st.columns([1, 5])  # Adjust the column ratio for layout
#                             with col1:
#                                 st.image(poster_url, caption=movie_title, width=100)
#                             with col2:
#                                 st.write(f"**{i}. {movie_title}**")
#                         else:
#                             st.write(f"**{i}. {movie_title}** (Poster not available)")
#                 else:
#                     st.write("No close match found. Please try another movie name.")
#         else:
#             st.error("The uploaded CSV does not contain the required columns!")
#     except Exception as e:
#         st.error(f"An error occurred: {e}")
# else:
#     st.write("Please upload a CSV file to proceed.")

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib
import requests

def get_movie_poster(movie_name, api_key="2d2138d81246f496bae564f66ed0d316"):
    base_url = "https://api.themoviedb.org/3/search/movie"
    params = {"query": movie_name, "api_key": api_key}
    response = requests.get(base_url, params=params).json()
    if response['results']:
        movie = response['results'][0]  # Get the first search result
        poster_path = movie['poster_path']
        poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return poster_url
    return None

def get_trailer_link(movie_name, api_key="2d2138d81246f496bae564f66ed0d316"):
    base_url = f"https://api.themoviedb.org/3/search/movie"
    params = {"query": movie_name, "api_key": api_key}
    response = requests.get(base_url, params=params).json()
    if response['results']:
        movie = response['results'][0]  # Get the first search result
        movie_id = movie['id']
        
        # Fetch trailer info using the movie ID
        trailer_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={api_key}&language=en-US"
        trailer_response = requests.get(trailer_url).json()
        if trailer_response['results']:
            trailer_key = trailer_response['results'][0]['key']
            return f"https://www.youtube.com/watch?v={trailer_key}"
    return None

# App title
st.title("Movie Recommendation System")

# File upload
movies_file_available=st.text_input("Enter yes if you have movie file or Enter no if you don't have:", placeholder="Y/N").strip().lower()

if movies_file_available=="yes":
    uploaded_file = st.file_uploader("Upload a movies CSV file if you have some movie file", type=["csv"])
else:
    uploaded_file="movies.csv"

# uploaded_file = st.file_uploader("Upload a movies CSV file", type=["csv"])

if uploaded_file:
    # Load the dataset
    try:
        movies_data = pd.read_csv(uploaded_file)
        st.write("File uploaded successfully!")
        st.dataframe(movies_data.head())

        # Check required columns
        required_columns = ['title', 'genres', 'keywords', 'tagline', 'cast', 'director']
        if all(col in movies_data.columns for col in required_columns):
            # Preprocessing
            selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
            for feature in selected_features:
                movies_data[feature] = movies_data[feature].fillna("")
            
            # Combine features into a single string
            combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + \
                                movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']
            
            # Convert text data to feature vectors
            vectorizer = TfidfVectorizer()
            feature_vectors = vectorizer.fit_transform(combined_features)
            
            # Calculate similarity scores
            similarity = cosine_similarity(feature_vectors)

            # Input movie name
            movie_name = st.text_input("Enter a movie name to get recommendations:")

            if movie_name:
                # Find a close match
                list_of_all_titles = movies_data['title'].tolist()
                close_match = difflib.get_close_matches(movie_name, list_of_all_titles, n=1)

                if close_match:
                    closest_match = close_match[0]
                    st.write(f"Closest match found: {closest_match}")

                    # Get the index of the matched movie
                    movie_index = movies_data[movies_data.title == closest_match].index[0]

                    # Get similarity scores for the movie
                    similarity_scores = list(enumerate(similarity[movie_index]))
                    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

                    # Display top 10 similar movies with posters linked to trailers
                    st.subheader("Top Recommendations:")

                    for i, (index, score) in enumerate(sorted_movies[1:31], start=1):
                        movie_title = movies_data.iloc[index]['title']
                        poster_url = get_movie_poster(movie_title, api_key="2d2138d81246f496bae564f66ed0d316")
                        trailer_link = get_trailer_link(movie_title, api_key="2d2138d81246f496bae564f66ed0d316")

                        # Display movie poster as clickable link to trailer
                        if poster_url and trailer_link:
                            col1, col2 = st.columns([1, 5])  # Adjust column ratios for layout
                            with col1:
                                st.markdown(f"[![{movie_title}]({poster_url})]({trailer_link})", unsafe_allow_html=True)
                            with col2:
                                st.write(f"**{i}. {movie_title}**")
                        else:
                            st.write(f"**{i}. {movie_title}** (Poster or trailer not available)")
                else:
                    st.write("No close match found. Please try another movie name.")
        else:
            st.error("The uploaded CSV does not contain the required columns!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please upload a CSV file to proceed.")

