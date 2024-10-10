
def hit(person_obj,deck_obj):
    print(f"*Adding {person_obj.name}'s hand one more card*")
    person_obj.add_card(deck_obj.cards)
    deck_obj.pop()

def bet(myplayer):
    verify_value = False
    while verify_value == False:
        try:
            value = int(input("Gentleman, please, set your bet: "))
            if value > 0 and value <= myplayer.ballance:
                verify_value = True
            else:
                print(f"It is not possible to play with this value. Try again with a value between $1 and ${myplayer.ballance}")
        except:
            print(f"I am sorry. It is not possible to bet this value. Try again with a value between $1 and ${myplayer.ballance}")
    myplayer.change_money(-value)
    #Indicating the current bet and the player's ballance
    print(f"Current bet value: ${value}")
    print(f"This way, your current balance is ${myplayer.ballance}")
    return value
