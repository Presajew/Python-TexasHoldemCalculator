from xmlrpc.client import boolean
from src.objects.PokerHand import PokerHand
from src.objects.Deck import Deck


class PokerGame:
    def __init__(self) -> None:
        self.deck = Deck()
        self.players = []
        self.table_cards = PokerHand()
        self.ante = 50

    def __str__(self) -> str:
        output = "Game Overview\n-------------\n"
        output += f"Table Cards\n{str(self.table_cards)}\n\n"
        for player in self.players:
            output += str(player)
        return output

    def add_player(self, player) -> None:
        self.players.append(player)

    def get_active_players(self) -> list:
        # return a list of players that are still in the round
        return list(filter(lambda p: p.active == True, self.players))

    def pre_round_check(self):
        # check if each player wants to play or sit out the round
        # collect ante if player is active
        for player in self.players:
            player.collect_ante(self.ante)

    def deal_hands(self) -> None:
        # deal first card to each player
        for player in self.get_active_players():
            player.hand.put_card_in_hand(self.deck.deal_one_card())
        # deal second card to each player
        for player in self.get_active_players():
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

    def round_of_bets(self) -> None:
        pass

    def is_game_over(self) -> boolean:
        # prevent infinite loop for now
        return True

    def play_one_round(self) -> None:
        self.pre_round_check()
        self.deal_hands()
        print(str(self))

        self.round_of_bets()
        self.deal_flop()
        print(str(self))

        self.round_of_bets()
        self.deal_river()
        print(str(self))

        self.round_of_bets()
        self.deal_turn()
        print(str(self))

        self.round_of_bets()
        self.end_round()
        print(str(self))
