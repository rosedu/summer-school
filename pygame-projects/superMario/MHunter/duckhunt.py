import pygame 
from pygame.locals import*
from sys import exit
from random import randint

pygame.init()

black = (0, 0, 0)
black = (255, 255, 255)

screen = pygame.display.set_mode((890, 550), 0, 32)
pygame.display.set_caption("Mihai Vanatorul")

# Duck position
x_duck = 0
y_duck = randint(0, 450)

# Mouse position
x_pos = 0
y_pos = 0

# Click position
x_click = 0
y_click = 0

points = 0
speed = 2
exit = False

ok = 0
while ok == 0:
    screen.fill(black)
    #pygame.mouse.set_visible(False)

    screen.blit(pygame.image.load("./res/bg1.jpg"), (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            ok = 1
    

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONDOWN:
            x_click, y_click = pygame.mouse.get_pos()

    position = (x_pos - 50 , y_pos - 50)
    x_duck += 1

    if x_duck * speed > 890 and not exit:
        x_duck = 0
        y_duck = randint(0, 450)

        exit = True

    # make screen black before adding objects
    screen.fill(black)
    pygame.mouse.set_visible(False)

    screen.blit(pygame.image.load("./res/background.jpg"), (0, 0))
    screen.blit(pygame.image.load("./res/score.gif"), (750, 10))
    screen.blit(pygame.font.SysFont("tahoma", 40).render(str(points), True, black), (800, 10))

    # target
    if x_click in range(x_duck * speed - 20, x_duck * speed + 20) and y_click in range(y_duck - 30, y_duck + 30):
        points += 1
	if points%2 == 0:
        	speed += 1
        x_duck = 0
        y_duck = randint(50, 500)

    # duck animation
    if x_duck%3 == 0 or x_duck%4 == 0 or x_duck%5 == 0:
        screen.blit(pygame.image.load("./res/greenduck2.gif"), (x_duck * speed, y_duck))
    else:
	screen.blit(pygame.image.load("./res/greenduck3.gif"), (x_duck * speed, y_duck))

    if exit:
        x_duck = -50
        y_duck = -50
        screen.blit(pygame.image.load("./res/dog.gif"), (400, 300))
	screen.blit(pygame.font.SysFont("arial", 60).render("LOOOSER!", True, (0, 255, 0)), (300, 200))

    # set crosshair
    screen.blit(pygame.image.load("./res/crosshair.gif").convert(), position)

    pygame.display.update()
