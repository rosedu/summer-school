import pygame
import os
from pygame.locals import *

def load_image(name, colorkey = None, perpixel_alpha = False):
    """
    Loads an image and returns a surface
    """

    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message

    if perpixel_alpha:
        image = image.convert_alpha()
    else:
        image = image.convert()

    if colorkey != None and not perpixel_alpha:
        colorkey = image.get_at(colorkey)
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    return image
