from src.objects.PokerGame import PokerGame
from src.objects.Player import Player
from src.objects.Deck import Deck


def main():

    # Create a game with 6 players
    game = PokerGame()
    game.deck.shuffle()
    for x in range(1, 7):
        game.add_player(Player(f"Player{x}", 1000))
    print(str(game))

    game.deal_hands()
    print(str(game))

    game.deal_flop()
    print(str(game))

    game.deal_river()
    print(str(game))

    game.deal_turn()
    print(str(game))

    game.end_round()
    print(str(game))


if __name__ == "__main__":
    main()
