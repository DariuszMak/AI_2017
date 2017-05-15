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

        self.flammable = False
        self.explosive = False
        self.radioactive = False
        self.medical = False
        self.expiry = None
        self.food = False

    def updateInfo(self, flammable, explosive, radioactive, medical, food, expiry):

        Package.assertIfInvalidConfiguration(food, expiry)

        self.flammable = flammable
        self.explosive = explosive
        self.radioactive = radioactive
        self.medical = medical
        self.food = food
        self.expiry = expiry

    def _display(self, display):

        infoLabel = self.font.render("PACKAGE INFO", 1, (0,0,0),) 
        flammableLabel = self.font.render("not implemented", 1, (0,0,0),) 
        explosiveLabel = self.font.render("not implemented", 1, (0,0,0),) 
        radiocativeLabel = self.font.render("not implemented", 1, (0,0,0),) 
        medicalLabel = self.font.render("not implemented", 1, (0,0,0),) 
        FoodLabel = self.font.render("not implemented", 1, (0,0,0),) 
        expiryDateLabel = self.font.render("not implemented", 1, (0,0,0),) 

        display.blit(infoLabel,(self.x,self.y))
        display.blit(flammableLabel,(self.x,self.y + self.shift))
        display.blit(explosiveLabel,(self.x,self.y+ 2*self.shift))
        display.blit(radiocativeLabel,(self.x,self.y+ 3*self.shift))
        display.blit(medicalLabel,(self.x,self.y+ 4*self.shift))
        display.blit(FoodLabel,(self.x,self.y+ 5*self.shift))
        display.blit(expiryDateLabel,(self.x,self.y+ 6*self.shift))
