#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys

# **********************************************************************
# Function "dumbmenu" **************************************************
# **********************************************************************
def dumbmenu(screen, menu, x_pos = 100, y_pos = 100, font = None,
            size = 70, distance = 1.4, fgcolor = (255,255,255),
            cursorcolor = (255,0,0), exitAllowed = True):
	"""Draws a Menu using pygame.
	
	Parameters are: screen, menu, x_pos, y_pos, font,
	                size, distance, fgcolor, cursor
	                
	PARAMETERS
	==========
	screen (Surface): The surface created with pygame.display.set_mode()
	                
	menu (List):      A List of every menupoint that should be visible
	
	x_pos (digit):   Start of x_position, in Pixels (Default: 100)
	
	y_pos (digit):   Start of y_position, in Pixels (Default: 100)
	
	size (digit):    Fontsize (Default: 70)
	
	distance (float):Y-Distance after every single menupoint
	                 (Default: 1.4)
	
	fgcolor (Tupel): Foreground-Color, means the Font-Color
	                 (Default: (255,255,255), means white)
	                 
	cursorcolor (Tupel): Cursor-Color, means that ">"-Charakter
	                     (Default: (255,0,0), means red)
	                     
	exitAllowed (Bool): If True:
	                    If User pressed the ESC-Key, the Cursor will
	                    move to the last Menupoint. If Cursorposition
	                    is already to the last Menupoint, a pressed
	                    ESC-Key will return the latest Menupoint. Very
	                    useful if the last Menupoint is something like
	                    "Quit Game"...
	                    If False:
	                    A pressed ESC-Key will takes no effect.
	                    (Default: True)
	                    
	EXAMPLE
	=======
	import pygame
	from dumbmenu import *
	pygame.init()

	# Just a few static variables
	red   = 255,  0,  0
	green =   0,255,  0

	size = width, height = 640,480	
	screen = pygame.display.set_mode(size)
	screen.fill(blue)
	pygame.display.update()

	print dumbmenu(screen, [
	                        'Start Game',
	                        'Options',
	                        'Manual',
	                        'Show Highscore',
	                        'Quit Game'],
	                        320, 250, "Courier", 32, 1.4, green, red)
	
	HOW TO INTERACT
	===============
	After called dumbmenu(), the User MUST choose an Menupoint. The
	Script will be haltet until the User makes a decision or a event
	called pygame.QUIT() will be raised.
	
	The User kann pressed directly a Key from 1 to 9 to take the choice.
	Another Method is pressing the UP-/DOWN-Key and take the choice with
	RETURN. Every single Menupoint will get a Number, beginning with 1.
	
	The return-value ist the Number of Menupoint decreased by 1. From
	the above Example: If the User will choice "Manual", the return-
	value will be 2.

	If the number of Menupoints is greater than 9, the numeration will
	continue from A to Z... the return-value is still a number,
	continue from 9 to 34...
	
	If a pygame.QUIT()-Event will be raised, the return-value will be
	-1.
	
	ACTUAL LIMITATIONS
	==================
	It's actually not possible to change the Font itself.
	
	Drawing Menu will be antialiased. If you want to change that, you'll
	have to change the sourcecode directly.

	OTHERS
	======
	Yes, I know, my english isn't that good (I'm not a naturally
	speaker) and the sourcecode isn't that good too ;) . It's more or
	less a "quick'n dirty"-Solution. My first intention was to make that
	code for me, but I hope it could may useful for other people too...

	Version: 0.40
	Author: Manuel Kammermeier aka Astorek
	License: MIT

	CHANGES:
	========
	Version 0.35:
	- First Version
	
	Version 0.40:
	- "bgcolor" removed, now the Function saves the Background
	- added "font", which allows to choose a Systemfont
	"""


	# Draw the Menupoints
	pygame.font.init()
	if font == None:
		myfont = pygame.font.Font(None, size)
	else:
		myfont = pygame.font.SysFont(font, size)
	cursorpos = 0
	renderWithChars = False
	for i in menu:
		if renderWithChars == False:
			text =  myfont.render(str(cursorpos + 1)+".  " + i,
				True, fgcolor)
		else:
			text =  myfont.render(chr(char)+".  " + i,
				True, fgcolor)
			char += 1
		textrect = text.get_rect()
		textrect = textrect.move(x_pos, 
		           (size // distance * cursorpos) + y_pos)
		screen.blit(text, textrect)
		pygame.display.update(textrect)
		cursorpos += 1
		if cursorpos == 9:
			renderWithChars = True
			char = 65

	# Draw the ">", the Cursor
	cursorpos = 0
	cursor = myfont.render(">", True, cursorcolor)
	cursorrect = cursor.get_rect()
	cursorrect = cursorrect.move(x_pos - (size // distance),
	             (size // distance * cursorpos) + y_pos)

	# The whole While-loop takes care to show the Cursor, move the
	# Cursor and getting the Keys (1-9 and A-Z) to work...
	ArrowPressed = True
	exitMenu = False
	clock = pygame.time.Clock()
	filler = pygame.Surface.copy(screen)
	fillerrect = filler.get_rect()
	while True:
		clock.tick(30)
		if ArrowPressed == True:
			screen.blit(filler, fillerrect)
			pygame.display.update(cursorrect)
			cursorrect = cursor.get_rect()
			cursorrect = cursorrect.move(x_pos - (size // distance),
			             (size // distance * cursorpos) + y_pos)
			screen.blit(cursor, cursorrect)
			pygame.display.update(cursorrect)
			ArrowPressed = False
		if exitMenu == True:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return -1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE and exitAllowed == True:
					if cursorpos == len(menu) - 1:
						exitMenu = True
					else:
						cursorpos = len(menu) - 1; ArrowPressed = True


				# This Section is huge and ugly, I know... But I don't
				# know a better method for this^^
				if event.key == pygame.K_1:
					cursorpos = 0; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_2 and len(menu) >= 2:
					cursorpos = 1; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_3 and len(menu) >= 3:
					cursorpos = 2; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_4 and len(menu) >= 4:
					cursorpos = 3; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_5 and len(menu) >= 5:
					cursorpos = 4; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_6 and len(menu) >= 6:
					cursorpos = 5; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_7 and len(menu) >= 7:
					cursorpos = 6; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_8 and len(menu) >= 8:
					cursorpos = 7; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_9 and len(menu) >= 9:
					cursorpos = 8; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_a and len(menu) >= 10:
					cursorpos = 9; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_b and len(menu) >= 11:
					cursorpos = 10; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_c and len(menu) >= 12:
					cursorpos = 11; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_d and len(menu) >= 13:
					cursorpos = 12; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_e and len(menu) >= 14:
					cursorpos = 13; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_f and len(menu) >= 15:
					cursorpos = 14; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_g and len(menu) >= 16:
					cursorpos = 15; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_h and len(menu) >= 17:
					cursorpos = 16; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_i and len(menu) >= 18:
					cursorpos = 17; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_j and len(menu) >= 19:
					cursorpos = 18; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_k and len(menu) >= 20:
					cursorpos = 19; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_l and len(menu) >= 21:
					cursorpos = 20; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_m and len(menu) >= 22:
					cursorpos = 21; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_n and len(menu) >= 23:
					cursorpos = 22; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_o and len(menu) >= 24:
					cursorpos = 23; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_p and len(menu) >= 25:
					cursorpos = 24; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_q and len(menu) >= 26:
					cursorpos = 25; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_r and len(menu) >= 27:
					cursorpos = 26; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_s and len(menu) >= 28:
					cursorpos = 27; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_t and len(menu) >= 29:
					cursorpos = 28; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_u and len(menu) >= 30:
					cursorpos = 29; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_v and len(menu) >= 31:
					cursorpos = 30; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_w and len(menu) >= 32:
					cursorpos = 31; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_x and len(menu) >= 33:
					cursorpos = 32; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_y and len(menu) >= 34:
					cursorpos = 33; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_z and len(menu) >= 35:
					cursorpos = 34; ArrowPressed = True; exitMenu = True
				elif event.key == pygame.K_UP:
					ArrowPressed = True
					if cursorpos == 0:
						cursorpos = len(menu) - 1
					else:
						cursorpos -= 1
				elif event.key == pygame.K_DOWN:
					ArrowPressed = True
					if cursorpos == len(menu) - 1:
						cursorpos = 0
					else:
						cursorpos += 1
				elif event.key == pygame.K_KP_ENTER or \
				     event.key == pygame.K_RETURN:
							exitMenu = True
	
	return cursorpos

if __name__ == '__main__':
	sys.stderr.write("You should import me, not start me...")
	sys.exit()
