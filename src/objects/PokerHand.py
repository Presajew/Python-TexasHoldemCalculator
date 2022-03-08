class PokerHand:    
    def __init__(self) -> None:
        self.cards = []

    def __str__(self) -> str:
        hand = ''
        for card in self.cards:
            hand += f'{str(card)}'
            if self.cards.index(card) != (len(self.cards) - 1):
                hand += ', '
        return hand

    def put_card_in_hand(self, card) -> None:
        self.cards.append(card)

    def clear_hand(self) -> None:
        self.cards = []
