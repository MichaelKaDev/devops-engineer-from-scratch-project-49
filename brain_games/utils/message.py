import prompt


def calc_rules():
    print('What is the result of the expression?')


def even_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
