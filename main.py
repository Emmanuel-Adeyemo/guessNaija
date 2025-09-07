
import time
from classes.GuessNaija import GuessNaijaPlayer, GuessNaijaComputer
from utils.helpers import get_number_of_players_or_level, get_category_and_phrase, spin_guess_naija_wheel, hide_phrase, \
    show_current_state, get_player_move

# Get number of human/ computer players. Get level of computer players if available

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'
VOWEL_COST = 50000

# player mechanics
min_number_of_players = 1
max_number_of_players = 4

min_computer = 0

min_level = 1
max_level = 10

# human players
num_of_human_players = get_number_of_players_or_level('Enter Number of Human Players: ',
                                                      min_number_of_players, max_number_of_players)

human_players = [GuessNaijaPlayer(input(f'Enter Name of Player {player + 1}: ')) for player in range(num_of_human_players)]

# computer players
num_of_computer_players = get_number_of_players_or_level('Enter Number of Computer Players: ', min_computer, max_number_of_players)

if num_of_computer_players >= 1:
    computer_level = get_number_of_players_or_level('Enter Computer Level: ', min_level, max_level)


computer_players = [GuessNaijaComputer(f'computer_{comp + 1}', computer_level) for comp in range(num_of_computer_players)]

players = human_players + computer_players

if len(players) == 0:
    print('We need players to play!')
    raise Exception ('Not Enough Players')



# GAME LOGIC CODE
print(' ' * 10 + ' /\\')
print(' ' * 9 + '/  \\')
print(' ' * 8 + '/    \\')
print(' ' * 7 + '/______\\')
print(' ' * 6 + '|      |')
print(' ' * 5 + '|      |')
print('='*15)
print(' ' + 'GUESS NAIJA' + ' ' * 3)
print('='*15)
print(' ' * 5 + '|      |')
print(' ' * 5 + '|      |')
print(' ' * 6 + '\\____/')

# run game
category, phrase = get_category_and_phrase()
# saves letters that have been guessed
guessed = []

# player_index keeps track of the index (0 to len(players)-1) of the player whose turn it is
player_index = 0

# will be set to the player instance when/if someone wins
winner = False
end = False

while True:
    player = players[player_index]
    wheel_prize = spin_guess_naija_wheel()

    print('')
    print('-'*15)
    print(show_current_state(category, hide_phrase(phrase, guessed), guessed))
    print('')
    print(f'{player.name} spins... ', end='')

    # pause
    time.sleep(2)
    print(f'{wheel_prize["text"]}!')
    # pause again
    time.sleep(1)


    if wheel_prize['type'] == 'bankrupt':
        player.go_bankrupt()
    elif wheel_prize['type'] == 'loseturn':
        # move to next player
        pass
    elif wheel_prize['type'] == 'cash':
        move = get_player_move(player, category, phrase, guessed)
        if move == 'EXIT':
            # leave game
            print('Exiting the game... until next time!')
            break
        elif move == 'PASS':
            # move to next player
            print(f'{player.name} passes!')


        elif len(move) == 1:
            # if they guess a letter
            guessed.append(move)

            print(f'{player.name} guesses "{move}"')


            # counts how many times letter appears
            letter_count = phrase.count(move)
            if letter_count > 0:
                if letter_count == 1:
                    print(f"There is one {move} in the phrase")
                else:
                    print(f"There are {letter_count} {move}'s in the phrase")

                # Give them the money and the prizes

                if move in VOWELS:
                    player.money_won -= VOWEL_COST

                else:
                    player.add_money(letter_count * wheel_prize['value'])
                    if wheel_prize['prize']:
                        player.add_other_prize(wheel_prize['prize'])

                # check if all of the letters have been guessed
                if hide_phrase(phrase, guessed) == phrase:
                    end = True
                    break

                continue # this player gets to go again

            else: # letter_count == 0
                print(f'There is no {move}')

        else: # they guessed the whole phrase
            if move == phrase: # they guessed the full phrase correctly
                end = True

                # Give them the money and the prizes
                player.add_money(wheel_prize['value'])
                if wheel_prize['prize']:
                    player.add_other_prize(wheel_prize['prize'])

                break
            else:
                print(f'{move} was not the phrase')

    # Move on to the next player (or go back to player[0] if we reached the end)
    player_index = (player_index + 1) % len(players)

if end:

    max_money = max(player.money_won for player in players)

    winner_list = [player for player in players if player.money_won == max_money]

    winner = winner_list[0]

    print('{} wins! The phrase was {}'.format(winner.name, phrase))
    print('{} won ${}'.format(winner.name, winner.money_won))
    if len(winner.other_prizes) > 0:
        print('{} also won:'.format(winner.name))
        for prize in winner.other_prizes:
            print('    - {}'.format(prize))
else:
    print(f'Nobody won. The phrase was {phrase}')



