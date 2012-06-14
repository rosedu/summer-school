import pygame
import rungame  as rg
import dumbmenu as dm
pygame.init()

# Just a few static variables
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255

size = width, height = 340,240	
screen = pygame.display.set_mode(size)
screen.fill(blue)
pygame.display.update()
pygame.key.set_repeat(500,30)

choose = dm.dumbmenu(screen, [
                        'Start Game',
                        'Options',
                        'Manual',
                        'Show Highscore',
                        'Quit Game'], 64,64,None,32,1.4,green,red)

if choose == 0:
    rg.main()
    print "You choose 'Start Game'."
elif choose == 1:
    print "You choose 'Options'."
elif choose == 2:
    print "You choose 'Manual'."
elif choose == 3:
    print "You choose 'Show Highscore'."
elif choose == 4:
    print "You choose 'Quit Game'."
pygame.quit()
exit()
