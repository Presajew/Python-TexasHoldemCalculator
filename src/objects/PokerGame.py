from src.objects.PokerHand import PokerHand
from src.objects.Deck import Deck


class PokerGame:
    def __init__(self) -> None:
        self.deck = Deck()
        self.players = []
        self.table_cards = PokerHand()

    def __str__(self) -> str:
        output = "Game Overview\n-------------\n"
        output += f"Table Cards\n{str(self.table_cards)}\n\n"
        for player in self.players:
            output += str(player)
        return output

    def add_player(self, player) -> None:
        self.players.append(player)

    def deal_hands(self) -> None:
        # deal first card to each player
        for player in self.players:
            player.hand.put_card_in_hand(self.deck.deal_one_card())
        # deal second card to each player
        for player in self.players:
            player.hand.put_card_in_hand(self.deck.deal_one_card())

    def deal_flop(self) -> None:
        for card in range(0, 3):
            self.table_cards.put_card_in_hand(self.deck.deal_one_card())

    def deal_river(self) -> None:
        self.table_cards.put_card_in_hand(self.deck.deal_one_card())

    def deal_turn(self) -> None:
        self.table_cards.put_card_in_hand(self.deck.deal_one_card())

    def end_round(self) -> None:
        # TODO: Determine Winner
        # TODO: Redistribute Money

        # reset table cards
        self.table_cards.cards = []

        # reset player cards
        for player in self.players:
            player.hand.cards = []

        # reset deck
        self.deck = Deck()
