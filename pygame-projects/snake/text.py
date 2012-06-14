import pygame
import gameobject
import random

from pygame.locals import *

class draw(gameobject.GameObject):

	def __init__(self, x, y, surface,show):
	    super(draw, self).__init__(x, y, surface)
	    font=pygame.font.SysFont("Times New Roman",50)
            self.image = font.render(str(show), 1, (0,0,0))
	    self.image.convert()
            self.rect = self.image.get_rect()
            self.rect.midtop = (x, y)

	def collide(self,main,other):
	    pass
