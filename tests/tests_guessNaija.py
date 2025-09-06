import random
import unittest

from unittest.mock import patch, MagicMock

import classes.GuessNaija
from classes.GuessNaija import GuessNaija, GuessNaijaComputer, GuessNaijaPlayer
from utils.helpers import hide_phrase


class TestGuessNaija(unittest.TestCase):

    def setUp(self):
        self.player = GuessNaija('oluchi')

    def test_initial_set(self):
        self.assertEqual(self.player.name, 'oluchi')
        self.assertEqual(self.player.money_won, 0)
        self.assertEqual(self.player.other_prizes, [])

    def test_add_money(self):
        self.player.add_money(120)
        self.assertEqual(self.player.money_won, 120)
        self.player.add_money(500)
        self.assertEqual(self.player.money_won, 620)

    def test_add_other_prizes(self):
        self.player.add_other_prize('two dericas of rice')
        self.assertEqual(self.player.other_prizes, ['two dericas of rice'])
        self.player.add_other_prize('buy petrol at ₦100/lt for a week')
        self.assertEqual(self.player.other_prizes, ['two dericas of rice', 'buy petrol at ₦100/lt for a week'])

    def test_go_bankrupt(self):
        self.player.add_money(1890)
        self.assertEqual(self.player.money_won, 1890)
        self.player.go_bankrupt()
        self.assertEqual(self.player.money_won, 0)


# Test Cases for Human Player
class TestGuessNaijaPlayer(unittest.TestCase):
    """ Test cases for human players """

    def setUp(self):
        self.player = GuessNaijaPlayer('dami')

    def test_inheritance(self):
        """ Check if all inherited variables are good """
        self.player.add_money(340)
        self.player.add_other_prize('chill bottle of star larger')
        self.assertEqual(self.player.money_won, 340)
        self.assertEqual(self.player.other_prizes, ['chill bottle of star larger'])
        self.player.go_bankrupt()
        self.assertEqual(self.player.money_won, 0)


    @patch ('builtins.input', side_effect = ['B'])
    def test_get_move(self, mock_input):

        category = 'Occupation'
        phrase = 'AREA BOYS'
        guessed = ['E', 'H', 'T', 'S']

        self.assertEqual(self.player.get_move(category, hide_phrase(phrase, guessed), guessed), 'B')


# Test Cases for Computer
class TestGuestNaijaComputer(unittest.TestCase):
    """ Tests cases for computer player """

    def setUp(self):
        self.computer_level_2 = GuessNaijaComputer('easy', 2)
        self.computer_level_5 = GuessNaijaComputer('medium', 5)
        self.computer_level_9 = GuessNaijaComputer('hard', 9)


    def test_initial_state(self):
        """ Check initial state of game """
        self.assertEqual(self.computer_level_9.level, 9)
        self.assertEqual(self.computer_level_2.name, 'easy')
        self.assertEqual(self.computer_level_5.money_won, 0)

    @patch ('random.randint')
    def test_is_smart(self, mock_rand_int):
        """ Test if computer is smart based on level"""
        mock_rand_int.return_value = 6
        self.assertFalse(self.computer_level_2.is_smart())
        self.assertTrue(self.computer_level_9.is_smart())


    def test_find_possible_letters_no_vowels(self):
        """ Test if no vowels is returned if available money is not up to threshold """
        guessed = ['E', 'H', 'T', 'A']
        results = self.computer_level_2.find_possible_letters(guessed)
        expected_outcome = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'V', 'W', 'X', 'Y', 'Z']
        self.assertEqual(results, expected_outcome)


    def test_find_possible_with_vowels(self):
        """ Tests to make sure vowels are returned when enough money is available """
        guessed = ['E', 'H', 'T', 'A']
        self.computer_level_5.add_money(460)
        results = self.computer_level_5.find_possible_letters(guessed)
        expected_outcome = ['B', 'C', 'D', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.assertEqual(results, expected_outcome)








if __name__ == '__main__':
    unittest.main()
