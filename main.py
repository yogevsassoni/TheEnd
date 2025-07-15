from Movie import Movie
from User import User


def get_movie_list():
    """
    Create a list of Movie objects by user input
    :return: list of Movie objects
    """
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


def rate_movie(movie: str) -> int:
    """
    Rate a movie between 1 and 10
    :param movie: movie name
    :return: rating as integer
    """
    while True:
        try:
            rate = int(input(f"Rate the movie '{movie}' (1-10): "))
            if 1 <= rate <= 10:
                return rate
            print("Number must be between 1 and 10.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 10.")


def cluster_movie_to_genre(movie: str) -> str:
    """
    Get the genre of a movie from user input
    :param movie: movie name
    :return: genre as string
    """
    return input(f"Genre of '{movie}': ")


def get_avg_rating(movies: list) -> float:
    """
    Calculate the average rating of the movies
    :param movies: list of Movie objects
    :return: average rating
    """
    return sum(movie.rating for movie in movies) / len(movies)


def get_max_rating_movies(movies: list) -> list:
    """
    Get all movies with the highest rating
    :param movies: list of Movie objects
    :return: list of Movie objects with max rating
    """
    max_rating = max(movie.rating for movie in movies)
    return [movie for movie in movies if movie.rating == max_rating]


def get_min_rating_movies(movies: list) -> list:
    """
    Get all movies with the lowest rating
    :param movies: list of Movie objects
    :return: list of Movie objects with min rating
    """
    min_rating = min(movie.rating for movie in movies)
    return [movie for movie in movies if movie.rating == min_rating]


def movies_by_genre(movies: list, genre: str) -> list:
    """
    Filter movies by a given genre
    :param movies: list of Movie objects
    :param genre: genre to filter by
    :return: list of Movie objects of that genre
    """
    return [movie for movie in movies if movie.genre.lower() == genre.lower()]


def best_movie_by_genre(movies: list, genre: str) -> list:
    """
    Get the best-rated movies in a specific genre
    :param movies: list of Movie objects
    :param genre: genre to search in
    :return: list of Movie objects with max rating in that genre
    """
    return get_max_rating_movies(movies_by_genre(movies, genre))


def filter_valid_genres(movies: list, genres_input: str) -> tuple:
    """
    Validate genres input by the user against available genres in the movie list
    :param movies: list of Movie objects
    :param genres_input: string of genres separated by comma
    :return: tuple of (valid genres, invalid genres)
    """
    available_genres = {movie.genre.lower() for movie in movies}
    input_genres = [genre.strip() for genre in genres_input.split(',')]
    valid_genres = [genre for genre in input_genres if genre.lower() in available_genres]
    invalid_genres = [genre for genre in input_genres if genre.lower() not in available_genres]
    return valid_genres, invalid_genres


def offer_best_rated_genre_movies(movies: list, valid_genres: list) -> list:
    """
    Get best-rated movies for each valid genre
    :param movies: list of Movie objects
    :param valid_genres: list of valid genres
    :return: list of best-rated Movie objects per genre
    """
    return [best_movie_by_genre(movies, genre) for genre in valid_genres]


def main():
    """
    Run the Movie Review App main flow
    """
    print("Welcome to the Movie Review App")
    username = input("Please login by username: ")
    movies = get_movie_list()

    if not movies:
        print("No movies listed.")
        return

    print(movies)
    print(
        f"\033[94mThe average rating is:\033[0m {get_avg_rating(movies)}\n"
        f"\033[92mThe highest rating movies are:\033[0m {get_max_rating_movies(movies)}\n"
        f"\033[91mThe lowest rating movies are:\033[0m {get_min_rating_movies(movies)}"
    )

    genres_input = input("Enter your favourite genres (comma separated): ")
    valid_genres, invalid_genres = filter_valid_genres(movies, genres_input)

    if invalid_genres:
        print(f"Ignored genres not found: {', '.join(invalid_genres)}")

    best_movies = offer_best_rated_genre_movies(movies, valid_genres)
    print(f"Best rated movies in your favourite genres: {best_movies}")

    user = User(username, movies, valid_genres)
    print(user)


if __name__ == '__main__':
    main()
