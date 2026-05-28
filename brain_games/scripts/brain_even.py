from brain_games.utils import check_answer_game, welcome_user


def main():
    name = welcome_user()
    check_answer_game(name)


if __name__ == "__main__":
    main()