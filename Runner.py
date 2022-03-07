from src.objects.Deck import Deck


def main():
    
    # Simple test to verify Deck object is functional
    deck = Deck()
    for card in deck.cards:
        print(f'Suit:{card.suit} Value:{card.value}')


if __name__ == '__main__':
    main()