import pygame
import random
import snake
import food
import wall

from pygame.locals import *

class GameException(Exception):
    pass

class Settings(object):
    def __init__(self):
        self.resolution = ( 800, 600)
        self.background = (255, 228, 225)
        self.title = "Snake" 

class Game(object):

    def __init__(self, settings = Settings()):
        pygame.init()
        self.score = 0
        self.loadSettings(settings)
        self.clock = pygame.time.Clock()
        self.snakeParts = [snake.SnakePart(400,300, self.background)]
        self.gameObjects = [self.snakeParts[0]]
	
	for i in range(0,820,20):
	    self.gameObjects.append(wall.Wall(i,-10, self.background)) 
	
	for i in range(0,820,20):
	    self.gameObjects.append(wall.Wall(i,590, self.background)) 
        self.sprites = pygame.sprite.RenderPlain(self.gameObjects)

        self.move_timer = 0
        self.score = 0
        self.food_timer = 200


    def loadSettings(self, settings):
        self.screen = pygame.display.set_mode(settings.resolution)
        pygame.display.set_caption(settings.title)
        pygame.mouse.set_visible(False)

        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(settings.background)

    def addObject(self, obj):
        self.gameObjects.append(obj)
        self.sprites.add(obj)
    
    
    def removeObject(self, obj):
        self.gameObjects.remove(obj)
        self.sprites.remove(obj)
    
    def run(self):
        isRunning = True
        while True:
            try:
                self.tick()
                if not isRunning:
                    return
            except GameException:
                return

    def tick(self):
        self.clock.tick(60)
        moved = False
        for event in pygame.event.get():
            if event.type == QUIT:
                raise GameException
            elif event.type == KEYDOWN:
                if event.key == 273:
                    moved = self.snakeParts[0].moveTo(1)
                if event.key == 274:
                    moved = self.snakeParts[0].moveTo(2)
                if event.key == 276:
                    moved = self.snakeParts[0].moveTo(3)
                if event.key == 275:
                    moved = self.snakeParts[0].moveTo(4)
        if not moved:
            self.move_timer = self.move_timer+1
            if self.move_timer == 10:
                self.snakeParts[0].moveTo(self.snakeParts[0].lastDirection)
                self.move_timer = 0
        else:
            self.move_timer = 0
            
        self.food_timer = self.food_timer - 1
        if self.food_timer == 0:
	    self.addObject(food.Food(random.randint(0,100)*8,random.randint(0,75)*8, self.background)) 
            self.food_timer = 200
        
        for obj in self.gameObjects:
                for obj2 in self.gameObjects:
                        if obj != obj2 and obj.rect.colliderect(obj2):
                            obj.collide(self, obj2)
                            obj2.collide(self, obj)
                            print self.score
        
        self.sprites.update()
        self.screen.blit(self.background,(0,0))
        self.sprites.draw(self.screen)
        pygame.display.flip()
