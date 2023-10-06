import random


def display_board(board):
    print('        |       |')
    print('   ', board[7], '  |  ', board[8], '  |  ', board[9])
    print(" -------|-------|-------")
    print('   ', board[4], '  |  ', board[5], '  |  ', board[6])
    print(" -------|-------|-------")
    print('   ', board[1], '  |  ', board[2], '  |  ', board[3])
    print('        |       |')


def player_input():
    inputted = 'nothinright'

    while (inputted == 'X' or inputted == 'O') == False:

        inputted = input('Player 1, would you like to be X or O: ')

        if (inputted == 'X' or inputted == 'O') == False:
            print(f'No, not {inputted}, X or O')

    return inputted


def place_marker(board, marker, position):
    while (str(position).isdigit() == False) or (0 < int(position) < 10) == False:
        position = input('a digit (1-9) pls: ')

    position = int(position)

    board[position] = marker

def place_marker(board, marker, position):

    while (str(position).isdigit() == False) or (0 < int(position) < 10) == False:
        position = input('a digit (1-9) pls: ')

    position = int(position)

    board[position] = marker


def win_check(board, marker):
    if board[1] == board[2] == board[3] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[7] == board[8] == board[9] == marker:
        return True
    elif board[7] == board[4] == board[1] == marker:
        return True
    elif board[8] == board[5] == board[2] == marker:
        return True
    elif board[9] == board[6] == board[3] == marker:
        return True
    elif board[7] == board[5] == board[3] == marker:
        return True
    elif board[9] == board[5] == board[1] == marker:
        return True
    else:
        return False


def choose_first():
    first = random.randint(1, 2)

    if first == 1:
        return 'Player X goes first!'
    else:
        return 'Player O goes first!'


def space_check(board, position):
    position = int(position)

    if board[position] == ' ':
        return True
    elif board[position] == 'X':
        return False
    else:
        return False


def full_board_check(board):
    if ' ' in board:
        return False
    else:
        print('Draw Game!')
        return True


def player_choice(board):
    position = input('For your next move, which space?: ')

    while (str(position).isdigit() == False) or (0 < int(position) < 10) == False or space_check(board,
                                                                                                 position) == False:
        position = input('for your next move, a digit (1-9) pls on an open space: ')

    position = int(position)

    if space_check(board, position) == True:
        return position


def replay():
    response = 'Placeholder'

    while (response == 'Y' or response == 'N') == False:
        response = input('Do you want to play again (Y/N)?: ')

    if response == 'Y':
        return True
    elif response == 'N':
        return False


def game():
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    while True:

        board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

        player_input()

        display_board(board)
        if choose_first() == 'Player X goes first!':
            marker = 'X'
            print('Player X goes first!')
        else:
            marker = 'O'
            print('Player O goes first!')

        while win_check(board, marker) == False and full_board_check(board) == False:

            while marker == 'X':
                position = player_choice(board)
                place_marker(board, marker, position)
                display_board(board)

                if win_check(board, marker) == False:
                    marker = 'O'
                    break
                elif win_check(board, marker) == True:
                    print(f' {marker} has won the game!')
                    break
                elif full_board_check(board) == True:
                    print('Draw game')
                    break

            if win_check(board, marker) == True:
                break

                # Player O's Turn
            while marker == 'O' and full_board_check(board) == False:
                position = player_choice(board)
                place_marker(board, marker, position)
                display_board(board)

                if win_check(board, marker) == False:
                    marker = 'X'
                    break
                elif win_check(board, marker) == True:
                    print(f' {marker} has won the game!')
                    break
                elif full_board_check(board) == True:
                    print('Draw game')
                    break

            if win_check(board, marker) == True:
                break

        if not replay():
            break

game()