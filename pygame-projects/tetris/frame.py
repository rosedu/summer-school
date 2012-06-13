import pygame

from pygame.locals import *
from constants import *

class Settings(object):
    """
    The board representing the tetris playing area
    """
    
    def __init__(self, scale = 20, max_x = 10, max_y = 20):
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
            self.scale = scale
            self.max_x = max_x
            self.max_y = max_y

    def check_for_complete_row(self, brick):
            """
            Look for a complete row of blocks
            """

            rows_deleted = 0
            
            # Add the blocks to those that have already landed
            for brick in bricks:
                    self.landed[brick.coord()] = brick.current_id

            empty_row = 0

            # Find the first empty row
            for y in xrange(self.max_y - 1, -1, -1):
                    row_is_empty = True
                    for x in xrange(self.max_x):
                            if self.landed.get((x, y), None):
                                    row_is_empty = False
                                    break
                    if row_is_empty:
                            empty_row = y
                            break

            # Scan up until an empty row is found
            y = self.max_y - 1
            while y > empty_row:
                    complete_row = True
                    
                    for x in xrange(self.max_x):
                            if self.landed.get((x, y), None) is None:
                                    complete_row = False
                                    break

                    if complete_row:
                            rows_deleted += 1

                            # Delete the completed row
                            for x in xrange(self.max_x):
                                    brick = self.landed.pop((x, y))
                                    self.delete_brick(brick)
                                    del brick

                            # Move all the rows above it down
                            for ay in xrange(y - 1, empty_row, -1):
                                    for x in xrange(self.max_x):
                                            brick = self.landed.get((x,
                                                    ay), None)
                                            if brick:
                                                    brick =
                                                    self.landed.pop((x,
                                                            ay))
                                                    self.move(self, x,
                                                                    y) = 
                                                    self.landed[(x, y)]
                                                    = brick

                            # move the empty row down
                            empty_row += 1

                    else:
                            y -= 1

