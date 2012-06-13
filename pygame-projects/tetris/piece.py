import pygame, os
from pygame.locals import *

BASE_FALL_RATE = 2
FALL_RATE_MULTIPLIER = 10

current_id = 0

class Piece(pygame.sprite.Sprite):
    """
    Movable piece with arrows
    Return: piece object
    Methods: """
    # Width = Height = L
    L = 15

    def __init__(self, type_of_piece):
        ''' (x, y) = initialpos
            image = image from file'''
        super(Brick, self).__init__()
        self.ID = current_id
        current_id += 1
        
        self.type = None
        self.falling = True
        self.fallrate = BASE_FALL_RATE

        #screen = pygame.display.get_surface()
        #self.rect = screen.get_rect()
        #default direction is down
        self.direction = 'd' # 'l', 'r', 'd'
        self.mode = 1  
        self.put_shape(type_of_piece)

    def put_shape(self, type_of_piece):
        """
        Sets the brick's color
        """
        if type_of_block == 1:
            self.image = pygame.image.load(os.path.join('data','tealbrick.png')).convert()
            self.starting_pos = [Rect(50,-10,L,L), Rect(65,-10,L,L), Rect(80,-10,L,L), Rect(95, -10, L, L)]
            self.display_pos = [Rect(200,95,L,L), Rect(215,95,L,L), Rect(230,95,L,L), Rect(245, 95, L, L)]
            self.type = 'I'
        
        if type_of_piece == 2: #S
            self.image = pygame.image.load(os.path.join('data', 'redbrick.png')).convert()
            self.starting_pos = [Rect(95,-10,L,L), Rect(80,-10,L,L), Rect(80,5,L,L), Rect(65,5,L,L)]
            self.display_pos = [Rect(245,95,L,L), Rect(230,95,L,L), Rect(230,110,L,L), Rect(215,110,L,L)]
            self.type = 'S'
        if type_of_piece == 3: #Z
            self.image = pygame.image.load(os.path.join('dat', 'greenbrick.png')).convert()
            self.starting_pos = [Rect(65,-10,L,L), Rect(80,-10,L,L), Rect(80,5,L,L), Rect(95,5,L,L)]
            self.display_pos = [Rect(215,95,L,L), Rect(230,95,L,L), Rect(230,110,L,L), Rect(245,110,L,L)]
            self.type = 'Z'
        if type_of_block == 4: #T 
            self.image = pygame.image.load(os.path.join('data', 'purplebrick.png')).convert()
            self.starting_pos = [Rect(80,-10,L,L), Rect(65,5,L,L), Rect(80,5,L,L), Rect(95,5,L,L)]
            self.display_pos = [Rect(230,95,L,L), Rect(215,110,L,L), Rect(230,110,L,L), Rect(245,110,L,L)]
            self.type = 'T'

    def coord(self):
        return (self.x, self.y)
    
    def update(self, time_passed, grid, speed):
        for pos in self.starting_pos:
            if(pos.bottom == 305):
                self.falling = False
            for i in grid:
                for ii in i.starting_pos:
                    if pos.bottom == ii.top and pos.right == ii.right and pos.left == ii.left:
                        self.falling = False
        if self.counter < time_passed:
            self.counter = time_passed + speed
            for pos in self.starting_pos:
                pos.top += L
        
    def move_right(self, grid):
        for pos in self.starting_pos:
            if(pos.right == 155):
                return
            for i in grid:
                for ii in i.starting_pos:
                    if pos.right == ii.left and pos.top == ii.top:
                        return      
        for pos in self.starting_pos:
            pos.right +=L
        
    def move_left(self, grid):
        for pos in self.starting_pos:
            if(pos.left == 5):
                return
            for i in grid:
                for ii in i.starting_pos:
                    if pos.left == ii.right and pos.top == ii.top:
                        return          
        for pos in self.starting_pos:
            pos.right -=L

