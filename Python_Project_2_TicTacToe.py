delimiter = '=' * 52


def print_board(board):  # this just prints the current board
    board_template = '''
-------------
|{6:^3}|{7:^3}|{8:^3}|
-------------
|{3:^3}|{4:^3}|{5:^3}|
-------------
|{0:^3}|{1:^3}|{2:^3}|
-------------
    '''
    print(board_template.format(*board))


def users_choice(board, turn):  # get input from user - select a position
    print(delimiter)
    choice = input(f'Player {turn} | Please enter your move number (1 - 9): ')
    while True:
        if not choice.isdigit():
            choice = input('Please select a value between 1 and 9: ')
        elif int(choice) not in range(1, 10):
            choice = input('Please select a value between 1 and 9: ')
        elif board[int(choice) - 1] != ' ':
            choice = input('Already taken, please select another one: ')
        else:
            print(delimiter)
            return int(choice) - 1


def update_board(board, turn, choice):
    board[choice] = turn
    return board


def is_board_full(board):  # check if the board is full
    return ' ' not in board


def win(board, turn):  # check if the current player wins or not
    is_win = (board[0] == board[1] == board[2] == turn or
              board[3] == board[4] == board[5] == turn or
              board[6] == board[7] == board[8] == turn or
              board[0] == board[3] == board[6] == turn or
              board[1] == board[4] == board[7] == turn or
              board[2] == board[5] == board[8] == turn or
              board[0] == board[4] == board[8] == turn or
              board[2] == board[4] == board[6] == turn)
    return is_win


def main():
    intro = '''
===========================
Welcome to Tic Tac Toe
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row
Let's start the game
    '''

    print(intro)
    turn = 'O'  # whos turn it is to play, player 1 = 'O', player 2 = 'X'
    repeat = ''

    while repeat.lower() != 'q':
        board = [' '] * 9
        print_board(board)
        win_flag = False
        while True:
            choice = users_choice(board, turn)
            update_board(board, turn, choice)
            print_board(board)
            if win(board, turn):
                win_flag = True
                print(f'CONGRATS, PLAYER {turn} WINS!!!!\n')
                break
            elif is_board_full(board):
                break
            else:
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'

        if not win_flag:
            print("It's a tie.\n")
        print(delimiter)
        repeat = input('Wanna play again? Press enter to continue,'
                       ' ''q'' to quit this game: ')


if __name__ == "__main__":
    main()
