import pygame,  os
from pygame.locals import *

#current_id = 0
pygame.display.set_mode()

class Piece(pygame.sprite.Sprite):
    """
    Movable piece with arrows
    Return: piece object
    Methods: """
    # Width = Height = 15

    def __init__(self, type_of_piece):
        ''' (x, y) = initialpos
            image = image from file'''
        super(Piece, self).__init__()
        
        self.type = None
        self.falling = True
        self.state = 1
        self.counter = 0

        self.mode = 1  
        self.put_shape(type_of_piece)

    def put_shape(self, type_of_piece):
        """
        Sets the brick's color
        """
        if type_of_piece == 1: #I
            self.image = pygame.image.load(os.path.join('data','tealbrick.png')).convert()
            self.starting_pos = [Rect(50,-10,15,15),
			    Rect(65,-10,15,15), Rect(80,-10,15,15), Rect(95, -10, 15, 15)]
            self.display_pos = [Rect(200,95,15,15), Rect(215,95,15,15), Rect(230,95,15,15), Rect(245, 95, 15, 15)]
            self.type = 'I'
        
        if type_of_piece == 2: #S
            self.image = pygame.image.load(os.path.join('data', 'redbrick.png')).convert()
            self.starting_pos = [Rect(95,-10,15,15), Rect(80,-10,15,15), Rect(80,5,15,15), Rect(65,5,15,15)]
            self.display_pos = [Rect(245,95,15,15), Rect(230,95,15,15), Rect(230,110,15,15), Rect(215,110,15,15)]
            self.type = 'S'
        if type_of_piece == 3: #Z
            self.image = pygame.image.load(os.path.join('data', 'greenbrick.png')).convert()
            self.starting_pos = [Rect(65,-10,15,15), Rect(80,-10,15,15), Rect(80,5,15,15), Rect(95,5,15,15)]
            self.display_pos = [Rect(215,95,15,15), Rect(230,95,15,15), Rect(230,110,15,15), Rect(245,110,15,15)]
            self.type = 'Z'
        if type_of_piece == 4: #T 
            self.image = pygame.image.load(os.path.join('data', 'purplebrick.png')).convert()
            self.starting_pos = [Rect(80,-10,15,15), Rect(65,5,15,15), Rect(80,5,15,15), Rect(95,5,15,15)]
            self.display_pos = [Rect(230,95,15,15), Rect(215,110,15,15), Rect(230,110,15,15), Rect(245,110,15,15)]
            self.type = 'T'

    def coord(self):
        return (self.x, self.y)
    
    def update(self, time_passed, grid, speed):
        for pos in self.starting_pos:
            if pos.bottom == 305:
                self.falling = False
            for i in grid:
                for ii in i.starting_pos:
                    if pos.bottom == ii.top and pos.right == ii.right and pos.left == ii.left:
                        self.falling = False
        if self.counter < time_passed:
            self.counter = time_passed + speed
            for pos in self.starting_pos:
                pos.top += 15
        
    def move_right(self, grid):
        for pos in self.starting_pos:
            if pos.right == 155:
                return
            for i in grid:
                for ii in i.starting_pos:
                    if pos.right == ii.left and pos.top == ii.top:
                        return      
        for pos in self.starting_pos:
            pos.right +=15
        
    def move_left(self, grid):
        for pos in self.starting_pos:
            if pos.left == 5:
                return
            for i in grid:
                for ii in i.starting_pos:
                    if pos.left == ii.right and pos.top == ii.top:
                        return          
        for pos in self.starting_pos:
            pos.right -=15
   
    def not_ok(self, pos, old_pos):
        if pos.right > 155 or pos.top < 5 or pos.left < 5:
            self.starting_pos = old_pos[:]
            return True
        return False

    def rotate(self):
        old_pos = self.starting_pos[:]
        # type 'I' can rotate in 2 ways
        if self.type == 'I':
            if self.state == 1:
                self.starting_pos[0] = Rect(self.starting_pos[2].left, self.starting_pos[2].top-2*15,15,15)
                self.starting_pos[1] = Rect(self.starting_pos[2].left, self.starting_pos[2].top-15,15,15)
                self.starting_pos[3] = Rect(self.starting_pos[2].left, self.starting_pos[2].top+15,15,15)
                for pos in self.starting_pos:
                    if self.not_ok(pos, old_pos):
                        return
                self.state = 2
                return
            if self.state == 2:
                self.starting_pos[0] = Rect(self.starting_pos[2].left-2*15, self.starting_pos[2].top,15,15)
                self.starting_pos[1] = Rect(self.starting_pos[2].left-15, self.starting_pos[2].top,15,15)
                self.starting_pos[3] = Rect(self.starting_pos[2].left+15, self.starting_pos[2].top,15,15)
                for pos in self.starting_pos:
                    if self.not_ok(pos, old_pos):
                        return
                self.state = 1
                return
        # type 'S' rotations
        if self.type == 'S':
            if self.state == 1:
                self.starting_pos[0] = Rect(self.starting_pos[1].left, self.starting_pos[1].top-15,15,15)
                self.starting_pos[2] = Rect(self.starting_pos[1].left+15, self.starting_pos[1].top,15,15)
                self.starting_pos[3] = Rect(self.starting_pos[1].left+15, self.starting_pos[1].top+15,15,15)
                for pos in self.starting_pos:
                    if self.not_ok(pos, old_pos):
                        return
                self.state = 2
                return
            if self.state == 2:
                self.starting_pos[0] = Rect(self.starting_pos[1].left+15, self.starting_pos[1].top,15,15)
                self.starting_pos[2] = Rect(self.starting_pos[1].left, self.starting_pos[1].top+15,15,15)
                self.starting_pos[3] = Rect(self.starting_pos[1].left-15, self.starting_pos[1].top+15,15,15)
                for pos in self.starting_pos:
                    if self.not_ok(pos, old_pos):
                        return
                self.state = 1
                return
