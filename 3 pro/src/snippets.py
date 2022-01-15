"""
Here go all the general functions that are used everywhere, that do
not belong to a single class.  
"""

import os
import constants

def clear_terminal():
    """ clear terminal. if in debug mode = developing , dont clear """
    if not constants.DEBUG:
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    print('abrakadabra')
    clear_terminal()
    print('dabrakadabra')