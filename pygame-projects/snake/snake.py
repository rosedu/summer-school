import pygame
import gameobject

from pygame.locals import *

class SnakePart(gameobject.GameObject):
    
    def __init__(self, x, y, surface):
        super(SnakePart, self).__init__(x, y, surface)
        self.lastDirection = 1

        self.SIZE = gameobject.GameObject.SIZE
        self.image = pygame.Surface((2*self.SIZE, 2*self.SIZE), flags = SRCALPHA)
        self.image.convert()

       
        self.rect = pygame.draw.circle(self.image,
                pygame.Color("green"),
                (self.SIZE,self.SIZE), self.SIZE)
        self.rect.midtop  = (x, y)
    
    def update(self):
        self.rect.midtop = (self.x, self.y)

    def moveTo(self,dire):
            y = self.y
            x = self.x
            if dire ==1 and self.lastDirection==2:
                return False
            if dire ==2 and self.lastDirection==1:
                return False
            if dire ==3 and self.lastDirection==4:
                return False
            if dire ==4 and self.lastDirection==3:
                return False
            if dire == 1:
                y = y-2*self.SIZE
            if dire == 2:
                y = y+2*self.SIZE
            if dire == 3:
                x = x-2*self.SIZE
            if dire == 4:
                x = x+2*self.SIZE
            self.y = y
            self.x = x
            self.lastDirection = dire
            return True


