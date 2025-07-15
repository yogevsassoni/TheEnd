def get_movie_list():
    movie_dict = {}
    while True:
        user_input = input("Enter a movie title (or type 'finish' to end): ")
        if user_input.lower() == 'finish':
            break
        if user_input in movie_dict:
            print("You've already rated this movie.")
            continue
        movie_dict[user_input] = rate_movie(user_input)
    return movie_dict


def rate_movie(movie):
    while True:
        try:
            rate = int(input(f"Rate the movie '{movie}' (1-10): "))
            if 1 <= rate <= 10:
                return rate
            print("Number must be between 1 and 10.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 10.")


def get_avg_rating(movie_dict):
    return sum(movie_dict.values()) / len(movie_dict)


def get_max_rating_movies(movie_dict):
    max_rating = max(movie_dict.values())
    return [movie for movie, rating in movie_dict.items() if rating == max_rating]


def get_min_rating_movies(movie_dict):
    min_rating = min(movie_dict.values())
    return [movie for movie, rating in movie_dict.items() if rating == min_rating]


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
