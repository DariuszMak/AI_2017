import pygame
import os
from .display_settings import *
from .rot_center import rot_center
from .ForkliftExceptions import *

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
        self.imageWithNoPackage = pygame.image.load(os.path.join('game','images','forklift.png'))
        self.imageWithPackageLow = pygame.image.load(os.path.join('game','images','forklift-with-package-low-pos.png'))
        self.imageWithPackageHigh = pygame.image.load(os.path.join('game','images','forklift-with-package-high-pos.png'))
        self.image= self.imageWithNoPackage
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.direction = "up"
        self.carryingPackage = None

    def _isPositionOutOfGrid(self, GRID_WIDTH, GRID_HEIGHT, x_shift, y_shift):
        if 0 <= self.x + x_shift <= GRID_WIDTH - 1 and 0 <= self.y + y_shift <= GRID_HEIGHT - 1 :
            return False
        else:
            return True

    def _isOnPackagePosition(self, grid):
        if type(grid.grid[self.x][self.y]) == type(None):
            return False
        else:
            return True

    def _changePosOrRaiseException(self, grid, isMoveForward, x_shift, y_shift):
        if self._isPositionOutOfGrid(GRID_WIDTH, GRID_HEIGHT, x_shift, y_shift):
            raise ForkliftOutOfGridError
        if self.carryingPackage and grid.grid[self.x + x_shift][self.y + y_shift]:
            raise ForkliftMovingOnPackagePosAlreadyCarryingPackage
        if self._isOnPackagePosition(grid) and isMoveForward:
            raise ForkliftMovedForwardWithPackageOnLoweredFork
        if grid.grid[self.x + x_shift][self.y + y_shift] and not isMoveForward:
            raise ForkliftMovedBackwardIntoPackage
        self.x += x_shift
        self.y += y_shift

    def liftPackage(self, grid):
        if self.carryingPackage:
            raise ForkliftAlreadyCarryingPackage
        if not grid.grid[self.x][self.y]:
            raise ForkliftNotOnPackagePosition
        else:
            self.carryingPackage = grid.grid[self.x][self.y]
            grid.grid[self.x][self.y] = None


    def lowerPackage(self, grid):
        if not self.carryingPackage:
            raise ForkliftNotCarryingPackage
        else:
            grid.grid[self.x][self.y] = self.carryingPackage
            self.carryingPackage = None


    def moveForward(self, grid):
        if self.direction == 'up':
            self._changePosOrRaiseException(grid, True, 0, -1)
        elif self.direction == 'down':
            self._changePosOrRaiseException(grid, True,  0, 1)
        elif self.direction == 'left':
            self._changePosOrRaiseException(grid, True, -1, 0)
        elif self.direction == 'right':
            self._changePosOrRaiseException(grid, True, 1, 0)

    def moveBackward(self, grid):
        if self.direction == 'up':
            self._changePosOrRaiseException(grid, False, 0, 1)
        elif self.direction == 'down':
            self._changePosOrRaiseException(grid, False, 0, -1)
        elif self.direction == 'left':
            self._changePosOrRaiseException(grid, False, 1, 0)
        elif self.direction == 'right':
            self._changePosOrRaiseException(grid, False, -1, 0)

    def turnRight(self, grid):
        if self._isOnPackagePosition(grid):
            raise ForkliftTurningWithLoweredPackage
        self.direction = Forklift.toRight[self.direction]

    def turnLeft(self, grid):
        if self._isOnPackagePosition(grid):
            raise ForkliftTurningWithLoweredPackage
        self.direction = Forklift.toLeft[self.direction]

    def display(self, display, grid):
        self.rect.x = self.x * GRID_DISTANCE
        self.rect.y = self.y * GRID_DISTANCE

        if self.carryingPackage:
            image = self.imageWithPackageHigh
        elif self._isOnPackagePosition(grid):
            image = self.imageWithPackageLow
        else:
            image = self.imageWithNoPackage


        if self.direction == 'left':
            image = rot_center(image, 90)
        elif self.direction == 'right':
            image = rot_center(image, 270)
        elif self.direction == 'down':
            image = rot_center(image, 180)

        display.blit(image, (self.rect.x, self.rect.y))
