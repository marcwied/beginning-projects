import random


def show_board(board):
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  | ' + board[9])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  | ' + board[6])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  | ' + board[3])
    print('     |     |')

def check_space(board, position):
    return board[position] == ' '

def check_for_full_board(board):
    for x in range(1,10):
        if check_space(board, x):
            return False
    return True

def check_for_winner(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or   # across bottom
            (board[4] == marker and board[5] == marker and board[6] == marker) or   # across middle
            (board[7] == marker and board[8] == marker and board[9] == marker) or   # across top
            (board[1] == marker and board[4] == marker and board[7] == marker) or   # vertical left
            (board[2] == marker and board[5] == marker and board[8] == marker) or   # vertical middle
            (board[3] == marker and board[6] == marker and board[9] == marker) or   # vertical right
            (board[1] == marker and board[5] == marker and board[9] == marker) or   # diagonal up
            (board[7] == marker and board[5] == marker and board[3] == marker))     # diagonal down


def select_marker():
    marker = ' '

    while not (marker == 'X' or marker == 'O'):
        marker = input("Please select your Marker, either 'X' or 'O' ").upper()
        if marker == "X":
            print('')
            print("Player 1 is X and Player 2 is O")
            return ('X','O')
        elif marker == "O":
            print('')
            print("Player 1 is O and Player 2 is X")
            return ('O', 'X')
        else:
            print("Please make a valid entry")
            continue

def place_marker(board, marker, position):
    board[position] = marker

def choose_position(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9]:

        try:
            position = int(input('Choose your position: '))
        except ValueError:
            print("Invalid Entry, use 1-9")
            continue

        if position not in range(1,10):
            print("Invalid Entry, use 1-9")
            continue

        elif not check_space(board, position):
            print("Space not available")
            print(' ')
            position = 0
            continue
    return position

def goes_first():
    if random.randint(1,2) == 1:
        print("Player 1 is first")
        return 'Player 1'
    else:
        print("Player 2 is first")
        return 'Player 2'



# Game Engine

gameboard = [' '] *10
show_board(gameboard)
player1, player2 = select_marker()
turn = goes_first()

while True:
    if turn == 'Player 1':
        print("Its Player 1s turn")
        position = choose_position(gameboard)
        place_marker(gameboard,player1, position)
        show_board(gameboard)
        if check_for_winner(gameboard, player1):
            print("Player 1 wins! ")
            break
        elif check_for_full_board(gameboard):
            print(" Tie.")
            break
        turn = 'Player 2'


    else:
        print("Its Player 2s turn")
        position = choose_position(gameboard)
        place_marker(gameboard, player2, position)
        show_board(gameboard)
        if check_for_winner(gameboard, player2):
            print("Player 2 wins! ")
            break
        elif check_for_full_board(gameboard):
            print(" Tie.")
            break
        turn = 'Player 1'