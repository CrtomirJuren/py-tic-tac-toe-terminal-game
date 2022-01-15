"""

"""
import time
import logging
import random

# --- global constants ---
DEBUG = False

# create logger
if DEBUG:
    # for showing all the messages during app development
    logging.basicConfig(level=logging.DEBUG, format ='%(levelname)s | %(message)s')
else:
    # for finished app
    logging.basicConfig(level=logging.INFO, format ='%(message)s')

logger = logging.getLogger(__name__)

# --- top level game structure ---
def game_start():
    """ game welcome screen """
    logging.debug('game_start()')
    
    logger.info('*** Welcome to Tic Tac Toe Game ***')
    logger.info('***  For exit press "Ctrl + c"  ***\n')

def game_play():
    """ 
    - main game logic
    - loop until game over
    """
    logging.debug('game_play()')    

    # initialize board
    board = 9*["-"]

    # select player to start
    player = random.choice(["O","X"])    
    
    # display board
    display_board(board)

    game_over = False
    while not game_over:
        # change to next player
        player = next_player(player)

        # player's turn
        board = handle_turn(board, player)

        # show updated board
        display_board(board)

        # check if win or tie
        game_over, winner = check_game_over_condition(board, player)

def game_end():
    """
    - dialogue for start new game or exit,
    - save results
    - show top scores 
    """
    logging.debug('game_end()')

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

            # accepted = True
            # print('end', end)

        except Exception as e:
            logger.info('Please enter a number 0 or 1')

    return app_running

# --- functions ---
def next_player(player):
    """ """
    logging.debug('select_player()')

    # change to next player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

    logging.info(f"Player '{player}' turn ")

    return player

def handle_turn(board, player):

    while True:
        # player selects board position
        position = input("Select position 1-9: ")
        # user input raises error if wrong key pressed
        try:
            # str -> int, 1-9 --> 0-8
            position = int(position) - 1
  
            logging.debug('position: ', position)
            # preveri ali je vnešena pozicija ok
            if (0 <= position <= 8):
                if (board[position] == '-'):
                    board[position] = player
                    # exit while loop
                    break
                else:
                    logging.info('Position already full. Try again.')
            else:   
                logging.info('Position not in range. Try again.')
        # ignore user key error
        except Exception as e:
            logging.info('User input error. Try again.')

    return board

def display_board(board): 
    """ show board in terminal"""

    logging.debug('display_board()')

    print(board[0] +" | "+ board[1] + " | " + board[2]+ 5*" " + " 1 | 2 | 3 ")
    print(board[3] +" | "+ board[4] + " | " + board[5]+ 5*" " + " 4 | 5 | 6 ")
    print(board[6] +" | "+ board[7] + " | " + board[8]+ 5*" " + " 7 | 8 | 9 ")
    print("")

def check_game_over_condition(board, player): 
    """ game over if win or tie """
    logging.debug('check_if_game_over_condition()')

    win = check_win_condition(board, player)
    tie = check_tie_condition(board)
    # if no win and a tie, there is tie
    tie = tie and not win

    if win:
        winner = player
        logging.info(f'Player {winner} won game.')
    else:
        winner = None

    if tie:
        logging.info(f'Game is tied.')  

    game_over = tie or win
    
    return game_over, winner

def check_win_condition(board, current_player): 
    """ win if row, column or diagonal win"""
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

def check_tie_condition(board): 
    """ tie = if no empty cells and no win """
    logging.debug('check_tie_condition()')

    # is the board full and no wins
    empty_cells = board.count('-')
    logging.debug(f'Number of empty cells {empty_cells}')   

    tie = (empty_cells == 0)

    return tie

def check_rows(board, player): 
    """ 3 rows check """
    logging.debug('check_rows()')

    row_1 = board[0:3] # 1,2,3
    row_2 = board[3:6] # 4,5,6
    row_3 = board[6:9] # 7,8,9

    r_1_win = (row_1.count(player) == 3)
    r_2_win = (row_2.count(player) == 3)
    r_3_win = (row_3.count(player) == 3)

    win = (r_1_win or r_2_win or r_3_win)

    return win

def check_columns(board,player): 
    """ 3 columns check """
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
    """ 2 diagonals check """
    logging.debug('check_diagonals()')

    diagonal_1 = [board[0],board[4],board[8]] # 0 | 4 | 8
    diagonal_2 = [board[2],board[4],board[6]] # 2 | 4 | 6

    d_1_win = (diagonal_1.count(player) == 3)
    d_2_win = (diagonal_2.count(player) == 3)

    win = (d_1_win or d_2_win)

    return win

# --- main game arhitecture loop ---
def main():
    app_running = True   

    while app_running:           
        try:
            # setup game 
            game_start()
            # continus loop until game over
            game_play()
            # display win, ask for play again
            app_running = game_end()

        except KeyboardInterrupt:
            logger.info('\nGame exit by user')
            break        

        except Exception as e:
            # logger.critical(f'Game exit by error: {e} ')
            logger.critical(f'Game exit by error: {e.args} ')
            break
        
    logger.info('Thank you for playing :)')

# --- application ---
main()

