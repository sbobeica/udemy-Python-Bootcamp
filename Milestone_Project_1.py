'''Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9
    corresponds with a number on a number pad, so you get a 3 by 3 board representation.'''
def print_board(board):
    print('\n'*10)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

'''Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. 
    Think about using while loops to continually ask until you get a correct answer.'''
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1, please choose from "X" or "O": ').upper()
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)

'''Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), 
    and a desired position (number 1-9) and assigns it to the board.'''
def place_marker(board, marker, position):
    board[position] = marker

'''Step 4: Write a function that takes in a board and checks to see if someone has won'''
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark))

'''Step 5: Write a function that uses the random module to randomly decide which player goes first. 
    You may want to lookup random.randint() Return a string of which player went first.'''
import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

'''Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.'''
def space_check(board, position):
    return board[position] == ' '

'''Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.'''
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    # BOARD IS FULL IF WE RETURN TRUE
    return True
# def full_board_check(board):  # Much more PYTHONIC approach of the same problem
#     if ' ' in board[1:]:
#         return False
#     else:
#         return True
# def full_board_check(board):  # Even more PYTHONIC approach of the same problem
#     return ' ' not in board[1:]

'''Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function 
    from step 6 to check if its a free position. If it is, then return the position for later use.'''
def player_choice(board):
    position = 100
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position

'''Step 9: Write a function that asks the player if they want to play again and returns 
    a boolean True if they do want to play again.'''
def replay():
    choice = input('Play again? Enter Yes or No')
    return choice == 'y'

'''Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!'''
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
