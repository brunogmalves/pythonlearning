import os
def board_draw(play_options):
    two_bars = '     |       |     '
    underline_twobars = '_____|_______|_____'
    board_list = [two_bars,'  '+play_options[7]+'  |   '+play_options[8]+'   |  '+play_options[9],underline_twobars,
    two_bars,'  '+play_options[4]+'  |   '+play_options[5]+'   |  '+play_options[6],underline_twobars,
    two_bars,'  '+play_options[1]+'  |   '+play_options[2]+'   |  '+play_options[3],two_bars]

    for num in range(len(board_list)):
        print(board_list[num])



#       |       |
#       |       |
#   ____|_______|_____
#       |       |
#       |       |
#   ____|_______|_____
#       |       |
#       |       |
#       |       |
#    
#          
