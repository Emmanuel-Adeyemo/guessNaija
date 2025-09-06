import unittest
from unittest.mock import patch

from utils.helpers import get_number_of_players_or_level, hide_phrase

class TestHelpers(unittest.TestCase):

    # The following tests get_number_of_players(prompt, min_val, max_val)
    # using the mock_input to simulate user response. Side_effect represents the response passed into game
    @patch ('utils.helpers.input', side_effect = ['2'])
    def test_valid_input(self, mock_input):
        """ Tests correct input """
        results = get_number_of_players_or_level('Enter number of players:', 1, 4)
        self.assertEqual(results, 2)


    @patch ('utils.helpers.input', side_effect = ['0', '3'])
    def test_too_low_and_then_valid(self, mock_input):
        """ Tests an input that is too low ie 0, and then test an actual valid num of players """
        results = get_number_of_players_or_level('Enter number of players:', 1, 4)
        self.assertEqual(results, 3)


    @patch ('utils.helpers.input', side_effect = ['two', 2])
    def test_non_valid_then_valid(self, mock_input):
        """ Tests non-valid input and then a valid one"""
        results = get_number_of_players_or_level('Enter number of players:', 1, 4)
        self.assertEqual(results, 2)


    @patch ('utils.helpers.input', side_effect = ['9', '4'])
    def test_too_high_then_valid(self, mock_input):
        """ Tests a value that's too high, and then one within range"""
        results = get_number_of_players_or_level('Enter number of players:', 1, 4)
        self.assertEqual(results, 4)


    # The following tests are for hide_phrase(phrase, guessed)
    def test_empty_guessed(self):
        """ Tests if guessed is empty ie at the beginning of game"""
        phrase = 'FIRST GAME'
        guessed = []
        expected_output = '_____ ____'
        self.assertEqual(hide_phrase(phrase, guessed), expected_output)

    def test_few_letters_guessed(self):
        """ Tests some letters in phrase has been guessed"""
        phrase = 'GUESS NAIJA'
        guessed = ['H', 'L', 'S', 'A', 'P']
        expected_outcome = '___SS _A__A'
        self.assertEqual(hide_phrase(phrase, guessed), expected_outcome)

    def test_all_guessed(self):
        """ Tests all letters in phrase has been guessed """
        phrase = 'CAPTAIN PUFF'
        guessed = ['H', 'L', 'S', 'A', 'P', 'F', 'C', 'T', 'I', 'N', 'U']
        expected_outcome = 'CAPTAIN PUFF'
        self.assertEqual(hide_phrase(phrase, guessed), expected_outcome)


if __name__ == '__main__':
    unittest.main()