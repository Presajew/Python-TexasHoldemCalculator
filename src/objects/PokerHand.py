class PokerHand:    
    cards = []

    def __init__(self):
        pass

    def put_card_in_hand(self, card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards = []
