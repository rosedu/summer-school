"""
Michal's Side-Scrolling Game
by Michal Wallace - http://www.sabren.net/
This code is in the public domain.

This is really just a proof of concept.
The code isn't very well factored and
the art and physics are horrible, but
it does show how pygame could be used
to make a side-scrolling action game.
"""
import os, sys
import random, math, pygame
from pygame.locals import *

WINSIZE = [640, 480]

def load_image(name, colorkey=None):
    """
    stolen from the chimp example.
    """
    fullname = os.path.join('sprites', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()



LEFT, RIGHT = -1, 1
class Hero(pygame.sprite.Sprite):
    def __init__(self, world):
        pygame.sprite.Sprite.__init__(self)
        self.other, self.rect = load_image('hero2.gif', -1)
        self.image, self.rect = load_image('hero.gif', -1)
        self.area = pygame.display.get_surface().get_rect()
        self.rect.bottomleft = 50,240
        self.running = 0
        self.runspeed = 1
        self.jumping = 0
        self.airtime = 100
        self.airtick = 0
        self.airspeed = 1
        self.facing = RIGHT
        self.world = world
        self.tick = 0

    def update(self):

        ## animation:
        
        ## movement and scrolling:
        if self.running:
            self.rect = self.rect.move((self.runspeed * self.facing,0))
	    


            if self.rect.right > 600:
                self.rect.right = 600                
		# modificare animatie
		self.tick +=1
		if self.tick == 10:
		    self.image, self.other = self.other, self.image
		    self.tick = 0
		self.world.scroll(LEFT * self.runspeed)

            if self.rect.left < 50:
                self.rect.left = 50
                self.world.scroll(RIGHT * self.runspeed)
	        # modificare animatie
	        self.tick +=1
                if self.tick == 10:
            	    self.image, self.other = self.other, self.image
            	    self.tick = 0



        ## jumping:
        if self.jumping:
            if self.airtick < self.airtime:
                self.rect = self.rect.move((0,-self.airspeed))
            elif self.airtick >= self.airtime * 1.5:
                self.rect = self.rect.move((0,self.airspeed))
            self.airtick += 1
            if self.airtick == self.airtime * 2.5:                
                self.jumping = 0


    def face(self, direction):
        if direction != self.facing:
            self.facing = direction
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.other = pygame.transform.flip(self.other, 1, 0)

    def jump(self):
        if not self.jumping:
            self.airtick = 0
            self.jumping = 1

    def start(self, direction):
        self.running = 1
	self.face(direction)
	#self.image = pygame.transform.flip(self.image, 1, 0)
	#self.other = pygame.transform.flip(self.other, 1, 0)
        #self.face(direction)

    def stop(self):
        self.running = 0
        


class World(pygame.sprite.Sprite):
    """
    The background image.
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('world.gif', -1)
    def scroll(self, vector):
        self.rect = self.rect.move((vector,0))
        

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINSIZE)
    pygame.display.set_caption("Super Mihai")
    white = 255, 240, 200
    black = 0, 0, 0

    world = World()
    hero = Hero(world)
    sprites = pygame.sprite.RenderPlain((world, hero))
    
    done = 0
    while not done:
        screen.fill(black)
        pygame.draw.line(screen, white, (0, 240), (640,240))
        sprites.update()
        sprites.draw(screen)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == QUIT:
                done = 1
            elif e.type==KEYDOWN:
                if   e.key==  K_RIGHT: hero.start(RIGHT)
                elif e.key==  K_LEFT:  hero.start(LEFT)
                elif e.key==  K_UP: hero.jump()
            elif e.type==KEYUP:
                if   e.key== K_ESCAPE: done = 1
                elif e.key== K_RIGHT: hero.stop()
                elif e.key== K_LEFT: hero.stop()

if __name__=="__main__":
    main()
