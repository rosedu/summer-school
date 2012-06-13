import pygame
import gameobject

from pygame.locals import *

class SnakePart(gameobject.GameObject):
    
    def __init__(self, x, y, surface):
        super(SnakePart, self).__init__(x, y, surface)

        self.SIZE = gameobject.GameObject.SIZE
        self.image = pygame.Surface((2*self.SIZE, 2*self.SIZE), flags = SRCALPHA)
        self.image.convert()

       
        self.rect = pygame.draw.circle(self.image,
                pygame.Color("green"),
                (self.SIZE,self.SIZE), self.SIZE)
        self.rect.midtop  = (x, y)
    
    def update(self):
        pass

    def moveTo(direction):
            if dir == 1:
                y--
            if dir == 2:
                y++
            if dir == 3:

    def handle_key(self, key):
            
        if key == 273: #key up
            print "UP!"
            pass
        if key == 274: #key down
            print "DOWN!"
            pass
        if key == 276: #key left
            print "LEFT!"
            pass
        if key == 275: #key right
            print "RIGHT!"
            pass
         
