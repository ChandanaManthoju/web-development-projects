def recommend_movies_for_users(algo, data, user_ids, n=5):
    recommendations = {}

    for user_id in user_ids:
        # Get movie recommendations for each user
        user_recommendations = algo.recommend(user_id, n, filter_already_liked_items=False)

        # Store the recommended movie IDs
        recommendations[user_id] = [movie_id for movie_id, _ in user_recommendations]

    # Convert movie IDs to movie titles
    movie_titles = {movie_id: movie['title'] for movie_id, movie in data['movies'].items()}
    recommended_movies = {user_id: [movie_titles[movie_id] for movie_id in movie_ids] for user_id, movie_ids in recommendations.items()}

    return recommended_movies

# Example MovieLens dataset (you should replace this with your actual data)
movie_data = {
    'movies': {
        1: {'title': 'Movie 1'},
        2: {'title': 'Movie 2'},
        # ... more movie data ...
    },
    # ... other data ...
}

# Example collaborative filtering algorithm (replace with your own)
class CollaborativeFilteringAlgorithm:
    def recommend(self, user_id, n, filter_already_liked_items):
        # Implement your recommendation logic here
        # Return a list of (movie_id, score) tuples
        return [(1, 0.9), (2, 0.8), (3, 0.7)]

# Example list of user IDs
user_ids = [1, 100, 500]

# Create an instance of the collaborative filtering algorithm
cf_algo = CollaborativeFilteringAlgorithm()

# Get movie recommendations for users
recommended_movies = recommend_movies_for_users(cf_algo, movie_data, user_ids, n=3)
print("Recommended Movies for Users:", recommended_movies)