from continue_choice import continue_choice

def final_check(play_options,player):
    won_control = 0
    first_line = (play_options[1] == play_options[2] == play_options[3] != ' ')
    second_line = (play_options[4] == play_options[5] == play_options[6] != ' ')
    third_line = (play_options[7] == play_options[8] == play_options[9] != ' ')
    first_column = (play_options[1] == play_options[4] == play_options[7] != ' ')
    second_column = (play_options[2] == play_options[5] == play_options[8] != ' ')
    third_column = (play_options[3] == play_options[6] == play_options[9] != ' ')
    first_diagonal = (play_options[1] == play_options[5] == play_options[9] != ' ')
    second_diagonal = (play_options[3] == play_options[5] == play_options[7] != ' ')

    if (first_line or second_line or third_line or first_column or second_column or third_column or first_diagonal or second_diagonal) == True:
        print(f'Congratulations! Player {player+1} won the game!')
        continue_play = continue_choice()
        play_options = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        won_control = 1
    elif play_options[1] != ' ' and play_options[2] != ' ' and play_options[3] != ' ' and play_options[4] != ' ' and play_options[5] != ' ' and play_options[6] != ' ' and play_options[7] != ' ' and play_options[8] != ' ' and play_options[9] != ' ' and won_control == 0:
        print('It is a draw!')
        continue_play = continue_choice()
        play_options = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    else:
        continue_play = 'Y'
    return play_options, continue_play
    