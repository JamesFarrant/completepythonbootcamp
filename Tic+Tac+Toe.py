from IPython.display import clear_output

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ']

def print_board():
        printed_board =  '''\t|{0}| <--->|{1}|<--->|{2}|
        -----------------------------
        |{3}|<--->|{4}|<--->|{5}|
        -----------------------------
        |{6}|<--->|{7}|<--->|{8}|\n'''
        print printed_board.format(*board)

def place_letter():
    print 'Choose your move --> '
    board.insert(input('index --> '), raw_input('letter --> ').upper())
    
def check_win():
    player_1 = 'X'
    player_2 = 'O'
    win = False
    
    # Horizontal wins
    if board[0] == board[1] == board[2] == player_1 or board[0] == board[1] == board[2] == player_2:
        win = True
    elif board[3] == board[4] == board[5] == player_1 or board[3] == board[4] == board[5] == player_2:
        win = True
    elif board[6] == board[7] == board[8] == player_1 or board[6] == board[7] == board[8] == player_2:
        win = True
    # Vertical wins
    elif board[0] == board[3] == board[6] == player_1 or board[0] == board[3] == board[6] == player_2:
        win = True
    elif board[1] == board[4] == board[7] == player_1 or board[1] == board[4] == board[7] == player_2:
        win = True
    elif board[2] == board[5] == board[8] == player_1 or board[2] == board[5] == board[8] == player_2:
        win = True
    # Diagonal wins
    elif board[0] == board[4] == board[8] == player_1 or board[0] == board[4] == board[8] == player_2:
        win = True
    elif board[6] == board[4] == board[2] == player_1 or board[6] == board[4] == board[2] == player_2:
        win = True
    if win == True:
        end_game()
        
def end_game():
    clear_output()
    print 'Congratulations, you won!'

def game_loop():
    while ' ' in  board:
        check_win()
        print_board()
        place_letter()

game_loop()
