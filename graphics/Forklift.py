import pygame
import os
from DisplaySettings import *


class Forklift(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image= pygame.image.load(os.path.join('images','forklift.png'))
        self.rect = self.image.get_rect()

        self.x, self.y = x, y


    def moveRight(self,):
        self.x += 1

    def moveLeft(self,):
        self.x -= 1

    def moveUp(self,):
        self.y += 1

    def moveDown(self,):
        self.y -= 1

    def display(self, display):
        self.rect.x = self.x * GRID_DISTANCE
        self.rect.y = self.y * GRID_DISTANCE
        display.blit(self.image, (self.rect.x, self.rect.y))
