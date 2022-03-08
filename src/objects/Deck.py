from src.objects.Card import Card
import random


class Deck:
    cards = []

    def __init__(self):
        self.init_cards()

    def init_cards(self):
        ### Generate a base 52 card deck ###
        for suit in range(1,5):
            for value in range(1,14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        ### Randomize the order of all cards in deck ###
        random.shuffle(self.cards)
    
    def deal_one_card(self):
        ### Remove the first element of the deck and return its value ###
        return self.cards.pop(0)
