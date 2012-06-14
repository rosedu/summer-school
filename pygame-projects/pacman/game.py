import pygame
import random
import rungame as rg
import dumbmenu as dm

directions  = { "start": (0, 0), "left": (-1, 0), "right": (1, 0), "down": (0, 1), "up": (0, -1) }

from pygame.locals import *

class GameException(Exception):
    """
    Exception raised during game logic
    """
    pass

class Settings(object):
    """
    Game Settings class

    Members represent different settings for the game:
    resolution: resolution of the game
    background: color of the background
    mouse_enabled: enable the mouse
    """
    def __init__(self):
        """
        Initialize with default settings
        """
        # Size of the main window.
        self.resolution = (800, 800)
        # Backround color in Red Blue Green channels
        self.background = (0, 0, 0)
        # Title
        self.title = "PacMan"

class Background(pygame.sprite.Sprite):
    SIZE = 30

    def __init__(self, surface, resolution):
        super(Background, self).__init__()
        self.x = 0
        self.y = 0
        self.surface = surface

        self.image = pygame.Surface(resolution, flags = SRCALPHA)
        self.image.convert()

        self.matrix = [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0], 
                        [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]

        res = resolution[0]

        self.blockSize = res / Background.SIZE
        self.generateBlocks()
        self.rect.topleft = (0, 0)

    def generateBlocks(self): 
        self.blocks = []
        r = 0
        for row in self.matrix:
            c = 0
            for pos in row:
                ver = [ (r*self.blockSize, c*self.blockSize), 
                        (r*self.blockSize + self.blockSize, c*self.blockSize), 
                        (r*self.blockSize + self.blockSize, c*self.blockSize + self.blockSize), 
                        (r*self.blockSize, c*self.blockSize + self.blockSize)]
                if pos == 1:
                    self.rect = pygame.draw.polygon(self.image, pygame.Color(200, 200, 200), ver)
                else:
                    self.rect = pygame.draw.polygon(self.image, pygame.Color(30, 30, 30), ver, 1)
                c = c+1
            r = r+1

    def isValid(self, (x, y), d):
        rel_x = x / self.blockSize
        rel_y = y / self.blockSize

        new_x = rel_x + d[0]
        new_y = rel_y + d[1] 

        if(new_x == Background.SIZE):
            new_x = 0
        if(new_x < 0):
            new_x = Background.SIZE-1
        if(new_y == Background.SIZE):
            new_y = 0
        if(new_y < 0):
            new_y = Background.SIZE-1

        if self.matrix[new_y][new_x] == 0:
            return True
        return False

    def getActualXY(self, (x, y), d):
        rel_x = x / self.blockSize
        rel_y = y / self.blockSize

        new_x = rel_x + d[0]
        new_y = rel_y + d[1] 

        if(new_x == Background.SIZE):
            new_x = 0
        if(new_x < 0):
            new_x = Background.SIZE-1
        if(new_y == Background.SIZE):
            new_y = 0
        if(new_y < 0):
            new_y = Background.SIZE-1

        return (new_x*self.blockSize, new_y*self.blockSize)

    def getNext(self, (x, y), (px, py)):
        return (x, y)
    
    def find(self, x, y, px, py):
        t1 = x - px
        t2 = y - py
        if abs(t1) > abs(t2):
            if t1 > 0 :
              return 'right'
            else :
              return 'left'
        else :
            if t2 > 0 :
              return 'up'
            else :
              return 'down'

