class Movie:
    def __init__(self, name, rating, genre):
        self.name = name
        self.rating = rating
        self.genre = genre

    def __str__(self):
        return f"Movie Name: {self.name}, Rating: {self.rating}, Genre: {self.genre}"

    def __repr__(self):
        return f"Movie(name='{self.name}', rate={self.rating}, genre='{self.genre}')"


def get_movie_list():
    movies = []
    while True:
        user_input = input("Enter a movie title (or type 'finish' to end): ")
        if user_input.lower() == 'finish':
            break
        if any(movie.name == user_input for movie in movies):
            print("You've already rated this movie.")
            continue
        movies.append(Movie(user_input, rate_movie(user_input), cluster_movie_to_genre(user_input)))
    return movies


def rate_movie(movie):
    while True:
        try:
            rate = int(input(f"Rate the movie '{movie}' (1-10): "))
            if 1 <= rate <= 10:
                return rate
            print("Number must be between 1 and 10.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 10.")


def cluster_movie_to_genre(movie):
    genre = input(f"Genre of '{movie}' : ")
    return genre


def get_avg_rating(movies):
    return sum(movie.rating for movie in movies) / len(movies)


def get_max_rating_movies(movies):
    max_rating = max(movie.rating for movie in movies)
    return [movie for movie in movies if movie.rating == max_rating]


def get_min_rating_movies(movies):
    min_rating = min(movie.rating for movie in movies)
    return [movie for movie in movies if movie.rating == min_rating]


def main():
    print("Welcome to the Movie Review App")
    movies = get_movie_list()
    if not movies:
        print("No movies listed.")
    else:
        print(movies)
        print(
            f"\033[94mThe average rating is:\033[0m {get_avg_rating(movies)}\n"
            f"\033[92mThe highest rating movies is:\033[0m {get_max_rating_movies(movies)}\n"
            f"\033[91mThe lowest rating movies is:\033[0m {get_min_rating_movies(movies)}"
        )


if __name__ == '__main__':
    main()
