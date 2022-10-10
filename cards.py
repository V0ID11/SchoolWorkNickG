import random


class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number: int) -> None:
        self._card_number = number

    def get_suit(self) -> str:
        suit = self._card_number / 13
        suits = ['S','H','D','C']
        return [suits[int(suit)]]
        

    def get_value(self) -> str:
        number = (self._card_number % 13) 
        numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return numbers[number]
        
        

    def get_short_name(self) -> str:
        return (self.get_suit(), self.get_value())

    def get_long_name(self) -> str:
        """ return card name eg 'Ten of Diamonds' """
        suits = ['Spades','Hearts','Diamonds','Clubs']
        numbers = ['Ace','Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine','Ten','Jack', 'Queen', 'King']
        return numbers[(self._card_number % 13)], "of", suits[self._card_number//13]


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self)-> None:
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self) -> int:
        """ returns the number of cards still in the deck """
        return len(self._card_list)

    def shuffle_deck(self) -> None:
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self) -> Card:
        """ removes the top card from the deck and returns it (as a card object) """
        return self._card_list.pop()

card = Card(1)
print(card.get_suit())
deck = Deck()   
deck.shuffle_deck()
for _ in range(deck.length()):
    card = deck.take_top_card()
    print(card.get_long_name())
