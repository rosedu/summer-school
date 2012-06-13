import pygame

from pygame.locals import *
from constants import *

class Settings(object):
    """
    The board representing the tetris playing area
    """
    
    def __init__(self):
            """
            Init and config the tetris board
            """
            
            #Size of the main window
            self.resolution = (600, 400)
            # Background color
            self.background(0, 153, 153)
            # Mouse enabled
            self.mouse_enabled = True
            # Title
            self.title = "Tetris"

            self.landed = {}

class Board(object):
    def check_for_complete_row(self, brick):
            """
            Look for a complete row of blocks
            """

            rows_deleted = 0
            
            # Add the blocks to those that have already landed
            for brick in bricks:
                    self.landed[brick.coord()] = brick.current_id

            empty_row = 0

            #find the first empty row
            for y in xrange(self.x, 
