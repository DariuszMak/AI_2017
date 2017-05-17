import pygame
import os
from commands.ForkliftCommand import *
from commands.Grid import Grid
from .Forklift import Forklift
from .ForkliftExceptions import *
from .Package import Package
from .PackageInfoBox import PackageInfoBox
from .display_settings import *


def game_loop(gameDisplay, clock, grid, forklift, font, packageInfoBox):
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
                    try:
                        if forklift.carryingPackage:
                            forklift.lowerPackage(grid)
                        else:
                            forklift.liftPackage(grid)
                    except (ForkliftNotCarryingPackage, ForkliftNotOnPackagePosition):
                        pass
                if event.key == pygame.K_UP:
                    try:
                        forklift.moveForward(grid)
                    except (ForkliftOutOfGridError,
                            ForkliftMovedForwardWithPackageOnLoweredFork,
                            ForkliftMovingOnPackagePosAlreadyCarryingPackage):
                        pass
                if event.key == pygame.K_DOWN:
                    try:
                        forklift.moveBackward(grid)
                    except (ForkliftOutOfGridError,
                            ForkliftMovingOnPackagePosAlreadyCarryingPackage,
                            ForkliftMovedBackwardIntoPackage):
                        pass

        gameDisplay.fill(WHITE)
        forkliftCommand(forklift, grid)

        for i in range(0, GAME_DISPLAY_WIDTH + GRID_DISTANCE, GRID_DISTANCE):
            pygame.draw.line(gameDisplay, BLACK, [i, 0], [
                             i, GAME_DISPLAY_HEIGHT], 1)

        for i in range(0, GAME_DISPLAY_HEIGHT + GRID_DISTANCE, GRID_DISTANCE):
            pygame.draw.line(gameDisplay, BLACK, [0, i], [
                             GAME_DISPLAY_WIDTH, i], 1)

        forklift._display(gameDisplay, grid)

        for i in range(len(grid.grid)):
            for j in range(len(grid.grid[0])):
                try:
                    if not (i == forklift.x and j == forklift.y):
                        grid.grid[i][j]._display(gameDisplay, i, j)
                except AttributeError:
                    pass
        
        label = font.render("Some text!", 1, (255,255,0))
        packageInfoBox._display(gameDisplay)
        pygame.display.update()
        clock.tick(TICK)


def run():

    pygame.init()
    font = pygame.font.SysFont("monospace", 15)
    font=pygame.font.Font(None,30)

    gameDisplay = pygame.display.set_mode(
        (GAME_DISPLAY_WIDTH + MENU_WIDTH, GAME_DISPLAY_HEIGHT))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()

    forklift = Forklift(6, 6)
    packageInfoBox = PackageInfoBox(810, 400, font)
    grid = Grid(GAME_DISPLAY_WIDTH, GAME_DISPLAY_HEIGHT, GRID_DISTANCE)
    grid.grid[8][8] = Package(False, False, False, False, True, 'short')
    grid.grid[2][5] = Package(False, False, False, True, False, None)
    grid.grid[2][2] = Package(True, False, False, False, False, None)
    grid.grid[2][9] = Package(True, True, False, False, False, None)
    grid.grid[3][1] = Package(False, False, True, False, False, None)
    grid.grid[7][7] = Package(False, False, False, False, False, None)
    grid.grid[0][0] = Package(False, False, True, False, False, None)

    addNewMove(None, (2, 1))
    addNewMove(None, (15, 8))
    addNewMove(grid.grid[0][0], (14, 13))
    addNewMove(None, (0, 0))

    if len(objectList) != 0:
        print('There is something')
        print(objectList)
        coordinateList.append(getAstarPath(grid, (forklift.x, forklift.y), objectList[0][1]))



        print(coordinateList)

        for step in range(len(coordinateList[0]) - 1):
            first = coordinateList[0][step]
            second = coordinateList[0][step + 1]
            print(coordinateList[0][step], coordinateList[0][step + 1])
            if(first[0] == second[0]):
                if first[1] > second[1]:
                    moveList.append('up')
                else:
                    moveList.append('down')
            else:
                if(first[0] > second[0]):
                    moveList.append('left')
                else:
                    moveList.append('right')
        print(moveList)



    game_loop(gameDisplay, clock, grid, forklift, font, packageInfoBox)

    pygame.quit()
    quit()


run()
