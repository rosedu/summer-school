import pygame
import random
import tetris
from background import Settings

from pygame.locals import *

class GameException(Exception):
    """
    Useful for exiting
    """
    pass

class Game(object):
    """
    Main class
    """
    
    def __init__(self, settings = Settings()):
        pygame.init()
        self.init_from_settings(settings)
        self.clock = pygame.time.Clock()

    def init_from_settings(self, settings):
        """
        Initializes game from Settings in tetris.py
        """

        # Initializes screen.
        self.screen = pygame.display.set_mode(settings.resolution)
        pygame.display.set_caption(settings.title)
        pygame.mouse.set_visible(settings.mouse_enabled)

        # Initializes background.
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(settings.background)

    def run(self):
        """
        Runs the game
        """

        while(True):
            try:
                self.game_tick()
            except GameException:
                return
    
    def random_spawn(self):
        w, h = self.screen.get_size()
        x = random.randint(0, w)
        y = random.randint(0, h)
        self.bricks.append(Bluebrick(x, y, self.background))

        #Add new persons to rendered group
        self.allsprites = pygame.sprite.RenderPlain(self.bricks)
    
    def game_tick(self):
        """
        Handle events and redraw scene
        """
        self.clock.tick(60)
        
        #Check events.
        for event in pygame.event.get():
            if event.type == QUIT:
                raise GameException
            elif event.type == KEYDOWN:
                #Keyboard events
                if event.key == pygame.K_UP:
                    continue
                elif event.key == pygame.K_DOWN:
                    continue
                elif event.key == pygame.K_LEFT:
                    continue
                elif event.key == pygame.K_RIGHT:
                    continue

        #Update all sprites
        self.allsprites.update()

        #Redraw.
        self.screen.blit(self.background, (0,0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()
