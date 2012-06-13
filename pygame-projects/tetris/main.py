import pygame
import random
import tetris

from random import *
from background import *
from piece import *
from pygame.locals import *

#Constants
start_rect = Rect(165,180,60,30)
reset_rect = Rect(245,180,60,30)
start_flag = 0

#Class definitions
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
        self.start_flag = 0
        #self.bricks = []
        #self.allsprites = pygame.sprite.RenderPlain(self.bricks)

    def init_from_settings(self, settings):
        """
        Initializes game from Settings in tetris.py
        """

        # Initializes screen.
        self.screen = pygame.display.set_mode(settings.resolution)
        self.screen.set_clip(settings.game_info)
        self.screen.fill(settings.colors[5])
        
        self.screen.blit(settings.help_text1, (165, 250))
        self.screen.blit(settings.help_text2, (165, 270))
        self.screen.blit(settings.help_text3, (165, 290))
        
        pygame.draw.rect(self.screen, settings.colors[6], start_rect, 0)
        pygame.draw.rect(self.screen, settings.colors[6], reset_rect, 0)
        pygame.draw.rect(self.screen, settings.colors[6], settings.box_display, 2)
        
        self.screen.blit(settings.start_text, (171, 188))
        self.screen.blit(settings.reset_text, (251, 188))
        
        self.screen.set_clip(settings.game_area)
        
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

    p = Piece(randint(1, 10))
    next_piece = Piece(randint(1, 10))    
	
    def game_tick(self):
        """
        Handle events and redraw scene
        """
        self.clock.tick(60)
        
        settings = Settings()
        
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
					if self.start_flag == 1:
						self.start_flag = 0
						self.screen.set_clip(settings.game_info)
						self.screen.blit(settings.pause_text, (171, 188))
					else:
						self.start_flag = 1
						self.screen.set_clip(settings.game_info)
						self.screen.blit(settings.pause_text, (171, 188))
				 if reset_rect.collidepoint(event.pos):
					settings.click_sound.play()
					self.start_flag = 0
					self.screen.set_clip(settings.game_area)
					self.screen.fill(colors[6])
					self.screen.set_clip(settings.game_info)
					self.screen.blit(settings.start_text, (171, 188))
					self.screen.display.update()
					settings.lines = 0
					settings.grid = []

		# New brick falling		
		time_passed = pygame.time.get_ticks()
		if (p.going_down):
			screen.set_clip(187, 67, 97, 67)
			screen.fill(colors[5])
			for pos in next_piece.display_pos:
				screen.blit(next_piece.image, pos)
			p.update(time_passed, grid, speed)
			screen.set_clip(settings.game_area)
			screen.fill(colors[5])
			for pos in p.starting_pos:
				screen.blit(p.image, pos)
		else:
			grid.append(p)
			for pos in p.starting_pos:
				bricks[pos.top] += 1
			game(grid, bricks)
			p = next_piece
			#	next_piece = Piece(randint(1, 10))
			for g in grid:
				for pos in g.starting_pos:
					if pos.left == 65 and pos.top <= 5:
						start_flag = 0
						screen.blit(settings.game_over, (30, 50))
						pygame.display.update()
		update()

        #Update all sprites
        #self.allsprites.update()

        #Redraw.
        self.screen.blit(self.background, (0,0))
        #self.allsprites.draw(self.screen)
        pygame.display.flip()
