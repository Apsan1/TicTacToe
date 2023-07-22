'''
This is the main module for the game. It contains the main function
which calls the welcome function to display the welcome message.
'''
from noughtsandcrosses import welcome, menu, play_game, save_score, load_scores, display_leaderboard

def main():
    '''
    This is the main function for the game. It calls the welcome function
    to display the welcome message, then it calls the menu function to
    display the menu and get the user's choice. If the user chooses to
    play the game, it calls the play_game function to play the game.
    If the user chooses to save the score, it calls the save_score
    function to save the score. If the user chooses to display the
    leaderboard, it calls the load_scores function to load the scores
    from the file and the display_leaderboard function to display the
    leaderboard.
    '''
    board =  [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return


# Program execution begins here
if __name__ == '__main__':
    main()
