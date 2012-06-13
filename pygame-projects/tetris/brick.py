import pygame
import copy
import resources

BASE_FALL_RATE = 2
FALL_RATE_MULTIPLIER = 10

class Brick(pygame.sprite.Sprite):
    """
    Movable brick with arrows
    Return: brick object
    Methods: """
    def __init__(self, image, x, y, surface):
        ''' (x, y) = initialpos
            image = image from file'''
        super(Brick, self).__init__()
        self.surface = surface
        self.image = copy.copy(image)
        self.image.covert()

        screen = pygame.display.get_surface()
        self.rect = screen.get_rect()

        self.mode = 'falling or fading'
        self.falling = False
        self.fallrate = BASE_FALL_RATE
        
        self.x = x
        self.y = y
        self.rect.topleftt = (x, y)
        self.direction = 'none' # l, r, none

    def move(self, x, y):
        ''' moves the brick by the amount provided '''
        self.rect.topleft = (self.rect.topleft[0] + x,
                self.rect.topleft[1] + y)
    def coord(self):
        l = [x, y]
        return l

    def update(self):
        ''' TODO: fading '''
        if self.mode == 'falling':
            self.fallrate *= FALL_RATE_MULTIPLIER
            self.move(0, round(self.fallrate, 0))
            if self.rect.top >= self.fallto:
                self.rect.top = self.fallto
                self.mode = 'neither'
                self.falling = False
        
        if self.direction == 'l':
            moveleft(self)
        
        if self.direction == 'r':

    def moveleft(self):
        self.x = self.y - self.rect.width
            
    def moveright(self):
        self.x = self.x + self.rect.width

    def set_fall(self, distace):
        ''' the falling distance '''
        self.mode = 'falling'
        self.fallrate = BASE_FALL_RATE
        self.fallto = self.rect.top + distance
        self.falling = True

class Redbrick(Brick):
    def ___init__(self, x, y):
        Brick.__init__(self, resources.images.redbrick, x, y, surface)

class Greenbrick(Brick):
    def __init__(self, x, y):
        Brick.__init__(self, resources.images.greenbrick, x, y, surface)

class Bluebrick(Brick):
    def __init__(self, x, y):
        Brick.__init__(self, resources.images.bluebrick, x, y, surface)

