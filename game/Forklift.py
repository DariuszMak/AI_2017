import pygame
import os
from .display_settings import *
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

        self.x, self.y = x, y
        self.direction = "up"
        self.carryingPackage = None

        pygame.sprite.Sprite.__init__(self)

        self._imageWithNoPackageUP = pygame.image.load(os.path.join('game','images','forklift-with-no-package-UP.png'))
        self._imageWithNoPackageRIGHT = pygame.image.load(os.path.join('game','images','forklift-with-no-package-RIGHT.png'))
        self._imageWithNoPackageDOWN = pygame.image.load(os.path.join('game','images','forklift-with-no-package-DOWN.png'))
        self._imageWithNoPackageLEFT = pygame.image.load(os.path.join('game','images','forklift-with-no-package-LEFT.png'))

        self._imageWithPackageLowUP = pygame.image.load(os.path.join('game','images','forklift-with-package-low-pos-UP.png'))
        self._imageWithPackageLowRIGHT = pygame.image.load(os.path.join('game','images','forklift-with-package-low-pos-RIGHT.png'))
        self._imageWithPackageLowDOWN = pygame.image.load(os.path.join('game','images','forklift-with-package-low-pos-DOWN.png'))
        self._imageWithPackageLowLEFT = pygame.image.load(os.path.join('game','images','forklift-with-package-low-pos-LEFT.png'))

        self._imageWithPackageHighUP = pygame.image.load(os.path.join('game','images','forklift-with-package-high-pos-UP.png'))
        self._imageWithPackageHighRIGHT = pygame.image.load(os.path.join('game','images','forklift-with-package-high-pos-RIGHT.png'))
        self._imageWithPackageHighDOWN = pygame.image.load(os.path.join('game','images','forklift-with-package-high-pos-DOWN.png'))
        self._imageWithPackageHighLEFT = pygame.image.load(os.path.join('game','images','forklift-with-package-high-pos-LEFT.png'))

        self._image= self._imageWithNoPackageUP
        self._rect = self._imageWithPackageHighLEFT.get_rect()


    def _isPositionOutOfGrid(self, GRID_WIDTH, GRID_HEIGHT, x_shift, y_shift):
        if 0 <= self.x + x_shift <= GRID_WIDTH - 1 and 0 <= self.y + y_shift <= GRID_HEIGHT - 1 :
            return False
        else:
            return True


    def getPossibleActions(x, y, direction, carryingPackage, grid):
        actions = list()
        
        if not carryingPackage and grid.grid[x][y]:
            actions.append('liftPackage')
        if carryingPackage:
            actions.append('lowerPackage')
        if type(grid.grid[x][y]) == type(None):
            actions.append('toLeft')
            actions.append('toRight')

        
        #  if self._isPositionOutOfGrid(GRID_WIDTH, GRID_HEIGHT, x_shift, y_shift):
        #      raise ForkliftOutOfGridError
        #  if self.carryingPackage and grid.grid[self.x + x_shift][self.y + y_shift]:
        #      raise ForkliftMovingOnPackagePosAlreadyCarryingPackage
        #  if self._isOnPackagePosition(grid) and isMoveForward:
        #      raise ForkliftMovedForwardWithPackageOnLoweredFork
        #  if grid.grid[self.x + x_shift][self.y + y_shift] and not isMoveForward:
        #      raise ForkliftMovedBackwardIntoPackage


        return actions
            


    def _isOnPackagePosition(self, grid):
        if type(grid.grid[self.x][self.y]) == type(None):
            return False
        else:
            return True

    def _changePosOrRaiseException(self, grid, isMoveForward, x_shift, y_shift):
        self._isPossibleToChangePos(grid, isMoveForward, x_shift, y_shift) # raises Exceptions
        self.x += x_shift
        self.y += y_shift

    def _isPossibleToChangePos(self, grid, isMoveForward, x_shift, y_shift):
        if self._isPositionOutOfGrid(GRID_WIDTH, GRID_HEIGHT, x_shift, y_shift):
            raise ForkliftOutOfGridError
        if self.carryingPackage and grid.grid[self.x + x_shift][self.y + y_shift]:
            raise ForkliftMovingOnPackagePosAlreadyCarryingPackage
        if self._isOnPackagePosition(grid) and isMoveForward:
            raise ForkliftMovedForwardWithPackageOnLoweredFork
        if grid.grid[self.x + x_shift][self.y + y_shift] and not isMoveForward:
            raise ForkliftMovedBackwardIntoPackage
        return True

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


    def _display(self, display, grid):
        self._rect.x = self.x * GRID_DISTANCE
        self._rect.y = self.y * GRID_DISTANCE

        if self.carryingPackage:
            if self.direction == 'up':
                image = self._imageWithPackageHighUP
            elif self.direction == 'right':
                image = self._imageWithPackageHighRIGHT
            elif self.direction == 'down':
                image = self._imageWithPackageHighDOWN
            elif self.direction == 'left':
                image = self._imageWithPackageHighLEFT
        elif self._isOnPackagePosition(grid):
            if self.direction == 'up':
                image = self._imageWithPackageLowUP
            elif self.direction == 'right':
                image = self._imageWithPackageLowRIGHT
            elif self.direction == 'down':
                image = self._imageWithPackageLowDOWN
            elif self.direction == 'left':
                image = self._imageWithPackageLowLEFT
        else:
            if self.direction == 'up':
                image = self._imageWithNoPackageUP
            elif self.direction == 'right':
                image = self._imageWithNoPackageRIGHT
            elif self.direction == 'down':
                image = self._imageWithNoPackageDOWN
            elif self.direction == 'left':
                image = self._imageWithNoPackageLEFT

        display.blit(image, (self._rect.x, self._rect.y))
