import logging
from constants import *

#TODO: formatter class to short/lengt string in columns
# class MyFormatter(logging.Formatter):
# board.__init__   | DEBUG |
# app.start        | DEBUG |
# game.start       | INFO | *** Welcome to Tic Tac Toe Game ***

# create parent logger
logger = logging

# configure logger
if DEBUG:
    # diferent styles of debug messages
    # logging.basicConfig(level=logging.DEBUG, format ='%(levelname)s | %(message)s')
    # logging.basicConfig(level=logging.DEBUG, format ='%(asctime)s | %(levelname)s | %(message)s')
    # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s.%(funcName)s | %(levelname)s | %(message)s')
    logging.basicConfig(level=logging.DEBUG, format='%(name)10s.%(funcName)-8s | %(levelname)-7s | %(message)s')
else:
    # for finished app
    logging.basicConfig(level=logging.INFO, format ='%(message)s')

# for testing purpose. this doesnt if we start main application
def main():
    
    # initalize logger for this module
    logger = logging.getLogger(__name__)

    logger.debug("this is a debug message")
    logger.info("this is an info message")
    logger.warning("this is a warning message")
    logger.error("this is an error message")

if __name__ == '__main__':
    main()