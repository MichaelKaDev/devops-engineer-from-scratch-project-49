import random


def get_random_number(f_board=-50, s_board=50):
    number = random.randint(f_board, s_board)
    return number


def get_random_operation():
    return random.choice(['+', '-', '*'])


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_random_progression(f_board=1, s_board=150, length=10):
    step = get_random_number(1, 10)
    progression_number = get_random_number(1, 100)
    progression_list = [0] * length

    for index, element in enumerate(progression_list):
        progression_list[index] = progression_number + index * step
    
    return progression_list


def is_prime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True