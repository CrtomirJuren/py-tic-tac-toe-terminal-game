"""
"""
import time
import logging
import random

# --- global constants ---
DEBUG = False

# --- global variables ---
# main application_flag
app_running = True
# game running
game_over = False
# who will win ?
winner = None
# who's turn is it
current_player = "X" # "O"
# game board   
board = []

# create logger
if DEBUG:
    # for showing all the messages during app development
    logging.basicConfig(level=logging.DEBUG, format ='%(levelname)s | %(message)s')
else:
    # for finished app
    logging.basicConfig(level=logging.INFO, format ='%(message)s')

logger = logging.getLogger(__name__)

# --- top level game logic ---
# three main game structures
def game_start():
    """ """
    global board
    global winner
    global current_player
    global game_over

    logging.debug('game_start()')

    # initialize board
    board = 9*["-"]
    # game running
    game_over = False
    # clear winner
    winner = None
    # select player to start
    current_player = random.choice(["O","X"])

def game_play():
    """ """
    global game_over

    logging.debug('game_play()')    
    
    # display board
    display_board()

    while not game_over:
        # change to next player
        select_player()
        # player's turn
        handle_turn()
        # show updated board
        display_board()
        # check if win or tie
        check_game_over_condition()

def game_end():
    """ """
    logging.debug('game_end()')
    global app_running

    # ask to start again or end game
    while True:
        # user input raises error if wrong key pressed
        app_running = input(f'Please select: Play Again = 1, Exit = 0 : ')
        
        # check for correct user input
        try:
            # str to int
            app_running = int(app_running)
            # check if user input is 0 or 1
            if app_running == 1:
                break
            
            if app_running == 0:
                break

        except Exception as e:
            logger.info('Please enter a number 0 or 1')


# --- functions ---
def select_player():
    global current_player

    logging.debug('select_player()')
    # change to next player

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    logging.info(f"Player '{current_player}' turn ")

def handle_turn():
    global current_player
    # accepted = False

    while True:
        # igralec izbere pozicijo
        position = input("Select position 1-9: ")
        # user input raises error if wrong key pressed
        try:
            # str -> int
            position = int(position)
            # pretvori na pravi index 1-9 --> 0-8
            position -= 1
            logging.debug('position: ', position)
            # preveri ali je vnešena pozicija ok
            if (0 <= position <= 8):
                if (board[position] == '-'):
                    board[position] = current_player
                    # exit while loop
                    break
                else:
                    logging.info('Position already full. Try again.')
            else:   
                logging.info('Position not in range. Try again.')
        # ignore user key error
        except:
            logging.info('User input error. Try again.')
    
def display_board():
    global board
    logging.debug('display_board()')

    print(board[0] +" | "+ board[1] + " | " + board[2]+ 5*" " + " 1 | 2 | 3 ")
    print(board[3] +" | "+ board[4] + " | " + board[5]+ 5*" " + " 4 | 5 | 6 ")
    print(board[6] +" | "+ board[7] + " | " + board[8]+ 5*" " + " 7 | 8 | 9 ")
    print("")

def check_game_over_condition():
    global game_over
    global winner

    logging.debug('check_if_game_over_condition()')

    win = check_win_condition()
    
    if win:
        winner = current_player
        logging.info(f'Player {winner} won game.')

    # if the game is won at the last cell,
    # dont check tie condition. or game will be win and tie    
    tie = check_tie_condition()
    # if no win and a tie, there is tie
    tie = tie and not win

    if tie:
        logging.info(f'Game is tied.')  

    if tie or win:
        game_over = True

def check_win_condition():
    global current_player
    global board

    # check rows
    row_win = check_rows(board,current_player)
    # check columns
    column_win = check_columns(board, current_player)  
    # check diagonals
    diagonal_win = check_diagonals(board, current_player)
    # win if any of conditions true
    win = (row_win or column_win or diagonal_win)

    # return result
    return win

def check_tie_condition():
    """ """
    global board

    logging.debug('check_tie_condition()')

    # is the board full and no wins
    empty_cells = board.count('-')
    logging.debug(f'Number of empty cells {empty_cells}')   

    tie = (empty_cells == 0)

    return tie

def check_rows(board, player):
    """ """
    logging.debug('check_rows()')
    win = False

    row_1 = board[0:3] # 1,2,3
    row_2 = board[3:6] # 4,5,6
    row_3 = board[6:9] # 7,8,9

    r_1_win = (row_1.count(player) == 3)
    r_2_win = (row_2.count(player) == 3)
    r_3_win = (row_3.count(player) == 3)

    win = (r_1_win or r_2_win or r_3_win)

    return win

def check_columns(board,player):
    """ """
    logging.debug('check_columns()')

    # stolpec je vsak element za tri indexe večji
    column_1 = board[0:9:3]
    column_2 = board[1:9:3]
    column_3 = board[2:9:3]
    
    # win if 3 in a column
    c_1_win = (column_1.count(player) == 3)
    c_2_win = (column_2.count(player) == 3)
    c_3_win = (column_3.count(player) == 3)

    win = (c_1_win or c_2_win or c_3_win)

    return win

def check_diagonals(board,player):
    """ """
    logging.debug('check_diagonals()')

    # --- DIAGONALE ---
    diagonal_1 = [board[0],board[4],board[8]] # 0 | 4 | 8
    diagonal_2 = [board[2],board[4],board[6]] # 0 | 4 | 8

    d_1_win = (diagonal_1.count(player) == 3)
    d_2_win = (diagonal_2.count(player) == 3)

    win = (d_1_win or d_2_win)

    return win

# --- main game arhitecture loop ---
def main():
    global app_running
    
    logger.info('*** Welcome to Tic Tac Toe Game ***')
    logger.info('***  For exit press "Ctrl + c"  ***\n')
    
    while app_running:           
        try:
            # setup game 
            game_start()
            # continus loop until game over
            game_play()
            # display win, ask for play again
            game_end()

        except KeyboardInterrupt:
            logger.info('\nGame exit by user')
            break        

        except Exception as e:
            logger.critical(f'Game exit by error: {e} ')
            break
        
    logger.info('Thank you for playing :)')

# --- application ---
main()

