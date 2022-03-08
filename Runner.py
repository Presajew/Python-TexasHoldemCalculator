from this import d
from src.objects.PokerHand import PokerHand
from src.objects.Deck import Deck


def main():
    
    # Simple test to verify Deck object is functional
    deck = Deck()
    print(f'\nInit Deck (Size: {len(deck.cards)})')
    for card in deck.cards:
        print(f'Suit:{card.suit} Value:{card.value} Index:{deck.cards.index(card)}')

    # Test the Shuffle Functionality
    deck.shuffle()
    print(f'\nShuffle Deck (Size: {len(deck.cards)})')
    for card in deck.cards:
        print(f'Suit:{card.suit} Value:{card.value}')

    # Test dealing 2 cards into a hand
    hand = PokerHand()
    hand.put_card_in_hand(deck.deal_one_card()) 
    hand.put_card_in_hand(deck.deal_one_card())
    print("\nHand")
    for card in hand.cards:
        print(f'Suit:{card.suit} Value:{card.value}')
    print(f'Deck Size: {len(deck.cards)}')


if __name__ == '__main__':
    main()