from Movie import Movie


class User:
    def __init__(self, username, movies, favourites):
        self.username = username
        self.movies = movies  # List of Movie objects
        self.favourites = favourites  # List of genres (strings)

    def to_dict(self):
        """
        Convert the User object to a dictionary suitable for JSON serialization.
        """
        return {
            'username': self.username,
            'movies': [movie.to_dict() for movie in self.movies],
            'favourites': self.favourites
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a User object from a dictionary (as loaded from JSON).
        :param data: Dictionary with user data.
        :return: User object.
        """
        movies = [Movie(**movie_data) for movie_data in data.get('movies', [])]
        return cls(
            username=data['username'],
            movies=movies,
            favourites=data.get('favourites', [])
        )
