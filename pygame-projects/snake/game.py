import pygame
import random

from pygame.locals import *

class GameException(Exception):
    pass


class Settings(object):
    def __init__(self):
        self.resolution = ( 800, 600)
        self.background = (255, 228, 225)
        self.title = "Snake" 

class Game(object):

    def __init__(self, settings = Settings()):
        pygame.init()
        self.loadSettings(settings)
        self.clock = pygame.time.Clock()
        #self.gameObjects = [Snake(400,300, self.background)]
        #self.sprites = pygame.sprite.RenderPlain(self.gameObjects)

    def loadSettings(self, settings):
        self.screen = pygame.display.set_mode(settings.resolution)
        pygame.display.set_caption(settings.title)
        pygame.mouse.set_visible(False)

        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(settings.background)

    def run(self):
        isRunning = True
        while True:
            try:
                self.tick()
                if not isRunning:
                    return
            except GameException:
                return

    def tick(self):
        

