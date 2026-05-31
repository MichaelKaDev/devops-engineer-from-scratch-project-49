import random


def get_random_number(f_board=-50, s_board=50):
    number = random.randint(f_board, s_board)
    return number


def get_random_operation():
    return random.choice(['+', '-', '*'])


def is_even(number: int) -> bool:
    return number % 2 == 0