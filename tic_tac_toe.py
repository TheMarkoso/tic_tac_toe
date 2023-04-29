import random

# TIC TAC TOE 
board = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-'
        ]

current_player = 'X'
game_running = True

# print the board
def print_board(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# input player option 
def player_input_board(board):
    inp = int(input('choose position beetwen 1|9: '))
    if board[inp-1] == '-':
        board[inp-1] = current_player
    else:
        print('oops, player is already in that spot!')

# check if win or tie 
def check_win(board, current_player):
    global game_running
    wins = [
            [0,3,6], [1,4,7], [2,5,8],
            [0,1,2], [3,4,5], [6,7,8],
            [0,4,8], [2,4,6]
            ]

    for win in wins:
        if board[win[0]] == current_player and board[win[1]] == current_player and board[win[2]] == current_player:
            
            print_board(board)
            print(f'El ganador es {current_player}')
            return True 



def chek_tie(board):
    global game_running
    if '-' not in board:
        print_board(board)
        #game_running = False
        print('esto es un empate!!')
        return True


# print the board with playerBOT input option
def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def computadora(board):
    while current_player == 'O':
        option = random.randint(0, 8)
        if board[option] == '-':
            board[option] = 'O'
            switch_player()


# check if win or tie again 



while game_running:
    print_board(board)
    player_input_board(board)
    #check_win(board)
    if check_win(board,current_player):
        break
    if chek_tie(board):
        break
    switch_player()
    computadora(board)
    if check_win(board,current_player):
        break
    if chek_tie(board):
        break
    #check_win(board)
    #chek_tie(board)

