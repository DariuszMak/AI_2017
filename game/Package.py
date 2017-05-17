import pygame
import os
from .display_settings import *

class Package(pygame.sprite.Sprite):

    _nextId = 0

    def assertIfInvalidConfiguration(food, expiry):
        assert (food and expiry in ['short', 'medium', 'long']) or (not food and expiry in [None])


    def __init__(self, flammable, explosive, radioactive, medical, food, expiry):

        Package.assertIfInvalidConfiguration(food, expiry)

        pygame.sprite.Sprite.__init__(self)
        self._image= pygame.image.load(os.path.join('game','images','package.png'))

        self.id = Package._nextId
        Package._nextId += 1

        self.flammable = flammable
        self.explosive = explosive
        self.radioactive = radioactive
        self.medical = medical
        self.food = food
        self.expiry = expiry


    def _display(self, display, xpos, ypos):
        display.blit(self._image, (xpos * GRID_DISTANCE, ypos * GRID_DISTANCE))


    def getPackage(posx,posy, grid):
        try:
            return grid.grid[posx][posy]
        except IndexError:
            return None 
