from game_init import game_init
from board_draw import board_draw
from choose_position import choose_position
from player_round import player_round
from final_check import final_check

continue_play = 'Y'
round_counter, play_options, symbol_list = game_init()


while continue_play.capitalize() == 'Y':
    player = player_round(round_counter)                                        #Defines which player is playing the current round
    list_pos = choose_position(player,play_options)                             #Ask on which position the current player want to insert X or O
    play_options[list_pos] = symbol_list[player]                                #Insert, at the chosen position, the right character
    board_draw(play_options)
    play_options,continue_play = final_check(play_options,player)
    round_counter += 1
