from src.objects.Card import Card


class Deck:
    
    cards = []

    # create a deck of cards 
    # inits with 52 unique combinations
    def __init__(self):
        self.init_cards()

    # TODO: implement enums
    def init_cards(self):
        for suit in range(0,4):
            for value in range(0,14):
                self.cards.append(Card(suit, value))