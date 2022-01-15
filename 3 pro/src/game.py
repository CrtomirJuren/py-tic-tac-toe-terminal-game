"""
    OOP tic-tac-toe game arhitecture
    - board object has 9 cell objects
    - cell object saves a player object
    - player object has id, name, icon 
"""
import os
import logging
import time

import constants
import snippets

from board import Board
from player import Player
from random import choice

# create child logger for this module, parent is in base_logger.py
logger = logging.getLogger(__name__)

class Game(object):
    # constructor
    def __init__(self, player_1, player_2):
        # logger.debug("")

        self._current_player = None
        # end current game
        self._game_over = False
        # completely finish playing
        self._is_shutdown = False

        self._player_1 = player_1
        self._player_2 = player_2
        self._players = [self._player_1, self._player_2]

    # --- public methods ---
    def start(self):
        """ create game """
        logger.debug("")
        
        snippets.clear_terminal()
        
        # create game board       
        self.board = Board()

    def play(self):
        """ 
        - main game logic
        - loop until game over
        """
        logger.debug("")
        
        self._select_random_player()
   
        while True:
            # display board
            self._display_board()

            # player's turn
            self._handle_turn()

            snippets.clear_terminal()
            self._display_board()


            # check if win or tie
            self._check_game_over_condition()

            if self._game_over:
                # stop play loop
                break
            else:
                # else player for next turn
                self._next_player()

    def end(self):
        """
        - dialogue for start new game or exit,
        - save results
        - show top scores 
        """
        # ask to start again or end game
        while True:
            # user input raises error if wrong key pressed
            new_game = input(f'Please select: Play Again = 1, Exit = 0 : ')
            
            # check if user input is not a number
            try:
                new_game = int(new_game)
                
                # check if user input is 0 or 1
                if new_game == 0:
                    self._is_shutdown = True
                    break
                elif new_game == 1:
                    self._is_shutdown = False
                    break
                else:
                    logger.info('Please enter a number 0 or 1')

            except Exception as e:
                logger.info('Please enter a number 0 or 1')

    @property # getter - accessor
    def is_shutdown(self):
        """ The value property."""
        return self._is_shutdown

    # --- private methods ---
    def _display_board(self):
        logger.info('\n'+ str(self.board))

    def _handle_turn(self):
        """ ask user for input and insert input into cell """
        # ask user until input is correct
        while True:

            # user input raises error if wrong key pressed
            try:
                cell_index = int(input(f'{self._current_player} \nSelect position 1-9: '))
                # print(TypeError("cell index must be an integer"))
                self.board.set_cell(cell_index, self._current_player)
                # correct input, break out of while loop
                break
            except Exception as e:
                snippets.clear_terminal()
                self._display_board()

                logger.warning(e)

    def _select_random_player(self):
        # select player to start
        self._current_player = choice(self._players)    
        logger.info(f'{self._current_player} has 1st turn') 

    def _next_player(self):
        """ switch players """
        # change to next player
        if self._current_player == self._player_1:
            self._current_player = self._player_2
        else:
            self._current_player = self._player_1

    def _check_win(self):
        row_full = self.board.is_any_row_full(self._current_player)
        column_full = self.board.is_any_column_full(self._current_player)
        diagonal_full = self.board.is_any_diagonal_full(self._current_player)

        win = any([row_full, column_full, diagonal_full])
        win_type = ['row','column','diagonal']

        return win

    def _check_game_over_condition(self):
        """ win if row, column or diagonal win"""
        win = self._check_win()
        tie = self.board.is_full() and not win

        if win:
            msg = ('\n' +  '*** CONGRATULATIONS ***' + '\n'
                     + f' {self._current_player} WINS '+ '\n')

            logger.info(msg)

        if tie:
            logger.info(f'Game is a tie.')

        self._game_over = any([win, tie])

# --- functions for testing module ---
def real_play():
    player_X = Player('Mr. Cross','X')
    player_O = Player('Mr. Nought','O')

    game = Game(player_X, player_O)
    game.start()
    game.play()
    game.end()

def simulated_play():
    pass

if __name__ == '__main__':
    real_play()
    # simulated_play()

