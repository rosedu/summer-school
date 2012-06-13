import pygame

from pygame.locals import *

class GameException(Exception):
    pass

class Settings(object):
    def __init__(self):
            self.resolution = (1000,1000)
            self.background = (48,121,4)
            self.title = "BOMBERMAN"

class Game(object):
    def __init__(self,settings = Settings()):
            pygame.init()
            self.init_from_settings(settings)
            self.clock = pygame.time.Clock()
            self.persons = [Person(75,55, self.background)]
            self.allsprites = pygame.sprite.RenderPlain(self.persons)

    def init_from_settings(self,settings):
            self.screen = pygame.display.set_mode(settings.resolution)
            pygame.display.set_caption(settings.title)
            background = pygame.Surface(self.screen.get_size())
            self.background = background.convert()
            self.background.fill(settings.background)

    def run(self):
        while True:
                try:
                        self.game_tick()
                except GameException:
                        return

    def game_tick(self):
        self.clock.tick(60)
        for event in pygame.event.get():
                if event.type == QUIT:
                       raise GameException
        for i in range(20):
            x = i * 50
            y = (i + 1) * 50
            pygame.draw.rect(self.background, pygame.color.Color("grey"),
                        (0, x, 50, y), 0)
            pygame.draw.rect(self.background, pygame.color.Color("black"),
                        (0, x, 50, y), 3)
            pygame.draw.rect(self.background, pygame.color.Color("grey"),
                        (x, 0, y, 50), 0)
            pygame.draw.rect(self.background, pygame.color.Color("black"),
                        (x, 0, y, 50), 3)
            pygame.draw.rect(self.background, pygame.color.Color("grey"),
                        (950, x, 1000, y), 0)
            pygame.draw.rect(self.background, pygame.color.Color("black"),
                        (950, x, 1000, y), 3)
            pygame.draw.rect(self.background, pygame.color.Color("grey"),
                        (x, 950, y, 1000), 0)
            pygame.draw.rect(self.background, pygame.color.Color("black"),
                        (x, 950, y, 1000), 3)
        
        self.allsprites.update()    
        self.screen.blit(self.background, (0,0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()
class Person(pygame.sprite.Sprite):
        SIZE = 20
        def __init__(self, x, y, surface):
                super(Person, self).__init__()
                self.x = x
                self.y = y
                self.surface = surface

                self.image = pygame.Surface((2 * Person.SIZE, 2 *
                        Person.SIZE), flags = SRCALPHA)
                self.image.convert()
                self.set_color("red")
                self.rect.midtop = (x, y)
        def set_color(self, color):
            radius = Person.SIZE
            self.rect = pygame.draw.circle(self.image, pygame.Color(color),
                        (radius, radius), radius)
        def update(self):
            self.rect.midtop = (self.x, self.y)
