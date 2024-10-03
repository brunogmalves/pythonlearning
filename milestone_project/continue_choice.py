def continue_choice():

    possibilities = ['Y','N']
    continue_playing = input("Do you wish to continue playing? [Y or N]: ")

    while continue_playing.capitalize() not in possibilities:
        continue_playing = input("Please, select some valid option [Y/N]: ")
    
    return continue_playing
