import csv
from functools import reduce

# Load movie data from CSV
def load_movies(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Convert numerical fields
def transform_movies(movies):
    return list(map(lambda m: {
        "title": m["title"],
        "year": int(m["year"]),
        "rating": float(m["rating"]),
        "revenue": int(m["revenue"])
    }, movies))

# Get top-rated movies (rating > 8.5)
def get_top_rated_movies(movies):
    return list(filter(lambda m: m["rating"] > 8.5, movies))

# Compute average rating
def average_rating(movies):
    total_rating = reduce(lambda acc, m: acc + m["rating"], movies, 0)
    return total_rating / len(movies) if movies else 0

# Find highest-grossing movie
def highest_grossing_movie(movies):
    return max(movies, key=lambda m: m["revenue"], default=None)

# Main function
def main():
    movies = load_movies("movies.csv")
    movies = transform_movies(movies)

    top_movies = get_top_rated_movies(movies)
    avg_rating = average_rating(movies)
    highest_grossing = highest_grossing_movie(movies)

    print("\nTop Rated Movies:")
    for movie in top_movies:
        print(f"{movie['title']} ({movie['year']}) - Rating: {movie['rating']}")

    print(f"\nAverage Movie Rating: {avg_rating:.2f}")
    print(f"\nHighest Grossing Movie: {highest_grossing['title']} - ${highest_grossing['revenue']}M")

if __name__ == "__main__":
    main()
