import pygame
import random
import rungame as rg
import dumbmenu as dm
import json
from collections import deque

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
    SIZE = 0

    def __init__(self, surface, resolution):
        super(Background, self).__init__()
        self.x = 0
        self.y = 0
        self.surface = surface

        self.image = pygame.Surface(resolution, flags = SRCALPHA)
        self.image.convert()

        f = open("pacman.map", "r")
        data = json.load(f)

        self.matrix = data['map']
        Background.SIZE = data['size']

        res = resolution[0]

        self.blockSize = res / Background.SIZE
        self.generateBlocks()
        self.rect.topleft = (0, 0)
        #self.move_ghost()

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

    def bfs(self, g, start):
        queue, enqueued = deque([(None, start)]), set([start])
        while queue:
            parent, n = queue.popleft()
            yield parent, n
            new = set(g[n]) - enqueued
            enqueued |= new
            queue.extend([(n, child) for child in new])

    def shortest_path(self, g, start, end):
        parents = {}
        for parent, child in self.bfs(g, start):
            parents[child] = parent
            if child == end:
                revpath = [end]
                while True:
                    parent = parents[child]
                    revpath.append(parent)
                    if parent == start:
                        break
                    child = parent
                x = list(reversed(revpath))
                if len(x) < 10:
                    return x[1]
                else:
                    i, j = start
                    a = []
                    new_i = i + 1
                    new_j = j + 1
                    low_i = i - 1
                    low_j = j - 1
                    if(new_i == len(self.matrix)):
                        new_i = 0
                    if(low_i < 0):
                        low_i = len(self.matrix) - 1
                    if(new_j == len(self.matrix)):
                        new_j = 0
                    if(low_j < 0):
                        low_j = len(self.matrix) - 1

                    if self.matrix[new_i][j] == 0:
                        a.append((new_i, j))
                    if self.matrix[i][new_j] == 0:
                        a.append((i, new_j))
                    if self.matrix[i][low_j] == 0:
                        a.append((i, low_j))
                    if self.matrix[low_i][j] == 0:
                        a.append((low_i, j))
                    return random.choice(a)
                
        return None # or raise appropriate exception

    def move_ghost(self, pacman_x, pacman_y, phantom_x, phantom_y):
        count = {}
        phantom_x = phantom_x / self.blockSize
        phantom_y = phantom_y / self.blockSize        
        pacman_x = pacman_x / self.blockSize
        pacman_y = pacman_y / self.blockSize
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 0:
                    a = []
                    new_i = i + 1
                    new_j = j + 1
                    low_i = i - 1
                    low_j = j - 1
                    if(new_i == len(self.matrix)):
                        new_i = 0
                    if(low_i < 0):
                        low_i = len(self.matrix) - 1
                    if(new_j == len(self.matrix)):
                        new_j = 0
                    if(low_j < 0):
                        low_j = len(self.matrix) - 1

                    if self.matrix[new_i][j] == 0:
                        a.append((new_i, j))
                    if self.matrix[i][new_j] == 0:
                        a.append((i, new_j))
                    if self.matrix[i][low_j] == 0:
                        a.append((i, low_j))
                    if self.matrix[low_i][j] == 0:
                        a.append((low_i, j))
                    count[(i, j)] = a

        phantom = (phantom_x, phantom_y)
        pacman = (pacman_x, pacman_y)
        x, y = self.shortest_path(count, phantom, pacman)
        return (x * self.blockSize, y * self.blockSize)
    
    def move_rand(self, i, j):
        a = []
        i = i / self.blockSize
        j = j / self.blockSize
        new_i = i + 1
        new_j = j + 1
        low_i = i - 1
        low_j = j - 1
        if(new_i == len(self.matrix)):
            new_i = 0
        if(low_i < 0):
            low_i = len(self.matrix) - 1
        if(new_j == len(self.matrix)):
            new_j = 0
        if(low_j < 0):
            low_j = len(self.matrix) - 1

        if self.matrix[new_i][j] == 0:
            a.append((new_i * self.blockSize, j * self.blockSize))
        if self.matrix[i][new_j] == 0:
            a.append((i * self.blockSize, new_j * self.blockSize))
        if self.matrix[i][low_j] == 0:
            a.append((i * self.blockSize, low_j * self.blockSize))
        if self.matrix[low_i][j] == 0:
            a.append((low_i * self.blockSize, j * self.blockSize))
        return a

