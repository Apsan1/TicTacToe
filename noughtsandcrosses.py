'''
    This program is a game of noughts and crosses. The user plays against the computer.
    The computer chooses a random cell to place its nought in.
    The user chooses a cell to place its cross in.
    The user can choose to save the score to a file, or load the scores from a file.
    The scores are stored in a dictionary, with the key being the name of the player,
    and the value being the score. The scores are saved to a file in JSON format.
'''
import random
import json
random.seed()


def draw_board(board):
    '''
        This function draws the board. It takes the board as a parameter.
        The board is a list of lists, with each inner list representing a row.
        The function prints the board to the screen.
    '''
    print('\n------------------------------------\n')
    print(
        f"|  {board[0][0]}      |     {board[0][1]}      |    {board[0][2]}      |")
    print("     ------------------------")
    print(
        f"|  {board[1][0]}      |     {board[1][1]}      |    {board[1][2]}      |")
    print("     ------------------------")
    print(
        f"|  {board[2][0]}      |     {board[2][1]}      |    {board[2][2]}      |")
    print('\n------------------------------------')


def welcome(board):
    '''
        This function prints the welcome message and draws the board.
        It takes the board as a parameter.
    '''
    print("---------------Welcome to Tic Tac Toe---------------\n\n")
    draw_board(board)


def initialise_board(board):
    '''
        This function initialises the board to all single spaces ' '.
        It takes the board as a parameter.
        It returns the board.
    '''
    board = [[' '] * 3 for i in range(3)]
    return board


def get_player_move(board):
    '''
        This function asks the user for the cell to put the X in.
        It takes the board as a parameter.
        It returns the row and column of the cell.
    '''
    try:
        row = int(input('Enter row number between 0-2 : '))
        col = int(input('Enter column number between 0-2 to place X : '))
        if row < 0 or row > 2 or col < 0 or col > 2:
            raise ValueError()
        if board[row][col] != ' ':
            raise ValueError()
    except ValueError:
        print('Invalid input. Please enter a number between 0 and 2.')
        return get_player_move(board)
    return row, col


def choose_computer_move(board):
    '''
        This function chooses a random cell to put the O in.
        It takes the board as a parameter.
        It returns the row and column of the cell.
    '''
    free_space = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                free_space.append((i, j))
    if free_space:
        row, col = random.choice(free_space)
    return row, col



def check_for_win(board, mark):
    '''
        This function checks if the player or the computer has won.
        It takes the board and the mark as parameters.
        It returns True if the player or the computer has won, False otherwise.
    '''
    for i in range(3):
        if board[i][0] == mark and board[i][1] == mark and board[i][2] == mark:
            return True
        if board[0][i] == mark and board[1][i] == mark and board[2][i] == mark:
            return True

    if board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    if board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True

    return False


def check_for_draw(board):
    '''
        This function checks if the game is drawn.
        It takes the board as a parameter.
        It returns True if the game is drawn, False otherwise.
    '''
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def play_game(board):
    '''
        This function plays the game.
        It takes the board as a parameter.
        It returns 1 if the player wins, -1 if the computer wins, 0 if the game is drawn.
    '''
    board = initialise_board(board)
    welcome(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = "X"
        if check_for_win(board, "X"):
            print("You won!!!!!")
            return 1
        if check_for_draw(board):
            print("It has been draw")
            return 0

        row, col = choose_computer_move(board)
        board[row][col] = "O"
        draw_board(board)
        if check_for_win(board, "O"):
            print("The computer won.")
            return -1
        if check_for_draw(board):
            print("It's a draw.")
            return 0


def menu():
    '''
        This function displays the menu and asks the user for a choice.
        It returns the choice.
    '''
    print(' \n\n-------------------- Menu--------------------\n ')
    print('1 - Start The Game')
    print('2 - Save Your Score')
    print('3 - View Scoreboard')
    print('q - Stop Playing')
    choice = input('Enter what would you like to do: ')
    return choice


def load_scores():
    '''
        This function loads the scores from the file 'leaderboard.txt'.
        It returns the scores in a Python dictionary with the player names
        as key and the scores as values.
    '''
    with open('leaderboard.txt', 'r',encoding="utf-8") as file:
        json_string = file.read()

    # Convert the JSON string into a Python dictionary
    leaders = json.loads(json_string)
    return leaders

def save_score(score):
    '''
        This function saves the score to the file 'leaderboard.txt'.
        It takes the score as a parameter.
    '''
    name = input('Enter your name: ')
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w',encoding="utf-8") as file:
        json_string = json.dumps(leaders)
        file.write(json_string)
    return leaders

def display_leaderboard(leaders):
    '''
        This function displays the leaderboard scores.
        It takes the leaderboard scores as a parameter.
    '''
    print('Leaderboard')
    for name, score in leaders.items():
        print(f" {name}: {score}")
