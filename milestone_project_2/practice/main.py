import card
import deck
import player

round_num = 0
game_on = True

# Game Setup

player_one = player.Player("One")
player_two = player.Player("Two")

new_deck = deck.Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One, out of cards!")
        print("Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards!")
        print("Player One Wins!")
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if (player_one_cards[-1].value) > (player_two_cards[-1].value):
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif (player_two_cards[-1].value) > (player_one_cards[-1].value):
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        else:
            print("War!")

            if len(player_one.all_cards) < 5:
                print("Player one unable to declar war.")
                print("Player two wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player two unable to declar war.")
                print("Player one wins!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
    