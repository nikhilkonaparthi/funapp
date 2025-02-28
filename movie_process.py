
---

### **📂 3. `src/movie_processing.py` (Core Functional Logic)**
```python
import csv
from functools import reduce

def load_movies(filename):
    """Load movie data from a CSV file."""
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def transform_movies(movies):
    """Convert string values to appropriate data types."""
    return list(map(lambda m: {
        "title": m["title"],
        "year": int(m["year"]),
        "rating": float(m["rating"]),
        "revenue": int(m["revenue"])
    }, movies))

def get_top_rated_movies(movies, threshold=8.5):
    """Return movies with a rating above the threshold."""
    return list(filter(lambda m: m["rating"] > threshold, movies))

def average_rating(movies):
    """Compute the average rating of movies."""
    total_rating = reduce(lambda acc, m: acc + m["rating"], movies, 0)
    return total_rating / len(movies) if movies else 0

def highest_grossing_movie(movies):
    """Find the movie with the highest revenue."""
    return max(movies, key=lambda m: m["revenue"], default=None)
