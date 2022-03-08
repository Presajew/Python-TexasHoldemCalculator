from src.enums.CardSuitEnum import CardSuitEnum
from src.enums.CardValueEnum import CardValueEnum


class Card:

    # Creating a simple object that stores suit and value
    def __init__(self, suit, value) -> None:
        self.suit = CardSuitEnum(suit)
        self.value = CardValueEnum(value)

    def __str__(self) -> str:
        return f'{self.value.name} of {self.suit.name}'
