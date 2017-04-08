import pygame
import os
from .display_settings import *
from .rot_center import rot_center

class Package(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(os.path.join('game','images','package.png'))

    def display(self, display, xpos, ypos):
        display.blit(self.image, (xpos * GRID_DISTANCE, ypos * GRID_DISTANCE))
