import pygame
import random
import tetris

from background import *
from piece import *
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
    start_flag = 0
    start_rect = Rect(165, 180, 60, 30)
    reset_rect = Rect(245, 180, 60, 30)

    def __init__(self, settings = Settings()):
        pygame.init()
        self.init_from_settings(settings)
        self.clock = pygame.time.Clock()
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

        # Initializes background.
        background = pygame.Surface(self.screen.get_size())
        self.background = background.convert()
        self.background.fill(settings.background)

        pygame.display.update()

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

    p = Piece(randint(1, 10))
    next_piece = Piece(randint(1, 10))    

    def game_tick(self):
        """
        Handle events and redraw scene
        """
        self.clock.tick(60)
        
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
                    p.rotate()
				settings.rotate_sound.play()
                elif event.key == pygame.K_DOWN:
                    pass
                elif event.key == pygame.K_LEFT:
                    p.move_left(settings.grid)
				settings.move_sound.play()
                elif event.key == pygame.K_RIGHT:
                    p.move_right(settings.grid)
				settings.move_sound.play()
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
				if start_rect.collidepoint(event.pos):
					settings.click_sound.play()
					if start_flag == 1:
						start_flag = 0
						screen.set_clip(settings.game_info)
						screen.blit(settings.pause_text, (171, 188))
					else:
						start_flag = 1
						screen.set_clip(settings.game_info)
						screen.blit(settings.pause_text, (171, 188))
				if reset_rect.collidepoint(event.pos):
					settings.click_sound.play()
					start_flag = 0
					screen.set_clip(settings.game_area)
					screen.fill(colors[6])
					screen.set_clip(settings.game_info)
					screen.blit(settings.start_text, (171, 188))
					screen.display.update()
					settings.lines = 0
					settings.grid = []

        #Update all sprites
        self.allsprites.update()

        #Redraw.
        self.screen.blit(self.background, (0,0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()
