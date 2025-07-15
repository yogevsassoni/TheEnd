def get_movie_list():
    movie_list = []
    user_input = input("Please enter a movie title (When you done enter 'finish': ")
    while user_input != "finish":
        movie_list.append(user_input)
        user_input = input("Please enter a movie title: ")
    return movie_list


def main():
    movie_list = get_movie_list()
    print(movie_list)


if __name__ == '__main__':
    main()
