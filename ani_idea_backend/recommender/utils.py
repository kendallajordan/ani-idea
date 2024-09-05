import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from collections import defaultdict

# Load the anime dataset
def load_anime_dataset():
    csv_path = "recommender/datasets/anime_dataset_2023.csv"
    df = pd.read_csv(csv_path)
    return df

# Step 1: Load the dataset and combine features
anime_df = load_anime_dataset()
# SYNOPSIS LIMITATION IS THAT CHARACTER NAMES HUGELY AFFECT SIMILARITY_SCORES (will recommend anime with characters that share same name)
# Learn if possible to merge datasets (give 2022 dataset's tag columns to 2023 dataset somehow (same name?))
#anime_df['Text Description'] = anime_df['Synopsis'] + ' ' + anime_df['Genres']
anime_df['Text Description'] = anime_df['Genres']
anime_df['Text Description'] = anime_df['Text Description'].fillna('')

# Step 2: Create the TF-IDF matrix (row: Text description, col: every unique word across all text descriptions | N X M)
# Highlights the most important words of each description, giving more value to unique words and less to common ones
# Gives each anime's text description a quantifiable, numerical form
# Anime's Vector Index corresponds to its Dataset Index
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(anime_df['Text Description'])

# Step 3: Compute the cosine similarity matrix
# Compares vectors (quantifiable numbers) of every anime with every other anime in the dataset including itself (N X N Matrix)
# Used to measure how similar two anime are based on their vectors (text descriptions)
# Row: ith anime | Col: (jth anime, similarity_score)
# Anime's Cos-Sim Index corresponds to its Dataset Index
cosine_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

# Search for anime titles in the dataset and return their details and indices
def get_anime_details(titles):
    # Normalize input titles to lowercase for case-insensitive matching
    titles = [title.lower().strip() for title in titles]

    anime_details = []

    for title in titles:
        # Search for matching rows in both 'Name' and 'English name' fields
        matched_anime = anime_df[
            (anime_df['Name'].str.lower() == title) |
            (anime_df['English name'].str.lower() == title)
        ]

        # If a match is found, convert the row to a dictionary and add to the list
        if not matched_anime.empty:
            # Get the first match to ensure we get the original series if there are sequels
            anime_dict = matched_anime.iloc[0].to_dict()    # iloc[0] to get original in case sequels share name
            index = matched_anime.iloc[0].name              # Get the index of the matched row
            anime_details.append((anime_dict, index))       # Add to list as a tuple-pair

    return anime_details

# Return a list of recommended anime series (list of anime objects) that are similar to titles
def get_recommendations(titles, num_recommendations=10):
    # Step 4: Get the details of input anime
    anime_details = get_anime_details(titles)       # List of tuple-pairs (anime_dict, index)
    input_indices = [i[1] for i in anime_details]   # Extract the indices from the anime_details
    
    # Step 5: Get similarity scores for each input title
    similarity_scores = []

    for index in input_indices:
        # Fetch the row of cosine similarity scores for this anime
        curr_sim_scores = list(enumerate(cosine_sim_matrix[index])) # List of (index, similarity score) pairs
        similarity_scores.extend(curr_sim_scores)

    # Step 6: Aggregate similarity scores by anime index (each unique anime now has an aggregated sim_score)
    anime_score_dict = defaultdict(float)   # Dictionary to hold aggregated similarity scores

    for index, score in similarity_scores:
        anime_score_dict[index] += score    # Add up scores for each anime
    
    # Step 7: Sort by similarity score x[1] in descending order
    sorted_anime_scores = sorted(anime_score_dict.items(), key=lambda x: x[1], reverse=True)

    # Step 8: Remove input titles from recommendations
    sorted_anime_scores = [item for item in sorted_anime_scores if item[0] not in input_indices]

    # Step 9: Get the top N recommendations and return their details
    top_recommendations = sorted_anime_scores[:num_recommendations]
    recommended_anime_details = [anime_df.iloc[index].to_dict() for index, score in top_recommendations]

    return recommended_anime_details
