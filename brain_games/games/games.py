import prompt

from brain_games.utils.logic import check_answer
from brain_games.utils.math import (
    get_random_number,
    get_random_operation,
    get_random_progression,
    is_even,
)


def calc_game_round(name: str):
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


def gcd_game_round(name: str):
    number1 = get_random_number()
    number2 = get_random_number()

    print(f'Question: {number1} {number2}')
    str_answer = abs(int(prompt.string('Your answer: ')))

    if number1 < number2:
        switch = number1
        number1 = number2
        number2 = switch
    
    while (number1 % number2 != 0):
        remainder = number1 % number2
        number1 = number2
        number2 = remainder
    right_answer = abs(number2)

    return check_answer(name, str_answer, right_answer)
    

def progression_game_round(name: str):
    progression_list = get_random_progression()
    position = get_random_number(1, 9)

    print('Question: ', end="")
    for index, number in enumerate(progression_list):
        if index != position:
            print(number, end=" ")
        else:
            right_answer = number
            print("..", end=" ")
    str_answer = int(prompt.string('\nYour answer: '))

    return check_answer(name, str_answer, right_answer)
    


    