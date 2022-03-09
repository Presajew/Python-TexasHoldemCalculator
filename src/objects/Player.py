from src.objects.PokerHand import PokerHand


class Player:
    def __init__(self, name, bank) -> None:
        self.name = name
        self.bank = bank
        self.hand = PokerHand()

    def __str__(self) -> str:
        return f"{self.name}\nBank: {self.bank}\nHand: {str(self.hand)}\n\n"
