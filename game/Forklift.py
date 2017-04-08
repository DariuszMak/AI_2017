import pygame
import os
from .display_settings import *
from .rot_center import rot_center

class ForkliftOutOfGridError(Exception):
    pass

class Forklift(pygame.sprite.Sprite):

    toLeft = {  'up' : 'left',
                'left' : 'down',
                'down' : 'right',
                'right' : 'up'  }

    toRight = {  'up' : 'right',
                'right' : 'down',
                'down' : 'left',
                'left' : 'up'  }

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(os.path.join('game','images','forklift.png'))
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.direction = "up"

    def _isPositionCorrect(self, GRID_WIDTH, GRID_HEIGHT, x_shift, y_shift):
        if 0 <= self.x + x_shift <= GRID_WIDTH - 1 and 0 <= self.y + y_shift <= GRID_HEIGHT - 1 :
            return True
        else:
            return False

    def _changePosOrRaiseException(self, x_shift, y_shift):
        if not self._isPositionCorrect(GRID_WIDTH, GRID_HEIGHT, x_shift, y_shift):
            raise ForkliftOutOfGridError
        else:
            self.x += x_shift
            self.y += y_shift

    def moveForward(self,):
        if self.direction == 'up':
            self._changePosOrRaiseException(0, -1)
        elif self.direction == 'down':
            self._changePosOrRaiseException(0, 1)
        elif self.direction == 'left':
            self._changePosOrRaiseException(-1, 0)
        elif self.direction == 'right':
            self._changePosOrRaiseException(1, 0)

    def moveBackward(self,):
        if self.direction == 'up':
            self._changePosOrRaiseException(0, 1)
        elif self.direction == 'down':
            self._changePosOrRaiseException(0, -1)
        elif self.direction == 'left':
            self._changePosOrRaiseException(+1, 0)
        elif self.direction == 'right':
            self._changePosOrRaiseException(-1, 0)

    def turnRight(self,):
        self.direction = Forklift.toRight[self.direction]
        self.image = rot_center(self.image, 270)

    def turnLeft(self,):
        self.direction = Forklift.toLeft[self.direction]
        self.image = rot_center(self.image, 90)

    def display(self, display):
        self.rect.x = self.x * GRID_DISTANCE
        self.rect.y = self.y * GRID_DISTANCE
        display.blit(self.image, (self.rect.x, self.rect.y))
