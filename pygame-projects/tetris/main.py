import pygame
import random
import tetris

from background import *
from brick import *
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
	   self.start_flag = 0
	   self.start_rect = Rect(165, 180, 60, 30)
	   self.reset_rect = Rect(245, 180, 60, 30)
        self.bricks = []
        self.allsprites = pygame.sprite.RenderPlain(self.bricks)

    def init_from_settings(self, settings):
        """
        Initializes game from Settings in tetris.py
        """

        # Initializes screen.
        self.screen = pygame.display.set_mode(settings.resolution)
	   self.screen.set_clip(settings.game_info)
	   self.screen.fill(settings.colors[5])
	   self.blit(settings.help_text1, (165, 250))
	   self.blit(settings.help_text2, (165, 270))
	   self.blit(settings.help_text3, (165, 290))
	   pygame.draw.rect(self.screen, settings.colors[6], start_rect, 0)
	   pygame.draw.rect(self.screen, settings.colors[6], reset_rect, 0)
	   pygame.draw.rect(self.screen, settings.colors[6], settings.box_display, 2)
	   screen.blit(settings.start_text, (171, 188))
	   screen.blit(settings.reset_text, (251, 188))
	   screen.set_clip(settings.game_area)
        pygame.display.set_caption(settings.title)
        pygame.mouse.set_visible(settings.mouse_enabled)
	   pygame.display.update()

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
            elif event.type == MOUSEBUTTONDOWN:
                self.random_spawn()

        #Update all sprites
        self.allsprites.update()

        #Redraw.
        self.screen.blit(self.background, (0,0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()
