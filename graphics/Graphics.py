import pygame
import os
from . import Forklift
from .DisplaySettings import *


def game_loop(gameDisplay, clock, forklift):
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    forklift.moveLeft()
                if event.key == pygame.K_RIGHT:
                    forklift.moveRight()
                if event.key == pygame.K_UP:
                    forklift.moveDown()
                if event.key == pygame.K_DOWN:
                    forklift.moveUp()

        gameDisplay.fill(WHITE)

        for i in range(0, GAME_DISPLAY_WIDTH + GRID_DISTANCE, GRID_DISTANCE):
            pygame.draw.line(gameDisplay, BLACK, [i, 0], [i,GAME_DISPLAY_HEIGHT], 1)

        for i in range(0, GAME_DISPLAY_HEIGHT + GRID_DISTANCE, GRID_DISTANCE):
            pygame.draw.line(gameDisplay, BLACK, [0, i], [GAME_DISPLAY_WIDTH,i], 1)

        forklift.display(gameDisplay)

        pygame.display.update()
        clock.tick(TICK)



def run():

    pygame.init()
    gameDisplay = pygame.display.set_mode((GAME_DISPLAY_WIDTH + MENU_WIDTH, GAME_DISPLAY_HEIGHT ))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()

    forklift = Forklift.Forklift(0, 0)

    game_loop(gameDisplay, clock, forklift)

    pygame.quit()
    quit()

run()
