from src.enums.PlayerType import PlayerType
from src.objects.PokerGame import PokerGame
from src.objects.Player import Player


def main():

    # Create a game with 6 players
    game = PokerGame(50)
    game.deck.shuffle()
    game.add_player(Player(f"HUMAN", PlayerType.HUMAN, 1000))
    for x in range(1, 6):
        game.add_player(Player(f"CPU_{x}", PlayerType.COMPUTER, 1000))
    print(str(game))

    # Loop game until end condition is reached
    while True:
        game.play_one_round()
        if game.is_game_over():
            break


if __name__ == "__main__":
    main()
