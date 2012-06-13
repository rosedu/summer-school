import pygame
import random

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
        self.resolution = (400, 400)
        # Backround color in Red Blue Green channels
        self.background = (0, 0, 0)
        # Mouse enabled
        self.mouse_enabled = True
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
                    self.rect = pygame.draw.polygon(self.image, pygame.Color(100, 100, 100), ver, 1)
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


class Person(pygame.sprite.Sprite):
    SIZE = 10

    def __init__(self, x, y, surface):
        super(Person, self).__init__()
        self.x = x
        self.y = y
        self.surface = surface

        # Surface of the person object.
        # Has flags for alpha chanels
        self.image = pygame.Surface((2 * Person.SIZE, 2 * Person.SIZE), flags = SRCALPHA)
        self.image.convert()

        self.selected = False
        self.set_color("yellow")

        self.rect.midtop = (x, y)
        self.new_x = 0
        self.new_y = 0

    def set_color(self, color):
        """
        Sets person's color
        """
        radius = Person.SIZE
        self.rect = pygame.draw.circle(self.image, pygame.Color(color), (radius, radius), radius)

    def move(self, next_move):
        """
        Compute the next move
        """
        self.new_x, self.new_y = next_move
    
    def update(self):
        """
        Updates graphical logic
        """
               
        self.x = self.new_x
        self.y = self.new_y

        self.rect.topleft = (self.x, self.y)

    def clicked(self, pos):
        """
        Logic if object is clicked
        """

        # Get absolute position.
        abs_rect = self.rect.move(self.image.get_abs_offset())
        if abs_rect.contains(pos, (1, 1)):
            return True
        return False

class Fantoma(pygame.sprite.Sprite):
    SIZE = 15;
    #random.seed()
    def __init__(self,x,y,surface):
        super(Fantoma,self).__init__()
        self.x = x
        self.y = y
        self.surface = surface
        self.direction = random.choice([1,2,3,4]);

        # Surface of the person object.
        # Has flags for alpha chanels
        self.image = pygame.Surface((2 * Person.SIZE, 2 * Person.SIZE), flags = SRCALPHA)
        self.image.convert()

        self.selected = False
        self.set_color("white")

        self.rect.midtop = (x, y)

    def set_color(self, color):
        """
        Sets person's color
        """
        radius = Person.SIZE
        self.rect = pygame.draw.circle(self.image, pygame.Color(color), (radius, radius), radius)

    def update(self):
        """
        Updates graphical logic
        """
        while True:
            if self.direction == 1 and self.y-1 > 0 : 
                self.x=self.x 
                self.y=self.y - 1
                break
            else :
                self.direction = 2

            if self.direction == 2 and self.x+1 < 480 : 
                self.x=self.x + 1
                self.y=self.y  
                break
            else :
                self.direction = 3

            if self.direction == 3 and self.y+1 < 480: 
                self.x=self.x 
                self.y=self.y + 1
                break
            else :
                self.direction = 4

            if self.direction == 4 and self.x-1 >0 : 
                self.x=self.x - 1
                self.y=self.y
                break
            else :
                self.direction = 1
        self.rect.midtop = (self.x, self.y)


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

    def init_from_settings(self, settings):
        """
        Init game from Settings object
        """

        # Init screen.
        self.screen = pygame.display.set_mode(settings.resolution)
        pygame.display.set_caption(settings.title)
        pygame.mouse.set_visible(settings.mouse_enabled)
        
        # Init background.
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(settings.background)
        
        #Init pacman        
        self.pacman = Person(0, 0, self.background)
        self.sprites.append(self.pacman)

        #Init table
        self.table = Background(background, settings.resolution)
        self.sprites.append(self.table)

        

    def run(self):
        """
        Run the game
        """
        while True:
            try:
                self.game_tick()
            except GameException:
                return

    def spawn_random_person(self):
        w, h = self.screen.get_size()
        x = random.randint(0, w)
        y = random.randint(0, h)
        self.persons.append(Person(x, y, self.background))

        # Add new persons to rendered group
        self.allsprites = pygame.sprite.RenderPlain(self.persons)

    def game_tick(self):
        """
        Handle events and redraw scene
        """
        self.clock.tick(5)

        # Check events.
        for event in pygame.event.get():
            if event.type == QUIT:
                raise GameException
            elif event.type == KEYUP:
                #self.direction = directions['start']
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

        if self.table.isValid((self.pacman.x, self.pacman.y), self.temp_direction):
            self.direction = self.temp_direction
        else:
            if not(self.table.isValid((self.pacman.x, self.pacman.y), self.direction)):
                self.direction = directions['start']
            self.temp_direction = self.direction

        

        x, y = self.table.getActualXY((self.pacman.x, self.pacman.y), self.direction)
        self.pacman.move((x, y))

        # Update all sprites.
        # Calls update method for the sprites defined.

        self.allsprites.update()

        # Redraw.
        self.screen.blit(self.background, (0, 0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()


