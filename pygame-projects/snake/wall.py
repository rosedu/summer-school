import pygame
import gameobject
import random

from pygame.locals import *

class Wall(gameobject.GameObject):

	def __init__(self, x, y, surface, time = random.randint(0,50)):
		super(Wall, self).__init__(x, y, surface)
		self.SIZE = gameobject.GameObject.SIZE
		self.image = pygame.Surface((2*self.SIZE, 2*self.SIZE),
				flags = SRCALPHA)
		self.image.convert()

		self.rect = pygame.draw.circle(self.image,pygame.Color("brown"),(self.SIZE,self.SIZE),
				self.SIZE)

		self.rect.midtop = (x,y)

	def collide(self,main,other):
		main.removeObject(other)
