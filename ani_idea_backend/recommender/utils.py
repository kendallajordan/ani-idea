import random
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Dummy anime data with 'title' and 'genre' fields
ANIME_DATA = [
    {"title": "Naruto", "genre": "Action"},
    {"title": "One Piece", "genre": "Adventure"},
    {"title": "Attack on Titan", "genre": "Action"},
    {"title": "Death Note", "genre": "Thriller"},
    {"title": "My Hero Academia", "genre": "Action"},
    # Add more anime data here
]

def get_anime_vector(anime_title):
    # A simple vectorization based on genre (dummy logic)
    genre_dict = {
        "Action": [1, 0, 0, 0],
        "Adventure": [0, 1, 0, 0],
        "Thriller": [0, 0, 1, 0],
        # Add more genres as needed
    }
    for anime in ANIME_DATA:
        if anime["title"].lower() == anime_title.lower():
            return genre_dict.get(anime["genre"], [0, 0, 0, 0])
    return [0, 0, 0, 0]

def recommend_anime(titles):
    if len(titles) == 0:
        return []

    # Normalize input titles to lowercase for consistency
    normalized_titles = [title.lower() for title in titles]

    # Vectorize the input anime titles
    vectors = np.array([get_anime_vector(title) for title in normalized_titles])

    # Combine the vectors into a single vector by averaging them (representing collective preferences)
    collective_vector = np.mean(vectors, axis=0).reshape(1, -1)

    # Prepare the dataset for the recommendation process
    all_vectors = np.array([get_anime_vector(anime["title"]) for anime in ANIME_DATA])

    # Use a simple nearest neighbors approach to find similar anime (train algorithm with dataset)
    knn = NearestNeighbors(n_neighbors=min(5, len(ANIME_DATA)), algorithm='ball_tree')
    knn.fit(all_vectors)

    # Recommend anime based on the collective vector
    distances, indices = knn.kneighbors(collective_vector)

    recommended_titles = []
    for index in indices.flatten():
        recommended_title = ANIME_DATA[index]["title"]
        # Check if the recommended title is not in the input list (case insensitive)
        if recommended_title.lower() not in normalized_titles:
            recommended_titles.append(recommended_title)

    # Return unique recommendations
    return list(set(recommended_titles))

# Example of integrating the function with the views
def get_recommendations(titles):
    # Call the recommend_anime function with user input titles
    recommendations = recommend_anime(titles)
    return recommendations
