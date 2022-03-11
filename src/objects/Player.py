from src.enums.PlayerType import PlayerType
from src.objects.PokerHand import PokerHand


class Player:
    def __init__(self, name, type, bank) -> None:
        self.name = name
        self.bank = bank
        self.type = type
        self.active = True
        self.hand = PokerHand()

    def __str__(self) -> str:
        return f"{self.name}\nBank: {self.bank}\nHand: {str(self.hand)}\n\n"

    def action_fold(self) -> None:
        self.active = False

    def action_check(self) -> None:
        pass

    def action_bet(self, amount) -> None:
        pass

    def action_call(self) -> None:
        pass

    def action_raise(self, amount) -> None:
        pass

    def collect_ante(self, ante) -> None:
        # prompt human players if they want to play round
        # deduct the ante amount if they choose to play
        # for computer players, always play round
        if self.type == PlayerType.HUMAN:
            answer = input(f"Would {self.name} like to play this round (y/n)?")
            if answer == "n":
                self.active = False
            else:
                self.bank -= ante
        else:
            self.bank -= ante