class Person(pygame.sprite.Sprite):

    def __init__(self, x, y, surface, size):
        super(Person, self).__init__()
        self.x = x
        self.y = y
        self.surface = surface

        # Surface of the person object.
        # Has flags for alpha chanels
        self.image = pygame.Surface((size, size), flags = SRCALPHA)
        self.image.convert()

        self.selected = False
        self.size = size
        self.set_color("yellow")

        self.rect.topleft = (x, y)
        self.new_x = 0
        self.new_y = 0
        self.delta_x = -self.size
        self.delta_y = 0

    def set_color(self, color):
        """
        Sets person's color
        """

        x = self.size/2
        y = self.size/2
        radius = self.size/2 - 1
        self.rect = pygame.draw.circle(self.image, pygame.Color(color), (x, y), radius)
        self.rect = pygame.draw.polygon(self.image, pygame.Color("black"), [(x, y), (self.size - 1, 1), (self.size - 1, self.size - 1)])
        
    def move(self, next_move):
        """
        Compute the next move
        """
        self.new_x, self.new_y = next_move
    
    def update(self):
        """
        Updates graphical logic
        """
        
        x = self.x - self.new_x
        y = self.y - self.new_y
        
        if y == 0 and x == 0:
            x = self.delta_x
            y = self.delta_y
        else:
            self.delta_x = x
            self.delta_y = y
            
            
        cenx = self.size/2
        ceny = self.size/2
        radius = self.size/2 - 1
        if x == 0 and y < 0: # goes down
            vertex = [(cenx, ceny), (self.size-1, self.size-1), (1, self.size-1)]
        elif x == 0 and y > 0: # goes up
            vertex = [(cenx, ceny), (1, 1), (self.size-1, 1)]
        elif x < 0 and y == 0: # goes right
            vertex = [(cenx, ceny), (self.size-1, 1), (self.size-1, self.size-1)]
        elif x > 0 and y == 0: #goes left
            vertex = [(cenx, ceny), (1, self.size-1), (1, 1)]
        
        self.rect = pygame.draw.circle(self.image, pygame.Color("yellow"), (cenx, ceny), radius)
        self.rect = pygame.draw.polygon(self.image, pygame.Color("black"), vertex)
            
            
        self.x = self.new_x
        self.y = self.new_y
        self.rect.topleft = (self.x, self.y)


class Fantoma(pygame.sprite.Sprite):
    
    #random.seed()
    def __init__(self,x,y,surface,size):
        super(Fantoma,self).__init__()
        self.x = x
        self.y = y
        self.size = size
        self.surface = surface
        self.direction = random.choice([1,2,3,4]);
        self.image = pygame.Surface((size, size), flags = SRCALPHA)
        self.image.convert()

        self.new_x = 0
        self.new_y = 0
        self.delta_x = -self.size
        self.delta_y = 0


     
        # Surface of the person object.
        # Has flags for alpha chanels
        self.image = pygame.Surface((self.size, self.size), flags = SRCALPHA)
        self.image.convert()
        self.set_color("blue")

        self.rect.topleft = (x, y)

    def set_color(self, color):
        """
        Sets person's color
        """
        radius = self.size/2
        self.rect = pygame.draw.circle(self.image, pygame.Color(color), (radius, radius), radius)

    def move(self, next_move):
        """
        Compute the next move
        """
        self.new_x, self.new_y = next_move
 
    def update(self):
        """
        Updates graphical logic"""
        self.x=self.new_x
        self.y=self.new_y
        self.rect.topleft = (self.x, self.y)


