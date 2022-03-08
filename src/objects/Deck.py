from src.objects.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.init_cards()

    def __str__(self) -> str:
        deck = ''
        for card in self.cards:
            deck += f'{str(card)}\n'
        return deck

    def init_cards(self) -> None:
        ### Generate a base 52 card deck ###
        for suit in range(1,5):
            for value in range(1,14):
                self.cards.append(Card(suit, value))

    def shuffle(self) -> None:
        ### Randomize the order of all cards in deck ###
        random.shuffle(self.cards)
    
    def deal_one_card(self) -> Card:
        ### Remove the first element of the deck and return its value ###
        return self.cards.pop(0)
