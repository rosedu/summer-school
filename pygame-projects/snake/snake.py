import pygame
import gameobject

from pygame.locals import *

class Snake(GameObject):
    
    def __init__self(self, x, y, surface):
        super(self, x, y, surface).__init__self()

        self.image = pygame.Surface((20, 20), flags = SRCALPHA)
        self.image.convert()

        self.set_color("green")

        self.rect.midtop = (x, y)

    def update():
        pass
         
