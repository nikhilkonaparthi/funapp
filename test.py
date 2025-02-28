import unittest
from src.movie_processing import transform_movies, get_top_rated_movies, average_rating, highest_grossing_movie

class TestMovieProcessing(unittest.TestCase):
    
    def setUp(self):
        self.movies = [
            {"title": "Inception", "year": 2010, "rating": 8.8, "revenue": 829},
            {"title": "Avatar", "year": 2009, "rating": 7.8, "revenue": 2788},
            {"title": "The Dark Knight", "year": 2008, "rating": 9.0, "revenue": 1005}
        ]

    def test_transform_movies(self):
        raw_movies = [
            {"title": "Movie1", "year": "2020", "rating": "7.5", "revenue": "100"}
        ]
        transformed = transform_movies(raw_movies)
        self.assertEqual(transformed[0]["year"], 2020)
        self.assertEqual(transformed[0]["rating"], 7.5)
        self.assertEqual(transformed[0]["revenue"], 100)

    def test_get_top_rated_movies(self):
        top_movies = get_top_rated_movies(self.movies, 8.5)
        self.assertEqual(len(top_movies), 2)

    def test_average_rating(self):
        self.assertAlmostEqual(average_rating(self.movies), 8.53, places=2)

    def test_highest_grossing_movie(self):
        self.assertEqual(highest_grossing_movie(self.movies)["title"], "Avatar")

if __name__ == "__main__":
    unittest.main()
