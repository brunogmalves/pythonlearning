def choose_position(player,play_options):
    
    ask_pos = input(f'Player {player+1}, on which position you want to play? [1 - 9]: ')
    control = 0

    while control == 0: 
        if ask_pos.isdigit():
            if int(ask_pos) in range(1,10) and play_options[int(ask_pos)] == ' ':
                control = 1
            elif int(ask_pos) in range(1,10) and play_options[int(ask_pos)] != ' ':
                ask_pos = input(f'Player {player+1}, position is already fulfilled. On which position you want to play? [1 - 9]: ')
            else:
                ask_pos = input(f'Player {player+1}, the value is outside of the range. On which position you want to play? [1 - 9]: ')
        else:
            ask_pos = input(f'Player {player+1}, the entered value is not accepted. On which position you want to play? [1 - 9]: ')
    return int(ask_pos)
