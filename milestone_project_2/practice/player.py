import deck

class Player:

    def __init__(self,name) -> None:

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        '''
        Adding cards
        '''

        # For multiple card object
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)

        # Handling string inputs
        elif type(new_cards) == str:
            print("It is not possible to add this number of card to the deck.")
        
        # For a single card object
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
