import random
import json
import time
from pathlib import Path

from classes.GuessNaija import GuessNaijaPlayer

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = [letter for letter in LETTERS]

VOWELS = 'AEIOU'
VOWEL_COST = 50000

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


def spin_guess_naija_wheel()-> dict:
    """ This spins the wheel
    Basically loads the rewards file and randomly select a prize.
    Returns a dictionary with wheel information. """

    current_directory = Path(__file__).parent.parent
    file_path = current_directory/'assets/naija_wheel.json'

    try:
        with open(file_path, 'r') as wheel_dta:
            naija_wheel = json.loads(wheel_dta.read())
    except:
        print(f'File not found in the path {file_path}')
        return {}

    return random.choice(naija_wheel)


def get_category_and_phrase()-> tuple:
    """ Loads the category file and randomly selects phrase"""
    current_directory = Path(__file__).parent.parent
    file_path = current_directory/'assets/naija_phrases.json'

    try:
        with open(file_path, 'r') as phrase_dta:
            naija_phrases = json.loads(phrase_dta.read())
            category  = random.choice([titles for titles in naija_phrases])
            phrase = random.choice(naija_phrases[category])
    except:
        print(f'No file found in {file_path}')

        return None, None

    return category, phrase.upper()


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

def show_current_state(category: str, hidden_phrase: str, guessed: list)-> str:
    """ Returns the current state of game"""

    return (f'Category: {category}\n'
            f'Phrase: {hidden_phrase}\n'
            f"Guessed: {','.join(sorted(guessed))}\n")


def get_player_move(player: GuessNaijaPlayer, category: str, phrase:str, guessed:list):
    """ This asks human player for move, makes sure it is a valid move and then returns move.
    Move can be a letter, the phrase, exit or pass """
    while True:
        time.sleep(0.6) # Just some delay before feedback

        move = player.get_move(category, hide_phrase(phrase, guessed), guessed)
        print(move)
        try:
            move = move.upper()
            # print(move)
        except:
            # print(move)
            move = move

        if move == 'EXIT' or move == 'PASS':
            return move
        if len(move) == 1:
            if move not in LETTERS:
                print('You have not entered a letter. Try again! \n')
                continue
            elif move in guessed:
                print(f'{move} has already been guessed. Try again!\n')
                continue
            elif move in VOWELS and player.money_won < VOWEL_COST:
                print(f'You need ₦{VOWEL_COST} to guess a vowel. Try again!\n')
                continue
            else:
                return move

        else:
            # player has entered the entire phrase
            return move


# print(show_current_state('Title', hide_phrase("THIS IS NEW YORK", ['F', 'N', 'E', 'T', 'U', 'S', 'R']), ['F', 'N', 'E']))
#
# gues = ['F', 'N', 'E', 'T', 'U', 'S', 'R']
# print(spin_guess_naija_wheel())

#
# # print(show_current_state(cat, hide_phrase(ph, gues), gues))
# oluchi = GuessNaijaPlayer('oluchi')
# print(get_player_move(oluchi, cat, ph, gues))


