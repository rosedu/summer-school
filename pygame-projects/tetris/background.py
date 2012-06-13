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

class image_holder(object):
   """ 
   Holding images
   """
   def __init__(self, image, rect):
       self.image = image
       self.rect = rect

   def draw(self, surface):
       return surface.blit(self.image, self.rect)

class Frame(pygame.sprite.Sprite):
   """
   Making the frame settings
   """
   def __init__(self, rect):
      pygame.sprite.Sprite.__init__(self)

      # Borders 
      border_size = rect.size
      ends = resources.image.border_ends
      vert = resources.image.vertical_border
      horz = resources.image.horizontal_border
      # Vertical
      vertical_border = pygame.Surface((TILE_SIZE[0], border_size[1] +
	      (TILE_SIZE[1] * 2)))
      Oy = 0
      while Oy < vertical_border.get_height():
         vertical_border.blit(vert, (0, y))
	 Oy += vert.get_height()
      vertical_border.blit(ends, (0, 0))
      vertical_border.blit(ends, (0, ends.get_height()))
      vertical_border.blit(ends, (0, vertical_border.get_height() - ends.get_height()))
      vertical_border.blit(ends, (0, vertical_border.get_height() - (2 *
	      ends.get_height())))
      # Horizontal
      horizontal_border = pygame.Surface((TILE_SIZE[0], border_size[1] +
	      (TILE_SIZE[1] * 2)))
      Ox = 0
      while Ox < horizontal_border.get_height():
          horizontal_border.blit(vert, (Ox, 0))
	  Ox += horz.get_height()
      horizontal_border.blit(ends, (0, 0))
      horizontal_border.blit(ends, (horizontal_border.get_width() -
	      ends.get_width(), 0))

      # Making the image
      Ox = (vertical_border.get_width * 2) + horizontal_border.get_width()
      Oy = (horizontal_border.get_height()
      self.image = pygame.Surface((Ox, Oy))
      self.image.blit(vertical_border, (0, 0))
      self.image.blit(vertical_border, (Ox -
	      vertical_border.get_width(), 0))
      self.image.blit(horizontal_border, (vertical_border.get_width(),
	      0))
      self.image.blit(horizontal_border, (vertical_border.get_width(),
	      vertical_border.get_heigth() -
	      horizontal_border.get_height()))
      self.rect = self.image.get_rect()
      self.rect.center = rect.center
 
class Pieces(pygame.sprite.Sprite):
   """
   Displays falling pieces that go straight down
   """
   def __init__(self, piece_map, area):
      pygame.sprite.Sprite.__init__(self)
      self.end = area[1]

      # Image
      piece_map = piece.fix_piece_map(piece_map)
      rows = list(piece_map.splitln())
      Ox = len(rows[0] * TILE_SIZE[0])
      Oy = len(rows) * TILE_SIZE[1]
      self.image = pygame.Surface((Ox, Oy))
      self.image.fill((0, 0, 0))
      self.image.convert()


