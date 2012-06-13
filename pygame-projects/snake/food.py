import pygame
import gameobject
import random

from pygame.locals import *

class Food(gameobject.GameObject):

        def __init__(self, x, y, surface, time = random.randint(0, 50)):
                super(Food, self).__init__(x,y,surface)
                self.SIZE = gameobject.GameObject.SIZE
                self.image = pygame.Surface((2*self.SIZE, 2*self.SIZE),
                                flags = SRCALPHA)
                self.image.convert()

                self.rect = pygame.draw.circle(self.image,
                                pygame.Color("blue"),
                                (self.SIZE,self.SIZE), self.SIZE/2+2)


                self.rect.midtop = (x,y)

        def update(self):
                print self.x+self.y
              #  self.rect.midtop = (self.x, self.y)

        def collide(self, main, other):
                print "GOOOOT HIAR N00W!"
                main.removeObject(self)
