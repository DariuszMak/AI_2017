import pygame
import os
from .display_settings import *
import game.Package

class PackageInfoBox(pygame.sprite.Sprite):

    def __init__(self, x, y, font):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.font = font
        self.shift = 25

        #  self.flammable = False
        #  self.explosive = False
        #  self.radioactive = False
        #  self.medical = False
        #  self.expiry = None
        #  self.food = False
        #

    def _display(self, package, info, gameDisplay):


        if type(package) == type(None):
            infoLabel = self.font.render(info, 1, (0,0,0),) 
            gameDisplay.blit(infoLabel,(self.x,self.y))
            return

        infoLabel = self.font.render(info, 1, (0,0,0),) 
        flammableLabel = self.font.render("flammable: " + str(package.flammable), 1, (0,0,0),) 
        explosiveLabel = self.font.render("explosive: " + str(package.explosive), 1, (0,0,0),) 
        radiocativeLabel = self.font.render("radioactive: " + str(package.radioactive), 1, (0,0,0),) 
        medicalLabel = self.font.render("medical: " + str(package.medical), 1, (0,0,0),) 
        FoodLabel = self.font.render("food: " + str(package.food), 1, (0,0,0),) 
        if package.food:
            expiryDateLabel = self.font.render("expiry: " + package.expiry, 1, (0,0,0),) 
        else:
            expiryDateLabel = self.font.render("expiry: " + "not apply",  1, (0,0,0),) 

        gameDisplay.blit(infoLabel,(self.x,self.y))
        gameDisplay.blit(flammableLabel,(self.x,self.y + self.shift))
        gameDisplay.blit(explosiveLabel,(self.x,self.y+ 2*self.shift))
        gameDisplay.blit(radiocativeLabel,(self.x,self.y+ 3*self.shift))
        gameDisplay.blit(medicalLabel,(self.x,self.y+ 4*self.shift))
        gameDisplay.blit(FoodLabel,(self.x,self.y+ 5*self.shift))
        gameDisplay.blit(expiryDateLabel,(self.x,self.y+ 6*self.shift))
