import time
import logging
import random

# my modules
import constants
import snippets # helper functions
from base_logger import logger

from game import Game 
from player import Player

# create child logger for this module, parent is in base_logger.py
logger = logging.getLogger(__name__)

class Application(object):
    """ """

    def __init__(self):
        # logger.debug("")
       pass
    
    # --- public methods ---
    def start(self):
        """ """
        logger.debug("")

        snippets.clear_terminal()
        # 2nd ask who will be playing the game
        # create players outside the game
        player_X_name = input(f'Enter player 1 "X" name: ')
        player_O_name = input(f'Enter player 2 "O" name: ')

        player_X = Player(player_X_name, 'X')
        player_O = Player(player_O_name, 'O')

        # start the game and send application instance to it
        self.game = Game(player_X, player_O)
        
    def run(self):
        """ """
        logger.debug("")
        
        while True:           
            try:
                # game config and initializations 
                self.game.start()
                
                # continus loop until game over
                self.game.play()
                
                # display win, ask for play again
                self.game.end()
                
                # if game terminated, exit app
                if self.game.is_shutdown:
                    break

            except KeyboardInterrupt:
                logger.debug('\nApplication exit by user')
                break        

            except Exception as e:
                # logger.critical(f'Game exit by error: {e} ')
                logger.critical(f'Application exit by error: {e.args} ')
                break

    def end(self):
        """ """
        logger.debug("")
        
        # this way helps to format a nice terminal message
        msg = (2*'\n' + '***   Thank you for playing   ***' + '\n'
                      + '***    for more info visit    ***' + '\n'
                      + '***  github.com/CrtomirJuren  ***')

        snippets.clear_terminal()
        logger.info(msg)

    def splash_screen(self):

        # this way helps to format a nice terminal message
        msg = (2*'\n' + '***   Welcome to Tic Tac Toe Game   ***' + '\n'
                      + '***    For exit press "Ctrl + c"    ***' + '\n')

        snippets.clear_terminal()
        logger.info(msg)


if __name__ == '__main__':
    # no delays used here - for development
    
    # create instance
    app = Application()
    # start
    app.start()
    # run
    app.run()
    # end
    app.end()