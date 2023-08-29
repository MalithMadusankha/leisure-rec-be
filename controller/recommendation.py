import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.neighbors import NearestNeighbors

def recommend_places(csv_file_path, target_type, num_recommendations=5):
    # Read data from CSV file
    print(" called recommend places ")
    places_data = []
    with open(csv_file_path, "r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            places_data.append(row)
    
    # Create TF-IDF vectors for place types
    place_types = [place["type"] for place in places_data]
    tfidf_vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf_vectorizer.fit_transform(place_types)
    
    # Calculate cosine similarities between place types
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    # Find the target place's index
    target_place_index = -1
    for i, place in enumerate(places_data):
        if place["type"] == target_type:
            target_place_index = i
            break
    
    if target_place_index == -1:
        return "Target type not found in the dataset"
    
    # Use KNN to recommend similar places 
    knn = NearestNeighbors(n_neighbors=num_recommendations, metric="cosine", algorithm="brute")
    knn.fit(cosine_similarities)
    similar_place_indices = knn.kneighbors([cosine_similarities[target_place_index]], n_neighbors=num_recommendations+1, return_distance=False)
    recommended_places = [places_data[i] for i in similar_place_indices.flatten() if i != target_place_index]
    
    return recommended_places


