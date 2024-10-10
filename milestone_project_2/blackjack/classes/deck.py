'''This class is responsable for the creation of a deck of cards, making all the possible combinations between the cards ranks and suits'''

import random

'''This class defines the possible cards ranks, and suits, as well making possible to create an object Card.'''

values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
suits = ("Clubs","Hearts","Spades","Diamonds")

class Card():

    def __init__(self,rank,suit) -> None:
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self) -> str:
        return f"{self.rank}" + " of " + f"{self.suit}"
    
class Deck():
    def __init__(self) -> None:
        '''Constructor method, that will combine all the possible cards'''
        self.cards = []
        for rank in values:
            for suit in suits:
                self.cards.append(Card(rank,suit))

    def __str__(self) -> str:
        return f"Your current deck has {len(self.cards)} cards"

    def shuffle(self):
        ''' Shuffling all the cards '''
        return random.shuffle(self.cards)
    
    def pop(self):
        ''' Popping the first card of the deck'''
        return self.cards.pop(0)