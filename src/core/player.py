class Player():
    def __init__(self, name):
        self.name = name
        self.player_turn = None
        self.combinations = {'Ones': None,
                             'Twos': None, 
                             'Threes': None,
                             'Fours': None,
                             'Fives': None,
                             'Sixes': None,
                             'Bonus': None,
                             '3 of kind': None,
                             '4 of kind': None,
                             'Full house': None,
                             'Small Straight': None,
                             'Large Straight': None,
                             'Yahtzee': None,
                             'Chance': None,
                             'Yahtzee_bonus': None}