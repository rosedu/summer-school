import pygame
import copy
import resources

BASE_FALL_RATE = 2
FALL_RATE_MULTIPLIER = 10

current_id = 0

class Brick(pygame.sprite.Sprite):
    """
    Movable brick with arrows
    Return: brick object
    Methods: """

    SIZE = 10

    def __init__(self, x, y, surface):
        ''' (x, y) = initialpos
            image = image from file'''
        super(Brick, self).__init__()
        self.x = x
        self.y = y
        self.surface = surface

        #Old version, with image
        #self.image = copy.copy(image)
        #self.image.covert()
        self.image = pygame.Surface((Brick.SIZE, Brick.SIZE), flags = SRCALPHA)
        self.image.convert()

        self.ID = current_id
        current_id += 1

        #screen = pygame.display.get_surface()
        #self.rect = screen.get_rect()
        #default direction is down
        self.direction = 'd' # 'l', 'r', 'd'
      
        self.mode = 'falling or fading'
        self.falling = False
        self.fallrate = BASE_FALL_RATE
        
        self.put_shape("red", x, y)

        self.rect.topleft = (x, y)
   
    def put_shape(self, color, x, y):
        """
        Sets the brick's color
        """
        w = Brick.SIZE
        self.rect = pygame.draw.rect(self.image, pygame.Color(color), (x, y, w, w), w) 
    
    def coord(self):
        return (self.x, self.y)

    def update(self):
        ''' TODO: fading '''
        if self.mode == 'falling':
            self.fallrate *= FALL_RATE_MULTIPLIER
            if self.rect.top >= self.fallto:
                self.rect.top = self.fallto
                self.mode = 'neither'
                self.falling = False
        
        if self.direction == 'l':
            self.moveleft()
        
        if self.direction == 'r':
            self.moveright()

    def moveleft(self):
        if isMoveableX(self.x, self.x - self.rect.width):
            self.x = self.x - self.rect.width
            
    def moveright(self):
        if isMoveable(self.x, self.x + self.rect.width):
            self.x = self.x + self.rect.width
    
    def isMoveableX(self, endX):
        if endX > 0 && endX < 500:
            return True
        return False     

    def set_fall(self, distace):
        ''' the falling distance '''
        self.mode = 'falling'
        self.fallrate = BASE_FALL_RATE
        self.fallto = self.rect.top + distance
        self.falling = True
