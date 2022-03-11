from enums.CardValueEnum import CardValueEnum
from src.enums.CardSuitEnum import CardSuitEnum
from src.enums.PokerHandEnum import PokerHandEnum


class PokerHandValueCalculator:

    # cards size will vary between 2, 5, 6, and 7
    def __init__(self, cards):
        self.cards = cards
        # TODO: store the 5 best card hand in this value
        self.best_hand = []

    def get_hand_value(self) -> PokerHandEnum:
        if self.is_royal_flush():
            return PokerHandEnum.ROYAL_FLUSH
        elif self.is_straight_flush():
            return PokerHandEnum.STRAIGHT_FLUSH
        elif self.is_four_of_a_kind():
            return PokerHandEnum.FOUR_OF_A_KIND
        elif self.is_full_house():
            return PokerHandEnum.FULL_HOUSE
        elif self.is_flush():
            return PokerHandEnum.FLUSH
        elif self.is_straight():
            return PokerHandEnum.STRAIGHT
        elif self.is_three_of_a_kind():
            return PokerHandEnum.THREE_OF_A_KIND
        elif self.is_two_pair():
            return PokerHandEnum.TWO_PAIR
        elif self.is_one_pair():
            return PokerHandEnum.ONE_PAIR
        else:
            return PokerHandEnum.HIGH_CARD

    def is_royal_flush(self) -> bool:
        pass

    def is_straight_flush(self) -> bool:
        pass

    def is_four_of_a_kind(self) -> bool:
        # must have at least 4 cards
        if len(self.cards) < 4:
            return False
        # if 4 cards have the same value, return true
        values = [card.value for card in self.cards]
        for value in CardValueEnum:
            if values.count(value) >= 4:
                return True
        return False

    def is_full_house(self) -> bool:
        pass

    def is_flush(self) -> bool:
        # must have at least 5 cards
        if len(self.cards) < 5:
            return False
        # if 5 cards in the cards array share the same suit, return true
        suits = [card.suit for card in self.cards]
        for suit in CardSuitEnum:
            if suits.count(suit) >= 5:
                return True
        return False

    def is_straight(self) -> bool:
        pass

    def is_three_of_a_kind(self) -> bool:
        # must have at least 3 cards
        if len(self.cards) < 3:
            return False
        # if 3 cards have the same value, return true
        values = [card.value for card in self.cards]
        for value in CardValueEnum:
            if values.count(value) >= 3:
                return True
        return False

    def is_two_pair(self) -> bool:
        pass

    def is_one_pair(self) -> bool:
        # must have at least 2 cards
        if len(self.cards) < 2:
            return False
        # if 4 cards have the same value, return true
        values = [card.value for card in self.cards]
        for value in CardValueEnum:
            if values.count(value) >= 2:
                return True
        return False
