import pygame
import os
# import AI_2017
from commands.ForkliftCommand import forkliftCommand
from commands.Grid import Grid
from .Forklift import *
from .Package import Package
from .display_settings import *


def game_loop(gameDisplay, clock, grid, forklift):
    gameExit = False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    try:
                        forklift.turnLeft(grid)
                    except ForkliftTurningWithLoweredPackage:
                        pass
                if event.key == pygame.K_RIGHT:
                    try:
                        forklift.turnRight(grid)
                    except ForkliftTurningWithLoweredPackage:
                        pass
                if event.key == pygame.K_SPACE:
                    if forklift.carryingPackage:
                        forklift.lowerPackage(grid)
                    else:
                        forklift.liftPackage(grid)
                if event.key == pygame.K_UP:
                    try:
                        forklift.moveForward(grid)
                    except (ForkliftOutOfGridError, ForkliftPackageCollison):
                        pass
                if event.key == pygame.K_DOWN:
                    try:
                        forklift.moveBackward(grid)
                    except (ForkliftOutOfGridError, ForkliftPackageCollison):
                        pass

        forkliftCommand(forklift, grid)

        gameDisplay.fill(WHITE)


        for i in range(0, GAME_DISPLAY_WIDTH + GRID_DISTANCE, GRID_DISTANCE):
            pygame.draw.line(gameDisplay, BLACK, [i, 0], [i,GAME_DISPLAY_HEIGHT], 1)

        for i in range(0, GAME_DISPLAY_HEIGHT + GRID_DISTANCE, GRID_DISTANCE):
            pygame.draw.line(gameDisplay, BLACK, [0, i], [GAME_DISPLAY_WIDTH,i], 1)

        forklift.display(gameDisplay, grid)
        for i in range(len(grid.grid)):
            for j in range(len(grid.grid[0])):
                try:
                    if not (i == forklift.x and j == forklift.y):
                        grid.grid[i][j].display(gameDisplay, i, j)
                except AttributeError:
                    pass


        pygame.display.update()
        clock.tick(TICK)

def run():

    pygame.init()
    gameDisplay = pygame.display.set_mode((GAME_DISPLAY_WIDTH + MENU_WIDTH, GAME_DISPLAY_HEIGHT ))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()

    forklift = Forklift(6, 6)
    package = Package()
    grid = Grid(GAME_DISPLAY_WIDTH , GAME_DISPLAY_HEIGHT, GRID_DISTANCE)
    grid.grid[8][8] = package

    game_loop(gameDisplay, clock, grid, forklift)

    pygame.quit()
    quit()

run()
