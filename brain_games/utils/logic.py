def check_answer(name, str_answer, right_answer):
    if str_answer != right_answer:
        print(f"'{str_answer}' is wrong answer ;(. Correct answer "
            f"was '{right_answer}'."
        )
        print(f"Let's try again, {name}!")
        return False
    else:
        print("Correct!")
        return True