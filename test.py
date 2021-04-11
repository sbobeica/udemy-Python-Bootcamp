def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ').upper()

    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[7] == board[5] == board[3] == mark))

import random
def choose_first():
    firs = random.randint(0,1)
    if firs == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 100
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose a position from 1-9: '))
        return position

def replay():
    play = input('Play again! Enter Yes or No')
    return play == 'y'


'''Implementation of all from the above'''
print('Welcome to TIC TAC Toe!')

while True:
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will play first!')

    play_game = input('Are you ready to play? Enter Yes or No: ')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            #Player1's turn.

            print_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                print_board(the_board)
                print('Congratulation, player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    print_board(the_board)
                    print('Tie game!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            print_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                print_board(the_board)
                print('Congratulation, player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    print_board(the_board)
                    print('Tie game!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