class Game(object):
    """
    PyGame sample game class
    """

    def __init__(self, settings = Settings()):
        pygame.init()
        self.sprites = []

        self.init_from_settings(settings)
        self.clock = pygame.time.Clock()

        self.allsprites = pygame.sprite.RenderPlain(self.sprites)

        self.direction = directions['start']
        self.temp_direction = directions['start']


        self.dirg =[]
        self.temp_dirg = []
        for i in range(4):
            self.dirg.append(random.choice(['up','down','left','right']))
            self.temp_dirg.append(random.choice(['up','down','left','right']))
    
    def init_from_settings(self, settings):
        """
        Init game from Settings object
        """

        # Init screen.
        self.screen = pygame.display.set_mode(settings.resolution)
        pygame.display.set_caption(settings.title)
        
        # Init background.
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(settings.background)
        
        #Init table
        self.table = Background(background, settings.resolution)
        self.sprites.append(self.table)
        
        #Init pacman        
        x = Background.SIZE / 2 * self.table.blockSize
        self.pacman = Person(x, x, self.background, self.table.blockSize)
        self.sprites.append(self.pacman)

        #Init ghosts
        self.ghosts=[]
        
        self.ghosts.append(Fantoma(0,0,self.background,self.table.blockSize))
        self.sprites.append(self.ghosts[0])
        self.ghosts.append(Fantoma(0,770,self.background,self.table.blockSize))
        self.sprites.append(self.ghosts[1])
        self.ghosts.append(Fantoma(770,770,self.background,self.table.blockSize))
        self.sprites.append(self.ghosts[2])
        self.ghosts.append(Fantoma(770,0,self.background,self.table.blockSize))
        self.sprites.append(self.ghosts[3])

    
    def reset(self):
        red   = 255,  0,  0
        green =   0,255,  0
        blred   = 255,  0,  0
        green =   0,255,  0
        blue  =   0,  0,255


        size = width, height = 340,240	
        screen = pygame.display.set_mode(size)
        screen.fill(blue)
        pygame.display.update()
        pygame.key.set_repeat(500,30)

        choose = dm.dumbmenu(screen, [
                        'Start Game',
                        'Options',
                        'Manual',
                        'Show Highscore',
                        'Quit Game'], 64,64,None,32,1.4,green,red)

        if choose == 0:
            rg.main()
            print "You choose 'Start Game'."
        elif choose == 1:
            print "You choose 'Options'."
        elif choose == 2:
            print "You choose 'Manual'."
        elif choose == 3:
            print "You choose 'Show Highscore'."
        elif choose == 4:
             print "You choose 'Quit Game'."
        pygame.quit()
        exit()


    def run(self):
        """
        Run the game
        """
        while True:
            try:
                self.game_tick()
            except GameException:
                return

    def game_tick(self):
        """
        Handle events and redraw scene
        """
        self.clock.tick(8)

        # Check events.
        for event in pygame.event.get():
            if event.type == QUIT:
                raise GameException
            elif event.type == KEYUP:
                continue
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.temp_direction = directions["down"]
                elif event.key == K_UP:
                    self.temp_direction = directions["up"]
                elif event.key == K_LEFT:
                    self.temp_direction = directions["left"]
                elif event.key == K_RIGHT:
                    self.temp_direction = directions["right"]
                continue


        # Pacman movement
        if self.table.isValid((self.pacman.x, self.pacman.y), self.temp_direction):
            self.direction = self.temp_direction
        else:
            if not(self.table.isValid((self.pacman.x, self.pacman.y), self.direction)):
                self.direction = directions['start']
            self.temp_direction = self.direction
            
        x, y = self.table.getActualXY((self.pacman.x, self.pacman.y), self.direction)
        self.pacman.move((x, y))



        # Ghost Movement
        #self.temp_dirg=directions[random.choice(('left','right','up'))]
        for i in range(4):
            self.temp_dirg[i]=directions[self.table.find(self.pacman.x, self.pacman.y,
                                                  self.ghosts[i].x,
                                                  self.ghosts[i].y)]
            if self.table.isValid((self.ghosts[i].x, self.ghosts[i].y),
                        self.temp_dirg[i]):
                self.dirg[i] = self.temp_dirg[i]
            else:
                if not(self.table.isValid((self.ghosts[i].x,
                        self.ghosts[i].y),
                        self.dirg[i])):
                    self.dirg[i] = directions['up']
                self.temp_dirg[i] = self.dirg[i]
        
            x, y = self.table.getActualXY((self.ghosts[i].x,
                    self.ghosts[i].y), self.dirg[i])
            self.ghosts[i].move((x, y))

        #Game Over
        for i in range(4):
            if (self.pacman.x == self.ghosts[i].x) and (self.pacman.y ==
            self.ghosts[i].y) :
                    self.reset()
                    print 'TATATATAATA'
        # Update all sprites.
        # Calls update method for the sprites defined.
        self.allsprites.update()

        # Redraw.
        self.screen.blit(self.background, (0, 0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()


