from src.objects.PokerHand import PokerHand
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
    hand = PokerHand()
    hand.put_card_in_hand(deck.deal_one_card()) 
    hand.put_card_in_hand(deck.deal_one_card())
    print("\nHand")
    print(str(hand))
    print(f'Deck Size: {len(deck.cards)}')


if __name__ == '__main__':
    main()