class Food(pygame.sprite.Sprite):

    def __init__(self, x, y, surface, size):
        super(Food, self).__init__()
        self.x = x
        self.y = y
        self.surface = surface

        # Surface of the person object.
        # Has flags for alpha chanels
        self.image = pygame.Surface((size, size), flags = SRCALPHA)
        self.image.convert()

        self.size = size
        self.set_color(pygame.Color(130, 70, 0))

        self.rect.topleft = (x, y)


    def set_color(self, color):
        """
        Sets person's color
        """
        
        x = self.size/2
        y = self.size/2
        radius = self.size/4
        self.rect = pygame.draw.circle(self.image, color, (x, y), radius)
        
    
    def update(self):
        """
        Updates graphical logic
        """


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

        self.frame = 0

    def set_color(self, color):
        """
        Sets person's color
        """
        
        x = self.size/2
        y = self.size/2
        radius = self.size/2 - 1
        self.rect = pygame.draw.circle(self.image, pygame.Color(color), (x, y), radius)
        x = self.size / 3 
        y = self.size / 3
        radius = self.size / 6
        self.rect = pygame.draw.circle(self.image, pygame.Color("black"), (x, y), radius)
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
        self.frame = self.frame + 1
        if(self.frame > 1):
            self.frame = 0

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
        eyerad = self.size/6

        self.rect = pygame.draw.circle(self.image, pygame.Color("yellow"), (cenx, ceny), radius)


        if self.frame == 0:
            if x == 0 and (y == -self.size or y > self.size): # goes down
                eyex = self.size / 3
                eyey = self.size / 3 
                vertex = [(cenx, ceny), (self.size-1, self.size-1), (1, self.size-1)]
            elif x == 0 and (y == self.size or y < -self.size): # goes up
                eyex = self.size / 3 
                eyey = self.size * 2 / 3
                vertex = [(cenx, ceny), (1, 1), (self.size-1, 1)]
            elif (x == -self.size or x > self.size) and y == 0: # goes right
                eyex = self.size / 3 
                eyey = self.size / 3
                vertex = [(cenx, ceny), (self.size-1, 1), (self.size-1, self.size-1)]
            elif (x == self.size or x < -self.size) and y == 0: #goes left
                eyex = self.size * 2 / 3 
                eyey = self.size / 3
                vertex = [(cenx, ceny), (1, self.size-1), (1, 1)]

            self.rect = pygame.draw.polygon(self.image, pygame.Color("black"), vertex)
            self.rect = pygame.draw.circle(self.image, pygame.Color("black"), (eyex, eyey), eyerad)
        else:
            if x == 0 and (y == -self.size or y > self.size): # goes down
                eyex = self.size / 3
                eyey = self.size / 3 
                vertex = [(cenx, ceny), (cenx, self.size-1), (cenx, ceny)]
            elif x == 0 and (y == self.size or y < -self.size): # goes up
                eyex = self.size / 3 
                eyey = self.size * 2 / 3
                vertex = [(cenx, ceny), (cenx, 1), (cenx, ceny)]
            elif (x == -self.size or x > self.size) and y == 0: # goes right
                eyex = self.size / 3 
                eyey = self.size / 3
                vertex = [(cenx, ceny), (self.size, ceny), (cenx, ceny)]
            elif (x == self.size or x < -self.size) and y == 0: #goes left
                eyex = self.size * 2 / 3 
                eyey = self.size / 3
                vertex = [(cenx, ceny), (0, ceny), (cenx, ceny)]
    
            self.rect = pygame.draw.polygon(self.image, pygame.Color("black"), vertex, 2)
            self.rect = pygame.draw.circle(self.image, pygame.Color("black"), (eyex, eyey), eyerad)
        
            
            
        self.x = self.new_x
        self.y = self.new_y
        self.rect.topleft = (self.x, self.y)


class Phantom(pygame.sprite.Sprite):
    
    #random.seed()
    def __init__(self,x,y,surface,size, color):
        super(Phantom,self).__init__()
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
        self.set_color(color)

        self.rect.topleft = (x, y)

    def set_color(self, color):
        """
        Sets person's color
        """
        #Draw circle part of phantom
        radius = self.size * 1 / 2
        x = self.size * 1 / 2
        y = self.size * 1 / 2
        self.rect = pygame.draw.circle(self.image, color, (x, y), radius)

        #Draw rectangle part of phantom
        vertex = [    (0, self.size * 1 / 2),
                    (self.size, self.size * 1 / 2),
                    (self.size, self.size * 3.5 / 5),
                    (0, self.size * 3.5 / 5) ]
        self.rect = pygame.draw.polygon(self.image, color, vertex)

        vertex = [    (0, self.size * 3.5 / 5),
                    (self.size, self.size * 3.5 / 5),
                    (self.size, self.size - 1),
                    (0, self.size-1) ]
        self.rect = pygame.draw.polygon(self.image, pygame.Color('black'), vertex)

        #Draw triangle parts of phantom
        for i in range(4):
            vertex = [    (self.size * i / 4, self.size * 3.5 / 5),
                        (self.size * (i + 1) / 4, self.size * 3.5 / 5),
                        (self.size * (i + 0.5) / 4, self.size - 1) ]
            self.rect = pygame.draw.polygon(self.image, color, vertex)

        #Draw eyes
        radius = self.size * 1 / 6
        radius2 = self.size * 1 / 8
        x = self.size * 1 / 4
        y = self.size * 1 / 2
        self.rect = pygame.draw.circle(self.image, pygame.Color("white"), (x, y), radius)
        self.rect = pygame.draw.circle(self.image, color, (x, y), radius2)
        x = self.size * 3 / 4
        self.rect = pygame.draw.circle(self.image, pygame.Color("white"), (x, y), radius)
        self.rect = pygame.draw.circle(self.image, color, (x, y), radius2)
        

    def move(self, next_move):
        """
        Compute the next move
        """
        self.new_x, self.new_y = next_move
 
    def update(self):
        """
        Updates graphical logic
        """
        self.x=self.new_x
        self.y=self.new_y
        self.rect.topleft = (self.x, self.y)


