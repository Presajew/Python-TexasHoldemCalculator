class PokerHand:    
    cards = []

    def __init__(self):
        pass

    def __str__(self) -> str:
        hand = ''
        for card in self.cards:
            hand += f'{str(card)}\n'
        return hand

    def put_card_in_hand(self, card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards = []
