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

		self.rect = pygame.draw.polygon(self.image,pygame.Color("brown"),[(self.SIZE-10,self.SIZE-10),
				(self.SIZE-10,self.SIZE+10),(self.SIZE+10,self.SIZE+10),(self.SIZE+10,self.SIZE-10)])

		self.rect.midtop = (x,y)

	def collide(self,main,other):
		main.scoreshow(200,200,"You Loose!!!")
		main.scoreshow(150,260,"Press escape to exit")
		main.waitForPlayerToPressKey()
		main.removeObject(other)
