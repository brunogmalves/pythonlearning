'''
Instantiating a new deck, with 52 possible card objects
'''
import card
import random

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in card.suits:
            for rank in card.ranks:
                '''
                Creating the Card Object
                '''
                created_card = card.Cards(rank,suit)

                self.all_cards.append(created_card)
        print(100*"\n")
    
    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):

        return self.all_cards.pop()
    
my_deck = Deck()
my_deck.shuffle()
