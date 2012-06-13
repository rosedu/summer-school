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
        self.screen.blit(self.background, (0,0))
     #  self.allsprites.draw(self.screen)
        pygame.display.flip()
