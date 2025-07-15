class User:
    def __init__(self, username, movies, favourites):
        self.username = username
        self.movies = movies
        self.favourites = favourites

    def __str__(self):
        return (
            f"User: {self.username}\n"
            f"Movies: {self.movies}\n"
            f"Favourites: {self.favourites}"
        )

    def to_dict(self):
        return {
            'username': self.username,
            'movies': [movie.to_dict() for movie in self.movies],
            'favourites': self.favourites
        }

    def __repr__(self):
        return f"User(username='{self.username}', movies={self.movies}, favourites={self.favourites})"
