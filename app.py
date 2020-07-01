def display_board(board):
    print('\n'*100)
    print('   |   |    ')
    print(' {} | {} | {}  '.format(board[7], board[8], board[9]))
    print('   |   |    ')
    print('-----------')
    print('   |   |    ')
    print(' {} | {} | {}  '.format(board[4], board[5], board[6]))
    print('   |   |    ')
    print('-----------')
    print('   |   |    ')
    print(' {} | {} | {}  '.format(board[1], board[2], board[3]))
    print('   |   |    ')


def player_input():
    marker = input("Do you want to be 'X' or 'O': ").upper()
    if marker == 'X':
        player_marker1 = 'X'
        return ['X', 'O']
    elif (marker.lower() == 'exit'):
        return 'exit'
    else:
        player_marker1 = 'O'
        return ['0', 'X']

def place_marker(board, marker, position):
    #board = ['#','X','O','X','O','X','O','X','O','X']
    
    board[position] = marker

def win_check(board, mark):
    
    for _ in range(1,len(board)+1):
        if board[1] == board[2] == board[3] == mark:
            return True
        elif board[1] == board[4] == board[7] == mark:
            return True
        elif board[1] == board[5] == board[9] == mark:
            return True
        elif board[2] == board[5] == board[8] == mark:
            return True
        elif board[3] == board[5] == board[7] == mark:
            return True
        elif board[3] == board[6] == board[9] == mark:
            return True
        elif board[4] == board[5] == board[6] == mark:
            return True
        elif board[7] == board[8] == board[9] == mark:
            return True 
    else:
        return False

import random

def choose_first():
    return random.randint(1,3)

def space_check(board, position):
    if position < len(board):
        if board[position] == ' ':
            return True
        else:
            return False
    return ''

def full_board_check(board):
    
    for i in board:
        if i == ' ':
            return False
        else:
            continue
    
    return True

def player_choice(board):
    player_pos1 = 0
    player_pos2 = 0
    while True:
        player_pos1 = input('Choose your next position: ')
        if player_pos1.isnumeric():
            player_pos1 = int(player_pos1)
            if space_check(board, player_pos1):
                return player_pos1
                break
            elif space_check(board, player_pos1) == False:
                print('\nPosition occupied!')
                continue
            else:
                print('Enter digit from 1-9')
                break
        elif player_pos1.lower() == 'exit':
            return 'exit'

def replay():
    
    play_again = input('Do you want to play again? (Yes/No)')
    return play_again.lower() == 'yes'

print('Welcome to Tic Tac Toe!\nEnter "exit" to leave at anytime')
while True:

    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
      
    marker = player_input()
    player1 = marker[0]
    player2 = marker[1]
    
    if marker == 'exit':
        print('\nGoodbye!')
        break
    
    while True:
        display_board(board)
        print(f'\nPlayer 1 is {player1}')
        print(f'Player 2 is {player2}')
        
        #Player 1 Turn
        print('\nPlayer 1')
        position = player_choice(board)
        
        if type(position) == str:
            if position.lower() == 'exit':
                print('\nGoodbye!')
                break

        board[position] = player1
        place_marker(board, player1, position)
        display_board(board)
        if win_check(board, player1) == True:
            print('\nYou won!')
            break
        if full_board_check(board) == True:
            print('\nGame over!')
            break
        
        # Player2's turn.
        print('\nPlayer 2')
        position = player_choice(board)
        
        if type(position) == str:
            if position.lower() == 'exit':
                print('\nGoodbye!')
                break
        
        board[position] = player2
        place_marker(board, player2, position)
        display_board(board)
        if win_check(board, player2) == True:
            print('\nYou won!')
            break
        if full_board_check(board) == True:
            print('\nGame over!')
            break
            
        
    if not replay():
        break
    else:
        display_board(board)
        continue
