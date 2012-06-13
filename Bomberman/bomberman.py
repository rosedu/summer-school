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
        self.screen.blit(self.background, (0,0))
     #  self.allsprites.draw(self.screen)
        pygame.display.flip()

