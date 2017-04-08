import pygame
import os
from .display_settings import *

class Package(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._image= pygame.image.load(os.path.join('game','images','package.png'))

    def _display(self, display, xpos, ypos):
        display.blit(self._image, (xpos * GRID_DISTANCE, ypos * GRID_DISTANCE))
