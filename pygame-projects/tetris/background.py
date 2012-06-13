mport pygame

from pygame.locals import *
from constants import *

class Settings(object):
   """
   Game Settings class
   """

   def __init__(self):
       """        
       Initialize with default settings
       """

       #Size of the main window
       self.resolution = (600, 400)
       # Background color
       self.background(0, 153, 153)
       # Mouse enabled
       self.mouse_enabled = True
       # Title
       self.title = "Tetris"
       self.game_area = Rect(5, 5, 300, 400)
       self.game_info = Rect(150, 5, 300, 400)
       self.box_display = Rect(180, 70, 200, 100)
       
       self.colors = [(255, 255, 255),		# WHITE
		      (100, 100, 100), 		# GRAY
		      (255,   0,   0), 		# RED
		      (  0, 255,   0), 		# BLUE
		      (  0,   0, 255), 		# GREEN
		      (  0,   0,   0)]		# BLACK

       self.my_font40 = pygame.font.SysFont(None, 40)
       self.my_font30 = pygame.font.SysFont(None, 30)
       self.my_font20 = pygame.font.SysFont(None, 20)
