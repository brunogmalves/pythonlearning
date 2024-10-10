
def play_again():
    control = 0
    continue_choice = input("Do you want to play again? [Y/N]: ")
    
    while control == 0:
        if continue_choice.capitalize() == "Y":
            another_round = True
            control = 1
        elif continue_choice.capitalize() == "N":
            another_round = False
            control = 1
        else:
            print("I did not understand.")
            continue_choice = input("Do you want to play again? [Y/N]: ")
    return another_round

def winner(player_obj,dealer_obj):
    if player_obj > 21:
        winner = "dealer"
    if player_obj <= 21:
        if dealer_obj > 21:
            winner = "player"
        elif player_obj > dealer_obj and dealer_obj < 21:
            winner = "player"
        elif player_obj == dealer_obj:
            winner = "draw"
        elif dealer_obj > player_obj:
            winner = "dealer"
    if winner == "dealer":
        print("Woops... You've lost the game.")
    elif winner == "player":
        print("Wow! You're lucky. You've duplicated your bet.")    
    elif winner == "draw":
        print("Incredible! We got the same sum. Not for me, neither for you. Take your bet back.")    
    return winner

def prize(winner,bet):
    if winner == "player":
        payout = 2*bet
    elif winner == "draw":
        payout = bet
    elif winner == "dealer":
        payout = 0
    return payout

def ace_verification(person_obj,person_sum):
    if person_sum > 21:
        for x in range(len(person_obj.hand)):
            if person_obj.hand[x].value == 11:
                person_obj.hand[x].value = 1

def gameover_verify(person_object):
    if person_object.ballance == 0:
        print("I am sorry. You are out of money. Now...")
        print("GET OUT OF HERE!!!")
        return True
    else:
        return False
    