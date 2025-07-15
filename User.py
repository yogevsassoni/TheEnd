class User:
    def __init__(self, name, movies, favourites):
        self.name = name
        self.movies = movies
        self.favourites = favourites

    def __str__(self):
        return (
            f"User: {self.name}\n"
            f"Movies: {self.movies}\n"
            f"Favourites: {self.favourites}"
        )

    def __repr__(self):
        return f"User(username='{self.name}', movies={self.movies}, favourites={self.favourites})"
