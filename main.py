

def main():
    movies = load_movies("data/movies.csv")
    movies = transform_movies(movies)

    top_movies = get_top_rated_movies(movies)
    avg_rating = average_rating(movies)
    highest_grossing = highest_grossing_movie(movies)

    print("\n🎬 Top Rated Movies:")
    for movie in top_movies:
        print(f"{movie['title']} ({movie['year']}) - Rating: {movie['rating']}")

    print(f"\n⭐ Average Movie Rating: {avg_rating:.2f}")
    print(f"\n💰 Highest Grossing Movie: {highest_grossing['title']} - ${highest_grossing['revenue']}M")

if __name__ == "__main__":
    main()
