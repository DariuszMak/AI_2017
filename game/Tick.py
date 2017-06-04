import pygame
from .display_settings import *


class TickBelowZeroTriedException(Exception):
    pass


class Tick(pygame.sprite.Sprite):
    def __init__(self, x, y, font):
        self.tick = TICK
        self.x = x
        self.y = y
        self.font = font
        self.shift = 25
        self.timeShift = 2

    def increase(self, ):
        self.tick += self.timeShift

    def decrease(self, ):
        if self.tick - self.timeShift <= 0:
            raise TickBelowZeroTriedException
        self.tick -= self.timeShift

    def _display(self, gameDisplay):
        FPSLabel = self.font.render("FPS: " + str(self.tick), 1, (0, 0, 0), )
        decreaseLabel = self.font.render("[ to decrease", 1, (0, 0, 0), )
        increaseLabel = self.font.render("] to increase", 1, (0, 0, 0), )

        gameDisplay.blit(FPSLabel, (self.x, self.y))
        gameDisplay.blit(decreaseLabel, (self.x, self.y + self.shift))
        gameDisplay.blit(increaseLabel, (self.x, self.y + 2 * self.shift))
        #  gameDisplay.blit(flammableLabel,(self.x,self.y + self.shift))
        #  gameDisplay.blit(explosiveLabel,(self.x,self.y+ 2*self.shift))
        #  gameDisplay.blit(radiocativeLabel,(self.x,self.y+ 3*self.shift))
        #  gameDisplay.blit(medicalLabel,(self.x,self.y+ 4*self.shift))
        #  gameDisplay.blit(FoodLabel,(self.x,self.y+ 5*self.shift))
        #  gameDisplay.blit(expiryDateLabel,(self.x,self.y+ 6*self.shift))
