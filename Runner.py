from src.objects.Player import Player
from src.objects.Deck import Deck


def main():
    
    # Simple test to verify Deck object is functional
    deck = Deck()
    print(f'\nInit Deck (Size: {len(deck.cards)})')
    print(str(deck))

    # Test the Shuffle Functionality
    deck.shuffle()
    print(f'\nShuffle Deck (Size: {len(deck.cards)})')
    print(str(deck))

    # Test dealing 2 cards into a hand
    player = Player("Dude", 500)
    player.hand.put_card_in_hand(deck.deal_one_card()) 
    player.hand.put_card_in_hand(deck.deal_one_card())
    print("\nPlayer")
    print(str(player))
    print(f'Deck Size: {len(deck.cards)}')


if __name__ == '__main__':
    main()
