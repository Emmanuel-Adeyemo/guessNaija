import unittest
from classes.GuessNaija import GuessNaija

print('GuessNaija imported successfully')


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
        self.player.add_other_prize('free lunch')
        self.assertEqual(self.player.other_prizes, ['free lunch'])
        self.player.add_other_prize('free gas for a week')
        self.assertEqual(self.player.other_prizes, ['free lunch', 'free gas for a week'])

    def test_go_bankrupt(self):
        self.player.add_money(1890)
        self.assertEqual(self.player.money_won, 1890)
        self.player.go_bankrupt()
        self.assertEqual(self.player.money_won, 0)



if __name__ == '__main__':
    unittest.main()
