import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

# App title
st.title("Movie Recommendation System")

# File upload
uploaded_file = st.file_uploader("Upload a movies CSV file", type=["csv"])

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

                    # Display top 10 similar movies
                    st.subheader("Top Recommendations:")
                    for i, (index, score) in enumerate(sorted_movies[1:11], start=1):
                        st.write(f"{i}. {movies_data.iloc[index]['title']}")
                else:
                    st.write("No close match found. Please try another movie name.")
        else:
            st.error("The uploaded CSV does not contain the required columns!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please upload a CSV file to proceed.")
