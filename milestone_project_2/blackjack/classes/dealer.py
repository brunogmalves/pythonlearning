'''This class is responsable to create the object, with all the necessary methods'''

class Dealer():
    def __init__(self) -> None:
        self.name = "Dealer"
        self.hand = []

    def __str__(self) -> str:
        return f"Hey! My name is {self.name} and I am the dealer."

    def add_card(self,deck):
        self.hand.append(deck[0])
