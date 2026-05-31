from brain_games.games.games import calc_game_round, even_game_round
from brain_games.utils.message import calc_rules, even_rules, welcome_user


def run_game(game_name, rounds_count=3):
    match game_name:
        case "brain_even":
            rules_print = even_rules
            game_round = even_game_round
        case "brain_calc":
            rules_print = calc_rules
            game_round = calc_game_round

    name = welcome_user()
    rules_print()

    for quest in range(rounds_count):
        if not game_round(name):
            return
    print(f"Congratulations, {name}!")

    
    
