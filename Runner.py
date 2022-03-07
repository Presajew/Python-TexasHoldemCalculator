from src.objects.Card import Card


def main():
    
    # Simple test to verify Card object is functional
    test_card = Card('Hearts', '7')
    print(f'The card value is {test_card.value} and the suit of the card is {test_card.suit}.')


if __name__ == '__main__':
    main()