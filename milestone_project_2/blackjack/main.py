'''Main function to play blackjack.'''
import funcs.game_back as game_back
import funcs.verifications as verifications
import funcs.player_actions as player_actions
import time

# Global Variables.
possible_decisions = ("Hit","Stay","None")
continue_option = True
round_finished = False
no_money = False
action = "None"

# Instantiating fundamental objects.
my_deck, my_player, my_dealer = game_back.game_initialize()

# Initializing Casino.
game_back.welcome()

# Initializing game loop
while continue_option == True and no_money == False:
    # Display the current player currency
    game_back.player_currency(my_player)
    # Ask for the player to set a bet
    bet_value = player_actions.bet(my_player)

    # Round started
    round_finished = False
    # Distributing the first cards.
    game_back.game_firstcards(my_player,my_dealer,my_deck)
    print('-------♥️-------♠️-------♦️-------♣️-------')
    print(f"Player's Initial Cards: {my_player.hand[0]}" + " and " + f"{my_player.hand[1]}")
    print(f"Dealer's Initial Card: {my_dealer.hand[0]}")


    while round_finished == False:
        # Summing the initial value of both initial cards.
        player_initial_sum = game_back.current_sum(my_player)

        # If the first two cards are equal 21, the player receives 2.0x the bet
        if player_initial_sum == 21:
            print("Wow! The sum is equal 21. You've won 2x your bet.")
            payout = 3*bet_value
            my_player.change_money(payout)
            print(f"Your new ballance is equal ${my_player.ballance}")
            round_finished = True
        
        elif player_initial_sum != 21:
            player_sum = game_back.current_sum(my_player)

            while action != "Stay" and player_sum < 21:
                current_action = input(f"Mr. / Mrs. {my_player.name}, please, choose an action. [HIT or STAY]: ")

                if current_action.capitalize() == possible_decisions[0]:
                    player_actions.hit(my_player,my_deck)
                    action = possible_decisions[0]
                    player_sum = game_back.current_sum(my_player)
                    current_action = possible_decisions[2]
                    if player_sum > 21:
                        verifications.ace_verification(my_player,player_sum)
                    player_sum = game_back.current_sum(my_player)
                    print("Now, you have in your hand:",end=" ")
                    for x in range(len(my_player.hand)):
                        print(f"{my_player.hand[x]}",end=", ")
                    print("\n")

                elif current_action.capitalize() == possible_decisions[1]:
                    action = possible_decisions[1]
                    round_finished = True
                    player_sum = game_back.current_sum(my_player)
                    current_action = possible_decisions[2]
                    if player_sum > 21:
                        verifications.ace_verification(my_player,player_sum)
                    player_sum = game_back.current_sum(my_player)

                else:
                    current_action = possible_decisions[2]

                if player_sum >= 21:
                    break

            if player_sum > 21:
                print("\n"+"Woops. You've busted.")
                winner = "dealer"
                round_finished = True
            
            player_sum = game_back.current_sum(my_player)
            dealer_sum = game_back.current_sum(my_dealer)
            dealer_cards = 2

            while dealer_sum <= 16:
                player_actions.hit(my_dealer,my_deck)
                dealer_sum = game_back.current_sum(my_dealer)
                if dealer_sum > 21:
                    verifications.ace_verification(my_dealer,dealer_sum)
                dealer_sum = game_back.current_sum(my_dealer)
                dealer_cards += 1
                print(my_dealer.hand[dealer_cards-1])

            game_back.card_reveal(my_player)
            print(f"Player's sum = {player_sum}")

            game_back.card_reveal(my_dealer)
            print(f"Dealer's sum = {dealer_sum}")

            winner = verifications.winner(player_sum,dealer_sum)

            payout = verifications.prize(winner,bet_value)
            my_player.change_money(payout)
            round_finished = True
        
        no_money = verifications.gameover_verify(my_player)

        if round_finished == True and no_money == False:
            continue_option = verifications.play_again()

        if continue_option == True:
            payout = 0
            action = possible_decisions[2]
            my_deck = game_back.new_round(my_player,my_dealer)

        elif continue_option == False and no_money == False:
            game_back.clear_screen()
            print(f"Your final ballance is ${my_player.ballance}")
            print("Thank you for playing!")

