import pygame

from pygame.locals import *

class GameObject(pygame.sprite.Sprite):
    SIZE = 20
    def __init__self(self, x, y, surface):
        super(GameObject, self).__init__()
        self.x = x
        self.y = y
        self.surface = surface

    
    def getDistance(self, other):
        return abs(self.x-other.x) + abs(self.y - other.y)

        
