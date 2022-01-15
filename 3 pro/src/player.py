import logging
import time

import constants

# create child logger for this module, parent is in base_logger.py
logger = logging.getLogger(__name__)

class Player(object):
    # object instance counter
    obj_id = 0

    def __init__(self, name, icon):
        logger.debug("")
        # for each new instance increse uid
        Player.obj_id += 1
        self.id = Player.obj_id

        self.name = name
        self.icon = icon

        self._wins = 0

    def __str__(self):
        """ class string representation """
        return f'Player {self.id} "{self.icon}" {self.name}'

if __name__ == '__main__':
    # create instance
    player_X = Player('Mr. Cross','X')
    player_O = Player('Mr. Nought','O')

    print(f'{player_X} won')
    print(f'{player_O} lost')