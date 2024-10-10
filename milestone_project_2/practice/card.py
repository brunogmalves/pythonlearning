'''
Defining the card class that will be used in order to create the basic component of the War Game
'''

values = {"Two":2,
          "Three":3,
          "Four":4,
          "Five":5,
          "Six":6,
          "Seven":7,
          "Eight":8,
          "Nine":9,
          "Ten":10,
          "Jack":11,
          "Queen":12,
          "King":13,
          "Ace":14}
ranks = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
suits = ("Clubs","Hearts","Spades","Diamonds")

class Cards():
    '''
    Class to build a card with a value and a suit
    '''
    def __init__(self,rank,suit):
        '''
        Constructor
        '''
        self.rank   = rank
        self.suit   = suit
        self.value  = values[rank]

    def __str__(self):
        '''
        Making it possible to print something instead of memory address
        '''
        return f"{self.rank}" + " of " + f"{self.suit}"
    
