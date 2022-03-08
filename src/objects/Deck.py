from src.objects.Card import Card
import random


class Deck:
    
    cards = []

    # create a deck of cards 
    # inits with 52 unique combinations
    def __init__(self):
        self.init_cards()


    def init_cards(self):
        for suit in range(0,4):
            for value in range(0,14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)
