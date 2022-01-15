"""
- BOARD: SIMPLE LIST, NOT A 2D ARRAY BACKED GRID, WE DONT NEED THIS
- http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
- board uses numpy 2D array
"""

import logging
from os import times_result
import time
import numpy as np
import string 
import random
from itertools import chain # 2D->1D list

from base_logger import logger
import constants
import snippets


from cell import Cell
from player import Player

# create child logger for this module, parent is in base_logger.py
logger = logging.getLogger(__name__)

""" board coordinates same as numpad for simple playing   
7 8 9    
4 5 6
1 2 3
"""

class Board(object):
    """
    A class to represent game board.

    ...

    Attributes
    ----------
    _board : Board
    _board_index : 3x3 2D array of keypad strings

    # value : Player
    #     holds Player class value
    # Methods
    -------
    __init__(self, value = None)
        Initializes self
    __repr__(self)
        Returns board as string to print in terminal
    # is_empty(self)
    #     Returns True if no value is set to cell
    

    is_full(self)
    """

    def __init__(self):
        """ constructor """
        # logger.debug("")

        # crete 9 cells for board
        self._board = [Cell() for index in range(9)]
        
        # 1D list to 2D list
        self._board = [self._board[:3],
                       self._board[3:6],
                       self._board[6:]]               

        self._board_index = [['7','8','9'],
                            ['4','5','6'],
                            ['1','2','3']]   

    # public
    def __repr__(self):
        """ to simply use with print() """
        return self._display()

    # private
    def _display(self):
        """ board 
            -------------
            | X | 8 | O |
            -------------
            | 4 | X | 6 |
            -------------
            | 1 | 2 | O |
            -------------
        """
        # output_board = ''
        output_board = ' TIC TAC TOE \n'
        for irow, row in enumerate(self._board):
            
            # add top side

            output_row = '-------------'+'\n' 
            
            for icol, cell in enumerate(row):
                # player = cell.value 

                # if cell is empty show board index
                if cell.is_empty:
                    icon = self._board_index[irow][icol]
                # if cell is full, show cell-player icon
                else:
                    # str(cell) = player.icon
                    icon = str(cell) 

                # add left side + value 
                output_row += '|'+ ' ' + icon + ' '

            # add right side
            output_row += '|'
            
            # add row to board
            output_board += output_row +'\n'

        # add bottom
        # output_board += '-------------'+'\n'
        output_board += '-------------'

        return output_board

    # private
    def _keypad_to_2d_list_index(self, keypad_index):
        """ keypad 1-9, 2D list [0-2][0-2]"""
        # convert to 0-8
        keypad_index -= 1
        # convert row[0-2] col[0-2]
        irow = 2 -  keypad_index // 3
        icol =  keypad_index % 3

        return (irow, icol)

    # public
    def set_cell(self, keypad_index, player):
        """ user inputs numbers on keypad 1-9 """

        # check if cell index is integer
        if not type(keypad_index) == int:
            raise TypeError("Index must be an integer.")
        
        # check if keypad index in range of board
        low, high = 1, 9
        if low <= keypad_index <= high:

            # transform keypad index to 2D irow, icol index
            irow, icol = self._keypad_to_2d_list_index(keypad_index)
            # logger.debug(f'cell_index:{keypad_index},row:{irow}, column:{icol}') 

            # self.board[irow][icol] = CELL OBJECT
            cell = self._board[irow][icol]

            # check if cell is empty
            if(cell.value == None):
                cell.value = player
            else:
                raise ValueError(f'Cell {keypad_index} already full.')

        else:
            raise ValueError('Index must be ' +
                             f'between or equeal {low} and {high}')

    # -- private methods ---
    def is_any_row_full(self, player): 
        """ check rows if filled by player """

        completed = False

        # iterate over rows
        for index, row in enumerate(self._board):
            # extract Players from Cells
            row = [cell.value for cell in row]
            # returns [Player, Player, Player]

            # win happens if same player values in all row cells
            completed = (row.count(player) == len(row))
            
            if completed:
                logger.debug(f'{player} completed row {index}')
                break

        return completed

    def is_any_column_full(self, player): 
        """check columns if filled by player """

        # iterate over rows
        status = []
        # zip(*matrix) generates a transposed version of your matrix
        for column in zip(*self._board): 
            # extract Players from Cells
            column = [cell.value for cell in column]

            # win happens if same player in all row
            full = (column.count(player) == len(column))
            status.append(full)

        logger.debug(f'{player} | Columns {status} | Full {any(status)}')

        return any(status)

    def is_any_diagonal_full(self, player):
        """check diagonals if filled by player """

        # first get valeus from board that are diagonals
        diagonals = []
        l = len(self._board[0])
        # get top left diagonal
        diagonal = [self._board[i][i] for i in range(l)] # [7,5,3]
        diagonals.append(diagonal)

        # get top right diagonal
        diagonal = [self._board[l-1-i][i] for i in range(l-1,-1,-1)]  # [1,5,9]
        diagonals.append(diagonal)
        
        # iterate over both diagonals if any win
        status = []
        for diagonal in diagonals: 
            # extract Players from Cells
            diagonal = [cell.value for cell in diagonal]

            # win happens if same player in all row
            full = (diagonal.count(player) == len(diagonal))
            status.append(full)
        
        logger.debug(f'{player} | Diagonals {status} | Full {any(status)}')

        return any(status)

    def is_full(self):
        """ check if all places taken """
        # flatten 2D list to 1D
        flattened_board = chain.from_iterable(self._board)

        full = []
        for cell in flattened_board:
            # check if cell is full, not None
            full.append(cell.value != None) 

        return all(full) 

# testing functions

def simulated_board_win_checks():
    """ randomly generates full boards and checks for wins """

    # create board
    board = Board()

    # create players
    players = [Player('Črtomir', 'X'),
               Player('Miko', '0')]

    # randomize player turns
    [board.set_cell(position+1, random.choice(players)) for position in range(9)]

    snippets.clear_terminal()
    print(board)

    for player in players:
        # show full board
        print(player)

        status = board.is_any_row_full(player)
        print(f'is_any_row_full = {status}')

        status = board.is_any_column_full(player)
        print(f'is_any_column_full = {status}')

        status = board.is_any_diagonal_full(player)
        print(f'is_any_diagonal_full = {status}')

if __name__ == '__main__':
    simulated_board_win_checks()