import random
# import time

class GuessNaija:

    """ creates the guessNaija framework """

    def __init__(self, name):
        self.name = name
        self.money_won = 0
        self.other_prizes = []

    def add_money(self, amt):
        self.money_won += amt

    def go_bankrupt(self):
        self.money_won = 0
        self.other_prizes = []

    def add_other_prize(self, prize):
        self.other_prizes.append(prize)

    def __str__(self):
        return f'{self.name} (₦{self.money_won})'



class GuessNaijaPlayer(GuessNaija):

    # set up to print details at every move - ie after spin
    def get_move(self, category, phrase, guessed):
        trail = "Guess a letter, phrase, or type 'exit' or 'pass': "
        details = (f'\n{self.name} has ₦{self.money_won}\n\nCategory: {category}\nPhrase: '
                   f'{phrase}\nGuessed: {guessed}\n\n{trail}')

        userinpt = input(f'{details}')
        return str(userinpt)


class GuessNaijaComputer(GuessNaija):

    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    VOWELS = 'AEIOU'
    VOWEL_COST = 50000

    SORTED_FREQ = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    # reverse order of sorted_freq
    reverse_sort = []
    for letter in SORTED_FREQ:
        reverse_sort.insert(0, letter)

    vowel_lst = [vowel for vowel in VOWELS]

    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

    def is_smart(self):
        # get a random integer, if it's less than level, set smart to True - ie computer is smarter
        # for example if computer level is 7 and random integer is 3, it returns True - more likely to be smart
        # if integer is greater, set smart to False, ie computer is less smart. For example if level is 2 and
        # random integer is 5, it returns False - ie less likely to be smart.

        decider = random.randint(1, 10)
        if decider < self.level:
            return True
        else:
            return False

    def find_possible_letters(self, guessed):

        # if letter is not in guessed, save to list possible
        # if money_won is less than cost, remove vowel from list possible
        possible = [letter for letter in self.LETTERS if letter not in guessed]

        if self.money_won < self.VOWEL_COST:
            possible = [le for le in possible if le not in self.vowel_lst]
        return possible

    def get_move(self, category, hidden_word, guessed):
        # no money for vowels and all consonants have been guessed - pass
        # if there's enough money and letters then check if smart
        # if is_smart, use SORTED_FREQ to choose from available
        # else select random letter from available
        if not self.find_possible_letters(guessed):
            pass
        else:
            available = self.find_possible_letters(guessed)
            if self.is_smart():
                for smart_letter in self.reverse_sort:
                    if smart_letter in available:
                        return smart_letter
                return None

            else:
                return random.choice(available)


#
# oluchi = GuessNaija('oluchi')
# print(oluchi.name)