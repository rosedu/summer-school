import pygame
import random

directions  = { "start": (0, 0), "left": (-1, 0), "right": (1, 0), "down": (0, -1), "up": (0, 1) }

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
        self.resolution = (500, 500)
        # Backround color in Red Blue Green channels
        self.background = (0, 0, 0)
        # Mouse enabled
        self.mouse_enabled = True
        # Title
        self.title = "PacMan"


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
        self.set_color("red")

        self.rect.midtop = (x, y)

    def set_color(self, color):
        """
        Sets person's color
        """
        radius = Person.SIZE
        self.rect = pygame.draw.circle(self.image, pygame.Color(color), (radius, radius), radius)

    def select(self):
        """
        Selects person
        """
        self.set_color("blue")
        self.selected = True

    def deselect(self):
        """
        Deselects person
        """
        self.set_color("red")
        self.selected = False

    def toggle_select(self):
        """
        Toggles selectation of person
        """
        if self.selected:
            self.deselect()
        else:
            self.select()

    def move(self, next_move):
        """
        Compute the next move
        """
        self.new_x, self.new_x = next_move
    
    def update(self):
        """
        Updates graphical logic
        """
               
        self.x = self.new_x
        self.y = self.new_y

        self.rect.midtop = (self.x, self.y)

    def clicked(self, pos):
        """
        Logic if object is clicked
        """

        # Get absolute position.
        abs_rect = self.rect.move(self.image.get_abs_offset())
        if abs_rect.contains(pos, (1, 1)):
            return True
        return False

class Game(object):
    """
    PyGame sample game class
    """

    def __init__(self, settings = Settings()):
        pygame.init()
        self.init_from_settings(settings)
        self.clock = pygame.time.Clock()
        self.persons = [Person(10, 10, self.background)]
        self.selected = None

        # Render Group
        self.allsprites = pygame.sprite.RenderPlain(self.persons)

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

        #Init table
        table = Background(settings.resolution)

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
        self.clock.tick(60)

        # Check events.
        for event in pygame.event.get():
            if event.type == QUIT:
                raise GameException
            elif event.type == KEYDOWN:
                continue
            elif event.type == KEYUP:
                if event.key == K_DOWN:
                    direction = directions['down']
                    if table.isValid((pacman.x, pacman.y), direction):
                        x, y = table.getActualXY((pacman.x, pacman.y), direction)
                        person.move((x, y))
                    print direction
                elif event.key == K_UP:
                    direction = directions["up"]
                    print direction
                elif event.key == K_LEFT:
                    direction = directions["left"]
                    print direction
                elif event.key == K_RIGHT:
                    direction = directions["right"]
                    print direction
                continue
            elif event.type == MOUSEBUTTONUP:
                # Check if selection
                if self.selected is not None and event.button == 1:
                    self.selected.deselect()
                    self.selected = None
                elif event.button == 3:
                    self.spawn_random_person()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    for person in self.persons:
                        if person.clicked(event.pos):
                            person.select()
                            self.selected = person

        # Update all sprites.
        # Calls update method for the sprites defined.

        self.allsprites.update()

        # Redraw.
        self.screen.blit(self.background, (0, 0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()

