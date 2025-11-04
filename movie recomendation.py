import requests
import json
import os
from collections import Counter

class Movie:
    def __init__(self, title, year, genre, rated, imdb_rating, plot):
        self.title = title
        self.year = year
        self.genre = genre
        self.rated = rated
        self.imdb_rating = imdb_rating
        self.plot = plot

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Year: {self.year}\n"
                f"Genre: {self.genre}\n"
                f"Rated: {self.rated}\n"
                f"IMDb Rating: {self.imdb_rating}\n"
                f"Plot: {self.plot}\n")

class MovieSearchSystem:
    def __init__(self, api_key, history_filename="history.json"):
        self.api_key = api_key
        self.history_filename = history_filename
        # Load existing history (movie title counts) if exists
        self.history = self._load_history()

    def _load_history(self):
        if os.path.exists(self.history_filename):
            try:
                with open(self.history_filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print("Could not read history file, starting fresh:", e)
                return {}
        else:
            return {}

    def _save_history(self):
        try:
            with open(self.history_filename, "w", encoding="utf-8") as f:
                json.dump(self.history, f, indent=4)
        except Exception as e:
            print("Error saving history:", e)

    def _record_search(self, title):
        # Use title key (case-insensitive) or normalized?
        # For simplicity, store as-is
        self.history[title] = self.history.get(title, 0) + 1
        self._save_history()

    def search_movie(self, title):
        """
        Search a movie by title via OMDb API, return a Movie object or None if not found.
        """
        base_url = "http://www.omdbapi.com/"
        params = {
            "apikey": self.api_key,
            "t": title,
            "plot": "short",
            "r": "json"
        }
        try:
            response = requests.get(base_url, params=params, timeout=5)
            response.raise_for_status()
        except requests.RequestException as e:
            print("HTTP error / connection error:", e)
            return None

        data = response.json()
        # The API returns {"Response": "False", "Error": "..."} if not found
        if data.get("Response") == "False":
            print("Movie not found:", data.get("Error"))
            return None

        # Extract fields safely
        title0 = data.get("Title", "N/A")
        year = data.get("Year", "N/A")
        genre = data.get("Genre", "N/A")
        rated = data.get("Rated", "N/A")
        imdb_rating = data.get("imdbRating", "N/A")
        plot = data.get("Plot", "N/A")

        movie_obj = Movie(title0, year, genre, rated, imdb_rating, plot)
        # Record the successful search
        self._record_search(title0)
        return movie_obj

    def show_top_searched(self, top_n=5):
        """
        Show top N most searched movie titles and counts.
        """
        if not self.history:
            print("No search history yet.")
            return

        cnt = Counter(self.history)
        print(f"Top {top_n} most searched movies:")
        for title, count in cnt.most_common(top_n):
            print(f"  {title} → {count} times")

def main():
    # Replace with your actual API key
    API_KEY = "YOUR_OMDB_API_KEY"
    system = MovieSearchSystem(API_KEY)

    while True:
        print("\nOptions:")
        print("  1. Search a movie by title")
        print("  2. Show top 5 searched movies")
        print("  3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            title = input("Enter movie title: ").strip()
            if not title:
                print("Empty title, try again.")
                continue
            movie = system.search_movie(title)
            if movie:
                print("\nMovie details:\n")
                print(movie)
        elif choice == "2":
            system.show_top_searched(top_n=5)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try 1, 2 or 3.")

if __name__ == "__main__":
    main()
