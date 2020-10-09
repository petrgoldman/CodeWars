import numpy as np  # to be able to work with diagonals easily

# size = 6
# difficulty = 3
delimiter = '=' * 105

def create_board(size):
    board = np.array([[' '] * size] * size)
    return board


def print_board(board, size):  # this just prints the current board
    first_row = '  ' + '|{:^3}' * size + '|'
    temp_row = '{:<2}' +'|{:^3}' * size + '|'
    print(first_row.format(*range(1, size + 1)))
    for i in range(size):
        print('--' + '-' * 4 * size + '-')
        print(temp_row.format(i + 1,*board[i,:]))
    print('--' + '-' * 4 * size + '-')


def win(board, turn, difficulty, size):  # checks rows, columns and diagonals
    for row in board:
        if turn * difficulty in ''.join(row):
            return True

    for i in range(size):
        if turn * difficulty in ''.join(board[:, i]):
            return True

    for offset in range(- size + 1, size):
        if turn * difficulty in ''.join(board.diagonal(offset)):
            return True

    for offset in range(- size + 1, size):
        if turn * difficulty in ''.join(np.flipud(board).diagonal(offset)):
            return True

    return False

def is_board_full(board):  # check if the board is full
    for row in board:
        if ' ' in ''.join(row):
            return False
    return True


def users_choice(board, turn):  # get input from user - select a position
    print(delimiter)
    choice = input(f'Player {turn} | '
                   f'Please enter position (11 - {str(size) * 2}) '
                   f'(first digit is row number, second digit is '
                   f'column number): ')
    while True:
        if not choice.isdigit():
            choice = input('Try again please: ')
        elif int(choice) not in range(11, int(str(size) * 2) + 1):
            choice = input('Try again please: ')
        elif board[int(choice[0]) - 1, int(choice[1]) - 1] != ' ':
            choice = input('Already taken, please select another one: ')
        else:
            print(delimiter)
            return int(choice[0]) - 1, int(choice[1]) - 1


def game_params():  # get game parameters from user, field size and difficulty
    # print(delimiter)
    size = input('Select the size of the field (3 - 9): ')
    while True:
        if not size.isdigit():
            size = input('Try again please: ')
        elif int(size) not in range(3, 9):
            size = input('Try again please: ')
        else:
            break
    difficulty = input(f'Select difficulty level (3 - {size}): ')
    # difficulty corresponds with the number of consecutive marks
    # needed for victory
    while True:
        if not difficulty.isdigit():
            difficulty = input('Try again please: ')
        elif int(difficulty) < 3 or int(difficulty) > int(size):
            difficulty = input('Try again please: ')
        else:
            break
    return int(size), int(difficulty)



def update_board(board, turn, choice):
    board[choice[0], choice[1]] = turn
    return board


print(game_params())