from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-|" + "-|" + "-")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-|" + "-|" + "-")
    print(board[7] + '|' + board[8] + '|' + board[9])




def player_input():
    marker = " "

    while marker not in ['X', 'O']:
        marker = input("Player 1 choose a marker (X or O): ").upper()

        if marker not in ['X', 'O']:
            print("Not a valid marker, please choose (X or O): ")

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return "player 1 will go first"
    else:
        return "player 2 will go first"

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Player choose your next position: (1-9) '))

    return position


def replay():
    choice = input("Do you want to play again (Y or N)").upper()
    if choice not in ['Y', 'N']:
        print("Not a valid choice, please choose (Y or N): ")
    return choice == 'Y'

print('Welcome to Tic Tac Toe!')
while True:

    main_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn)

    play_game = input("want to play? (Y or N)").upper()

    if play_game == "Y":
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == "Player 1":
            display_board(main_board)
            position = player_choice(main_board)
            place_marker(main_board, player1_marker, position)

            if win_check(main_board, player1_marker):
                display_board(main_board)
                print('PLAYER 1 HAS WON THE GAME!')
                game_on = False
            else:
                if full_board_check(main_board):
                    display_board(main_board)
                    print("THE GAME IS A TIE!")
                    break
                else:
                    turn = "Player 2"

        else:
            display_board(main_board)
            position = player_choice(main_board)
            place_marker(main_board, player2_marker, position)

            if win_check(main_board, player2_marker):
                display_board(main_board)
                print('PLAYER 2 HAS WON THE GAME!')
                game_on = False
            else:
                if full_board_check(main_board):
                    display_board(main_board)
                    print("THE GAME IS A TIE!")
                    break
                else:
                    turn = "Player 1"
    if not replay():
        break


