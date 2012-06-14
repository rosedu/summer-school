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
        self.snakeParts[0].isHead = True
        self.gameObjects = [self.snakeParts[0]]
	
	for i in range(0,820,20):
	    self.gameObjects.append(wall.Wall(i,-10, self.background)) 
	
	for i in range(0,820,20):
	    self.gameObjects.append(wall.Wall(i,590, self.background)) 
        self.sprites = pygame.sprite.RenderPlain(self.gameObjects)

        self.move_timer = 0
        self.score = 0
        self.food_timer = random.randint(100,200)


    def loadSettings(self, settings):
        self.screen = pygame.display.set_mode(settings.resolution)
        pygame.display.set_caption(settings.title)
        pygame.mouse.set_visible(False)

        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(settings.background)

    def addObject(self, obj):
        if len(self.gameObjects) > 100:
            return
        self.gameObjects.append(obj)
        self.sprites.add(obj)

    
    
    def removeObject(self, obj):
        self.gameObjects.remove(obj)
        self.sprites.remove(obj)
    
    def scoreshow(self):
	font=pygame.font.SysFont("Times New Roman",50)
	s=font.render(str(self.score),True,(0,0,0))
	s.get_flags()
	self.screen.blit(s,(20,20))
	pygame.display.flip()
	pygame.event.pump()

    def run(self):
        isRunning = True
        while True:
            try:
                self.tick()
                if not isRunning:
                    return
            except GameException:
                return
    def addsnakepart(self):
        size=self.snakeParts[0].SIZE
        snk=self.snakeParts[len(self.snakeParts)-1]
        news = snake.SnakePart(snk.x,snk.y,self.background)
        self.snakeParts.append(news)
        self.addObject(news)

    def moveAllSnakeParts(self):
        #print "inainte de for"
        ls=len(self.snakeParts)
        #ll= range(ls-1,0,-1)
        #for i in ll:
        #    self.snakeParts[i].moveTo(self.snakeParts[i-1].lldir)
            #print "in for"
            #if self.snakeParts[i-1].lastDirection == 1
            #    self.snakeParts[i].moveTo(
        for i in range(1,ls):
            if self.snakeParts[i].x == self.snakeParts[0].lastx and  self.snakeParts[i].y == self.snakeParts[0].lasty:
                self.snakeParts[i].moveTo(self.snakeParts[0].lastDirection)
            else:
                self.snakeParts[i].moveTo(self.snakeParts[0].lldir)
            #print i

    def tick(self):
        self.clock.tick(60)
        self.scoreshow()
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
                self.move_timer = 0
                self.moveAllSnakeParts()
                self.snakeParts[0].moveTo(self.snakeParts[0].lastDirection)
                
                      
        else:
            self.move_timer = 0
            self.moveAllSnakeParts()

        self.food_timer = self.food_timer - 1

        if self.food_timer == 0:
            self.addObject(food.Food(random.randint(0,100)*8,random.randint(0,75)*8, self.background)) 
            self.food_timer = random.randint(100,200)
       
        for obj in self.gameObjects:
            for obj2 in self.gameObjects:
                if obj != obj2 and obj.rect.colliderect(obj2):
                    obj.collide(self, obj2)
                   # obj2.collide(self, obj)
        
        toRemove = []
        for obj in self.gameObjects:
                if hasattr(obj, "dead"):
                    if obj.dead:
                        toRemove.append(obj)
        for obj in toRemove:
            self.removeObject(obj)            
                                 
        self.sprites.update()
        self.screen.blit(self.background,(0,0))
        self.sprites.draw(self.screen)
        pygame.display.flip()
