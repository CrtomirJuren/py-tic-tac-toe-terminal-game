"""
- cell class used in board class.
- cell class is protected to only hold Player class 
"""

from base_logger import logger
import logging

from player import Player

# right now not used
# import snippets
# import constants

# create child logger for this module, parent is in base_logger.py
logger = logging.getLogger(__name__)

# v celico se zapiše numerična vrednost, lahko bi se tudi player object
class Cell(object):
    """
    A class to represent a single cell.

    ...

    Attributes
    ----------
    id : int
        increments for every new class instance
    value : Player
        holds Player class value
    Methods
    -------
    __init__(self, value = None)
        Initializes self
    __repr__(self)
        Returns Player's icon as string
    is_empty(self)
        Returns True if no value is set to cell
    """

    # object instance counter
    obj_id = 0

    def __init__(self, value = None):
            """ constructor """
            # for each new instance increse uid
            Cell.obj_id += 1
            self._id = Cell.obj_id
            self._value = value

    def __repr__(self):
        """ cell value is represented by the Player's icon """
        if self._value != None:
            player = self._value
            return player.icon
        else:
            return ' '

    # --- getters - accessors ---
    @property
    def value(self):
        """ Get or Set value. Set is protected to accept only Player class """
        return self._value

    @property
    def id(self):
        """ returns id """
        return self._id

    @property
    def is_empty(self):
        """ Returns True if no value is set to cell """
        return self._value == None

    # ---setters - mutators ---
    # PROTECTIVE VERSION FOR PLAYER CLASS ONLY
    # @value.setter
    # def value(self, new_value):
    #     # """ no docstrings for setters. """"

    #     # check if value is Player class
    #     if isinstance(new_value, Player):
    #         self._value = new_value
    #     else:
    #         raise TypeError("Value must be a Player class.")

    @value.setter
    def value(self, new_value):
        # """ no docstrings for setters. """"
        self._value = new_value


def how_to_use_example():
    # create cell and player instance
    cell = Cell()
    print(f'id {cell.id}')

    player_X = Player('Mr. Cross','X')

    # cell that is empty
    print(f'value {cell.value}')
    print(f'is_empty {cell.is_empty}')
    print(f'-----\n| {cell} | \n-----')

    # cell that is set with player
    cell.value = player_X
    print(f'value {cell.value}')
    print(f'is_empty {cell.is_empty}')
    print(f'-----\n| {cell} | \n-----')

def test_docstring():
    print('-------------')
    print(Cell.__doc__)

    print('-------------')
    print(Cell.value.__doc__)

if __name__ == '__main__':
    how_to_use_example()
    # test_docstring()