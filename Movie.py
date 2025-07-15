class Movie:
    def __init__(self, name, rating, genre):
        """
        Create a Movie object
        :param name: movie name
        :param rating: movie rating
        :param genre: movie genre
        """
        self.name = name
        self.rating = rating
        self.genre = genre

    def __str__(self):
        return f"Movie Name: {self.name}, Rating: {self.rating}, Genre: {self.genre}"

    def __repr__(self):
        return f"Movie(name='{self.name}', rate={self.rating}, genre='{self.genre}')"
