def player_symbol():
    
    possibilities = ['X','O']

    player_sym = input('Player 1, please, define which symbol you want to be. [X or O]: ')
    while player_sym.capitalize() not in possibilities:
        player_sym = input('Hm, this is not supported. Choose between [X or O]: ')
    if player_sym.capitalize() in possibilities:
        if player_sym.capitalize() == 'X':
            player_assignment = ['X','O']
            print(f'Player 1 is {player_assignment[0]}')
            print(f'Player 2 is {player_assignment[1]}')
        else:
            player_assignment = ['O','X']
            print(f'Player 1 is {player_assignment[0]}')
            print(f'Player 2 is {player_assignment[1]}')

    return player_assignment
