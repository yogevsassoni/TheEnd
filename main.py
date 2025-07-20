import json
from Movie import Movie
from User import User


def load_all_users(filename='users_data.json') -> dict:
    """
    Load all users' data from a JSON file.
    :param filename: The JSON file path to load data from.
    :return: A dictionary containing all users' data.
    """
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_all_users(all_users, filename='users_data.json'):
    """
    Save all users' data to a JSON file.
    :param all_users: Dictionary of all users.
    :param filename: The JSON file path to save data to.
    """
    with open(filename, 'w') as f:
        json.dump(all_users, f, indent=4)
    print("All users have been saved.")


def register(all_users) -> User:
    """
    Register a new user with a unique username.
    :param all_users: Dictionary of all existing users.
    :return: A new User object.
    """
    while True:
        username = input("Enter a username to register: ").strip()
        if username == '':
            print("Username cannot be empty.")
        elif username in all_users:
            print("Username already exists.")
        else:
            print(f"User {username} registered successfully.")
            return User(username, [], [])


def login(all_users) -> User | None:
    """
    Log in an existing user.
    :param all_users: Dictionary of all existing users.
    :return: The logged-in User object, or None if not found.
    """
    username = input("Enter username: ").strip()
    if username in all_users:
        return User.from_dict(all_users[username])
    else:
        print("User not found. Please register first.")
        return None


def add_movie(user: User):
    """
    Add a new movie to the user's movie list.
    Prevents duplicates by checking existing movie names.
    :param user: User object.
    """
    name = input("Enter movie name: ")
    if any(m.name == name for m in user.movies):
        print("Movie already exists in your list.")
        return
    rating = rate_movie(name)
    genre = cluster_movie_to_genre(name)
    user.movies.append(Movie(name, rating, genre))
    print(f"Movie '{name}' added.")


def rate_movie(movie_name: str) -> int:
    """
    Rate a movie between 1 to 10.
    :param movie_name: Name of the movie.
    :return: An integer rating between 1 to 10.
    """
    while True:
        try:
            rating = int(input(f"Rate '{movie_name}' (1-10): "))
            if 1 <= rating <= 10:
                return rating
            print("Rating must be between 1 and 10.")
        except ValueError:
            print("Invalid input. Enter a number between 1-10.")


def cluster_movie_to_genre(movie_name: str) -> str:
    """
    Prompt the user to provide a genre for the movie.
    :param movie_name: Name of the movie.
    :return: Genre name as a string.
    """
    return input(f"Enter genre for '{movie_name}': ").strip()


def show_statistics(user: User):
    """
    Display statistics for the user's movies including average rating,
    highest rated movies, and lowest rated movies.
    :param user: User object.
    """
    if not user.movies:
        print("No movies to show statistics for.")
        return
    avg = get_avg_rating(user.movies)
    max_movies = get_max_rating_movies(user.movies)
    min_movies = get_min_rating_movies(user.movies)

    print(f"\033[94mAverage rating:\033[0m {avg:.2f}")
    print(f"\033[92mHighest rated movies:\033[0m {[m.name for m in max_movies]}")
    print(f"\033[91mLowest rated movies:\033[0m {[m.name for m in min_movies]}")


def get_avg_rating(movies: list) -> float:
    """
    Calculate the average rating of a list of movies.
    :param movies: List of Movie objects.
    :return: The average rating.
    """
    return sum(m.rating for m in movies) / len(movies)


def get_max_rating_movies(movies: list) -> list:
    """
    Get the movies with the highest rating.
    :param movies: List of Movie objects.
    :return: List of movies with the maximum rating.
    """
    max_rating = max(m.rating for m in movies)
    return [m for m in movies if m.rating == max_rating]


def get_min_rating_movies(movies: list) -> list:
    """
    Get the movies with the lowest rating.
    :param movies: List of Movie objects.
    :return: List of movies with the minimum rating.
    """
    min_rating = min(m.rating for m in movies)
    return [m for m in movies if m.rating == min_rating]


def recommend_movies(user: User):
    """
    Provide movie recommendations based on user's favorite genres.
    :param user: User object.
    """
    if not user.movies:
        print("No movies in your list to recommend from.")
        return

    genres_input = input("Enter your favorite genres (comma separated): ")
    genres = [g.strip() for g in genres_input.split(',')]
    for genre in genres:
        genre_movies = movies_by_genre(user.movies, genre)
        if genre_movies:
            best = get_max_rating_movies(genre_movies)
            print(f"Best movies in genre '{genre}': {[m.name for m in best]}")
        else:
            print(f"No movies found in genre '{genre}'.")


def movies_by_genre(movies: list, genre: str) -> list:
    """
    Filter movies by a specific genre.
    :param movies: List of Movie objects.
    :param genre: Genre name to filter by.
    :return: List of movies matching the genre.
    """
    return [m for m in movies if m.genre.lower() == genre.lower()]


def main():
    """
    Main function to run the Movie Review App. Includes options for login,
    registration, adding movies, rating, recommendations, statistics, saving,
    loading, and exiting the application.
    """
    all_users = load_all_users()
    current_user = None

    print("Welcome to the Movie Review App")
    while not current_user:
        action = input("Choose 'login' or 'register': ").strip().lower()
        if action == 'login':
            current_user = login(all_users)
        elif action == 'register':
            current_user = register(all_users)
        else:
            print("Invalid choice. Try again.")

    while True:
        print("\nMenu:")
        print("1. Add a Movie")
        print("2. Rate a Movie")
        print("3. Get Recommendations")
        print("4. Show Statistics")
        print("5. Save")
        print("6. Load")
        print("7. Exit")

        choice = input("Enter choice (1-7): ")

        if choice == '1':
            add_movie(current_user)
        elif choice == '2':
            movie_name = input("Enter the name of the movie to rate: ")
            for m in current_user.movies:
                if m.name == movie_name:
                    m.rating = rate_movie(movie_name)
                    print(f"Updated rating for '{movie_name}'.")
                    break
            else:
                print("Movie not found in your list.")
        elif choice == '3':
            recommend_movies(current_user)
        elif choice == '4':
            show_statistics(current_user)
        elif choice == '5':
            all_users[current_user.username] = current_user.to_dict()
            save_all_users(all_users)
        elif choice == '6':
            all_users = load_all_users()
            print("Users data reloaded.")
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-7.")


if __name__ == '__main__':
    main()