class Game(object):
    """
    PyGame sample game class
    """

    def __init__(self, settings = Settings()):
        pygame.init()
        self.settings = settings
        
        self.clock = pygame.time.Clock()

        self.show_menu()

        
    
    def init_game(self):
        """
        Init game from Settings object
        """

        # Init screen.
        self.screen = pygame.display.set_mode(self.settings.resolution)
        pygame.display.set_caption(self.settings.title)
        
        # Init background.
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(self.settings.background)
        
        
        #Init table
        self.table = Background(background, self.settings.resolution)
        self.tableSprite = pygame.sprite.RenderPlain(self.table)

        # Init food
        self.foods = []
        self.foodsSprite = []
        for i in range(Background.SIZE):
            for j in range(Background.SIZE):
                if self.table.matrix[i][j] == 0:# and (i % 2 == 0 and j % 2 == 0):
                    x = i * self.table.blockSize
                    y = j * self.table.blockSize
                    self.foods.append(Food(x, y, self.background, self.table.blockSize))
        self.foodsSprite = pygame.sprite.RenderPlain(self.foods)
        
        #Init pacman        
        x = Background.SIZE / 2 * self.table.blockSize
        self.pacman = Person(x, x, self.background, self.table.blockSize)
        self.pacmanSprite = pygame.sprite.RenderPlain(self.pacman)

        #Init ghosts
        self.ghosts=[]
        self.ghostsSprite = []
        self.ghosts.append(Phantom(0,0,self.background,self.table.blockSize, pygame.Color(0, 50, 250)))
        self.ghosts.append(Phantom(0,770,self.background,self.table.blockSize, (250, 50, 100)))
        self.ghosts.append(Phantom(770,770,self.background,self.table.blockSize, (0, 200, 0)))
        self.ghosts.append(Phantom(770,0,self.background,self.table.blockSize, (150, 150, 150)))
        self.ghostsSprite = pygame.sprite.RenderPlain(self.ghosts)


        self.direction = directions['start']
        self.temp_direction = directions['start']

        self.dirg =[]
        self.temp_dirg = []
        for i in range(4):
            self.dirg.append(random.choice(['up','down','left','right']))
            self.temp_dirg.append(random.choice(['up','down','left','right']))

        self.run()

    
    def show_menu(self):
        letters = 250, 250, 0
        cursor = 250, 250, 0


        size = width, height = self.settings.resolution
        screen = pygame.display.set_mode(size)
        screen.fill(self.settings.background)
        pygame.display.update()
        pygame.key.set_repeat(500,30)

        x = self.settings.resolution[0] / 2 - 80
        y = self.settings.resolution[1] / 2 - 100

        choose = dm.dumbmenu(screen, [
                        'Start Game',
                        'Quit Game'], x, y, 'Verdana', 32, 0.5, letters, cursor)

        if choose == 0:
            self.init_game()
        elif choose == 1:
            pygame.quit()
            exit()


    def run(self):
        """
        Run the game
        """
        while True:
            try:
                if not(self.game_tick()):
                    break;
            except GameException:
                return

        self.show_menu()

    def game_tick(self):
        """
        Handle events and redraw scene
        """
        self.clock.tick(7)

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

        #Food eat
        for f in self.foods:
            if self.pacman.x == f.x and self.pacman.y == f.y:
                f.set_color(pygame.Color("black"))
                self.foods.remove(f)

        #Game Over
        for i in range(4):
            if (self.pacman.x == self.ghosts[i].x) and (self.pacman.y == self.ghosts[i].y) :
                return False

        if len(self.foods) == 0:
            return False

        # Ghost Movement
        #self.temp_dirg=directions[random.choice(('left','right','up'))]
        for i in range(4):
            t=random.choice(range(3))
            if t is not 2:
                x, y = self.table.move_ghost(self.pacman.x, self.pacman.y, self.ghosts[i].x, self.ghosts[i].y)
            else:
                a, b = self.ghosts[i].x, self.ghosts[i].y
                x, y = random.choice(self.table.move_rand(a,b))
            self.ghosts[i].move((x, y))

        # Update all sprites.
        # Calls update method for the sprites defined.
        self.pacmanSprite.update()
        self.ghostsSprite.update()

        # Redraw.
        self.screen.blit(self.background, (0, 0))
        self.tableSprite.draw(self.screen)
        self.foodsSprite.draw(self.screen)
        self.pacmanSprite.draw(self.screen)
        self.ghostsSprite.draw(self.screen)
        pygame.display.flip()

        return True


