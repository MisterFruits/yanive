class Game(object):
    """The Yanive game"""
    def __init__(self):
        super(Game, self).__init__()

    def deals():
        pass

    def shuffle():
        pass

    def gather_up():
        pass


class Trick(object):
    """A trick of cards"""
    def __init__(self):
        super(Trick, self).__init__()

    def show_pickable_cards():
        pass


class Player(object):
    """A player of Yanive"""
    def __init__(self):
        super(Player, self).__init__()

    def underplay(self):
        pass

    def pick_up(self):
        pass

    def say_yanive(self, game):
        pass

    def show_cards(self):
        pass


class Card(object):
    """A card from a game card"""
    def __init__(self):
        super(Card, self).__init__()
        pass

    def is_adjacent():
        pass

    def is_equal():
        pass


class ScoresHolder(object):
    """A stocks and process yanive scores"""
    def __init__(self):
        super(ScoresHolder, self).__init__()

    def append(self, newScore):
        pass

    def process():
        pass
