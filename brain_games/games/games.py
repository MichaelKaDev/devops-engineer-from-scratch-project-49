import prompt

from brain_games.utils.math import (
    get_random_number,
    get_random_operation,
    is_even,
)

from brain_games.utils.logic import check_answer


def calc_game_round(name: str, target_score=2):
    number1 = get_random_number()
    number2 = get_random_number()
    operation = get_random_operation()
    print(f'Question: {number1} {operation} {number2}')
    match operation:
        case '+':
            right_answer = number1 + number2
        case '-':
            right_answer = number1 - number2
        case '*':
            right_answer = number1 * number2
    str_answer = int(prompt.string('Your answer: '))
    return check_answer(name, str_answer, right_answer)
        

def even_game_round(name: str):
    number = get_random_number()
    print(f'Question: {number}')
    right_answer = "yes" if is_even(number) else "no"
    str_answer = prompt.string('Your answer: ')
    return check_answer(name, str_answer, right_answer)