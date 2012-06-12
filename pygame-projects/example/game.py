import pygame
import random

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
        self.resolution = (300, 300)
        # Backround color in Red Blue Green channels
        self.background = (0, 255, 0)
        # Mouse enabled
        self.mouse_enabled = True
        # Title
        self.title = "Sample Game"

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

    def update(self):
        """
        Updates graphical logic
        """
        if self.selected:
            self.x, self.y = pygame.mouse.get_pos()

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
                # Key Down events
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

