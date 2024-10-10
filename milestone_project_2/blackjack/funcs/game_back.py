import classes.deck as deck
import classes.dealer as dealer
import classes.player as player
import os

def game_initialize():
    my_deck = deck.Deck()
    my_deck.shuffle()
    player_name = input("Define your nickname: ")
    my_player = player.Player(player_name)
    my_dealer = dealer.Dealer()
    return my_deck, my_player, my_dealer

def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--------------🎰- DON's CASINO -🎰--------------")
    print("Welcome to the Don's Casino!")
    print("Today, we have Blackjack available. Do you want to play it?")
    decision = input("[Y/N]: ")
    if decision.capitalize() == "Y":
        print("Perfect! Let's play it.")
    elif decision.capitalize() == "N":
        print("Hm, I don't care. We will play it the same way.")
    else:
        print("Are you dumb? The options were Y or N. We will play it the same way.")
    print('-------🪙-------🪙-------🪙-------🪙-------')

def game_firstcards(my_player,my_dealer,my_deck):
    for x in range(2):
        my_player.add_card(my_deck.cards)
        my_deck.pop()
        my_dealer.add_card(my_deck.cards)
        my_deck.pop()
    return None

def player_currency(my_player):
    print(f"{my_player.name}"+"'s current ballance: $"+f"{my_player.ballance}")

def new_round(player_obj,dealer_obj):
    my_deck = deck.Deck()
    my_deck.shuffle()
    player_obj.hand = []
    dealer_obj.hand = []
    return my_deck

def card_reveal(person):
    print("\n")
    print(f"--------🔮 Revealing {person.name}'s Cards 🔮--------")
    for cards in range(len(person.hand)):
        print(f"{person.hand[cards]}")

def current_sum(my_person):
    cards_sum = 0
    for x in range(len(my_person.hand)):
        cards_sum += my_person.hand[x].value
    return cards_sum

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
