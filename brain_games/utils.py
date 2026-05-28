import random

import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return name


def get_random_number():
    number = random.getrandbits(16) * random.choice([-1, 1])
    return number


def is_even(number: int) -> bool:
    return number % 2 == 0


def check_answer_game(name: str, target_score=2):
    for score in range(3):
        number = get_random_number()
        print(f'Question: {number}')
        right_answer = "yes" if is_even(number) else "no"
        str_answer = prompt.string('Your answer: ')
        if str_answer.lower() != right_answer:
            print(f"'{str_answer}' is wrong answer ;(. Correct answer "
                f"was '{right_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
        if score >= target_score:
            print(f"Congratulations, {name}!")
            return