'''In this class, the players will be created and also capable to take more cards or do any action'''

class Player():
    def __init__(self,name) -> None:
        self.name = name
        self.hand = []
        self.ballance = 1000

    def __str__(self) -> str:
        return "Player's name: " + f"{self.name}"

    def add_card(self,deck):
        self.hand.append(deck[0])

    def change_money(self,coin):
        self.ballance += coin

    def check_balance(self):
        print(f"The actual player's ballance is ${self.ballance}")