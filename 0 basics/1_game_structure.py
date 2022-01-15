"""
simple game arhitecture for terminal
PLAY THE GAME UNTIL ALL ITEMS ARE REMOVED FROM LIST
"""
import time
import logging

# global constants
DEBUG = True

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
    """ welcome screen """

    logger.info("GAME STARTED")
    logger.info('Play the game until all elements are removed from list')

def game_play():

    # create list
    l = [0,'b']
    
    game_over = False
    while not game_over:

        logger.info(f'List: {l}')
        # get user input and print it out, if not integer error
        max_index = len(l)-1
        index = int(input(f'Player Please Select Item 0-{max_index}:\n'))
        item = l.pop(index)
        logger.info(f'Item | {item} | removed from list')
        logger.debug(f'Remaining list: {l}')

        # check if list empty
        if not l:
            logger.info("list is empty, all items were removed")
            game_over = True

def game_end():
    """
    - dialogue for start new game or exit,
    - save results
    - show top scores 
    """
    logging.debug('game_end()')

    # ask to start again or end game
    while True:
        # user input raises error if wrong key pressed
        end = input(f'Please select: Play Again = 0, Exit = 1 : ')
        
        # check for correct user input
        try:
            # str to int
            end = int(end)
            # check if user input is 0 or 1
            if end == 0 or end == 1:
                break
            else:
                logger.info('Please enter a number 0 or 1')

        except Exception as e:
            logger.info('Please enter a number 0 or 1')

    return end

# --- functions ---
def function():
    return True

# --- main game arhitecture loop ---
def main():
    while True:           
        try:
            # setup game 
            game_start()
            # continus loop until game over
            game_play()
            # display win, ask for play again
            if game_end():
                break

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