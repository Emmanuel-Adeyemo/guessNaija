# import random
# import time

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = [letter for letter in LETTERS]

def get_number_of_players_or_level(prompt: str, min_val: int, max_val: int) -> int:
    """ Gets the numbers of human players for the game.
    Can also get the level for the computer player.
    Returns the number of players or computer level for the game """

    # this is the initial message
    user_input = input(prompt)

    while True:
        try:
            player_num = int(user_input)
            if player_num < min_val:
                error_message = f'Must be at least {min_val}'
            elif player_num > max_val:
                error_message = f'Must not be more than {max_val}'
            else:
                return player_num
        except: # no input
            error_message = 'Enter a valid number'

        # return again and again until it passes
        user_input = input(f'{error_message}, {prompt}')

# print(get_number_of_players('Enter a number of players:', 1, 10))


def spin_guess_naija_wheel():
    """ This spins the wheel
    Basically loads the rewards file and randomly select a prize"""
    pass


def get_category_and_phrase():
    """ Loads the category file and phrase"""
    pass


def hide_phrase(phrase: str, guessed: list) -> str:
    """" Hides all letters in phrase, reveals letter in the right position when right letter is guessed
    Params: phrase - takes a string e.g. 'THIS IS NEW YORK'
     Params: guessed - this is a list of previously guessed letters e.g. ['F', 'N', 'E', 'T', 'U', 'S', 'R']
      Returns: 'T__S _S NE_ __R_'  """

    hidden = ''

    # check_phrase = [l for l in phrase]
    # for every letter in the selected phrase,
    # if it is not in guessed, return _
    # else - show position of letter in phrase
    for l in phrase:
        if l in letters and l not in guessed:
            hidden += '_'
        else:
            hidden += l

    return hidden

# print(hide_phrase("THIS IS NEW YORK", ['F', 'N', 'E', 'T', 'U', 'S', 'R']))

def show_current_state(category, hidden_phrase, guessed):
    """ Returns the current state of game"""

    return (f'Category: {category}\n'
            f'Phrase: {hidden_phrase}\n'
            f"Guessed: {','.join(sorted(guessed))}\n")

# print(show_current_state('Title', hide_phrase("THIS IS NEW YORK", ['F', 'N', 'E', 'T', 'U', 'S', 'R']), ['F', 'N', 'E']))

