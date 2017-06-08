import pygame
import os
import joblib
from commands.ForkliftCommand import *
from commands.Grid import Grid
from .Forklift import Forklift
from .ForkliftExceptions import *
from .Package import Package
from .PackageInfoBox import PackageInfoBox
from .display_settings import *
from .Tick import Tick
from tree.Tree import *


def game_loop(gameDisplay, clock, tick, grid, forklift, font, carryingPackageInfoBox, mousePackageInfoBox):
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
                if event.key == pygame.K_RIGHTBRACKET:
                    tick.increase()
                if event.key == pygame.K_LEFTBRACKET:
                    try:
                        tick.decrease()
                    except:
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

        mousePackageToDisplay = Package.getPackage(pygame.mouse.get_pos()[0] // GRID_DISTANCE,
                                                   pygame.mouse.get_pos()[1] // GRID_DISTANCE,
                                                   grid)

        carryingPackageInfoBox._display(forklift.carryingPackage, gameDisplay)
        mousePackageInfoBox._display(mousePackageToDisplay, gameDisplay)
        tick._display(gameDisplay)
        pygame.display.update()
        clock.tick(tick.tick)


def run():
    pygame.init()
    font = pygame.font.SysFont("monospace", 15)
    font = pygame.font.Font(None, 30)

    gameDisplay = pygame.display.set_mode(
        (GAME_DISPLAY_WIDTH + MENU_WIDTH, GAME_DISPLAY_HEIGHT))
    pygame.display.set_caption(CAPTION)
    clock = pygame.time.Clock()
    tick = Tick(810, 50, font)

    forklift = Forklift(8, 11)
    carryingPackageInfoBox = PackageInfoBox(810, 180, "CURRENT:", font)
    mousePackageInfoBox = PackageInfoBox(810, 400, "MOUSE:", font)
    grid = Grid(GAME_DISPLAY_WIDTH, GAME_DISPLAY_HEIGHT, GRID_DISTANCE)
    #grid.grid[8][8] = Package(False, False, False, False, True, 'short')
    #grid.grid[2][5] = Package(False, False, False, True, False, None)
    #grid.grid[2][2] = Package(True, False, False, False, False, None)
    grid.grid[2][9] = Package(True, True, False, False, False, None, 8, 'big', 'little', 5)
    #grid.grid[3][1] = Package(False, False, True, False, False, None)
    #grid.grid[7][7] = Package(False, False, False, False, False, None)
    #grid.grid[0][0] = Package(False, False, True, False, False, None)

    packages = []
    packages.append(Package(False, False, False, True, False, None, 8, 'big', 'little', 5))
    packages.append(Package(False, False, False, False, True, 'short', 10, 'short', 'little', -10))
    packages.append(Package(True, False, False, False, False, None, 25, 'short', 'big', 25))
    packages.append(Package(False, False, False, True, False, None, 15, 'mid', 'mid', 10))
    packages.append(Package(False, False, False, False, True, 'short', 20, 'mid', 'big', -15))
    packages.append(Package(True, False, False, False, False, None, 25, 'short', 'big', 20))
    packages.append(Package(False, False, False, True, False, None, 18, 'short', 'mid', 2))
    packages.append(Package(False, False, False, False, True, 'short', 5, 'long', 'little', -5))
    packages.append(Package(True, False, False, False, False, None, 15, 'long', 'mid', 25))
    packages.append(Package(False, False, False, True, False, None, 22, 'long', 'mid', 10))
    packages.append(Package(False, False, False, False, True, 'short', 8, 'mid', 'little', -20))
    packages.append(Package(True, False, False, False, False, None, 9, 'short', 'little', 25))

    #createTree()

    filename = os.path.join('tree', 'tree.pkl')

    decisionTree = joblib.load(filename)

    plot(decisionTree)

    testData = loadCSV(os.path.join('tree', 'test.csv'))
    calculateTest(testData, decisionTree)

    #addNewMove(None, (2, 1))
    #addNewMove(None, (15, 8))
    #addNewMove(grid.grid[0][0], (14, 13))
    #addNewMove(None, (0, 0))

    print('getPackageDistance:', getPackageDistance(grid, grid.grid[2][9], 1, 3))

    # if len(objectList) != 0:
    #     print('There is something')
    #     print(objectList)
    #     coordinateList.append(getAstarPath(grid, (forklift.x, forklift.y), objectList[0][1]))
    #
    #     print(coordinateList)
    #
    #     for step in range(len(coordinateList[0]) - 1):
    #         first = coordinateList[0][step]
    #         second = coordinateList[0][step + 1]
    #         print(coordinateList[0][step], coordinateList[0][step + 1])
    #         if (first[0] == second[0]):
    #             if first[1] > second[1]:
    #                 moveList.append('up')
    #             else:
    #                 moveList.append('down')
    #         else:
    #             if (first[0] > second[0]):
    #                 moveList.append('left')
    #             else:
    #                 moveList.append('right')
    #     print(moveList)

    random_xa = 15
    random_ya = 0
    random_xb = 0
    random_yb = 0
    random_xc = 0
    random_yc = 6

    for package in packages:
        random_number_x = random.randint(6, 10)
        random_number_y = random.randint(0, 9)
        print('Package from grid:', grid.grid[random_number_x][random_number_y])
        walls = get_walls(grid)
        print('Walls first call:', walls)
        if isinstance(grid.grid[random_number_x][random_number_y], Package):
            packages.remove(package)
        else:
            grid.grid[random_number_x][random_number_y] = package
            addNewMove(None, (random_number_x, random_number_y))
            result = classify([package.weight, package.timeOnMagazine, package.size, package.storageTemperature],
                              decisionTree)
            for key in result:
                target = key
            if target == 'sectorA':
                position = grid.grid[random_xa][random_ya]
                while isinstance(position, Package) or position in walls:
                    random_ya += 1
                    position = grid.grid[random_xa][random_ya]
                addNewMove(None, (random_xa, random_ya))
                if random_ya >= 8:
                    if random_xa == 15:
                        random_xa = 13
                        random_ya = 0
                    else:
                        random_xa = 11
                        random_ya = 0
                else:
                    random_ya += 1
            if target == 'sectorB':
                position = grid.grid[random_xb][random_yb]
                while isinstance(position, Package) or position in walls:
                    random_xb += 1
                    position = grid.grid[random_xb][random_yb]
                addNewMove(None, (random_xb, random_yb))
                if random_xb >= 5:
                    if random_yb == 0:
                        random_yb = 2
                        random_xb = 0
                    else:
                        random_yb = 4
                        random_xb = 0
                else:
                    random_xb += 1
            if target == 'sectorC':
                position = grid.grid[random_xc][random_yc]
                while isinstance(position, Package) or position in walls:
                    random_xc += 1
                    position = grid.grid[random_xc][random_yc]
                addNewMove(None, (random_xc, random_yc))
                if random_xc >= 5:
                    if random_yc == 6:
                        random_yc = 8
                        random_xc = 0
                    else:
                        random_yc = 10
                        random_xc = 0
                else:
                    random_xc += 1
            print('Target:', target)

    walls = get_walls(grid)
    print('Walls second call:', walls)

    for i in range(len(objectList)):
        print('There is something in object list:')
        print('Object list:', objectList)
        if i == 0:
            walls.remove(objectList[i][1])
            coordinateList.append(getAstarPath(grid, (forklift.x, forklift.y), objectList[i][1], walls))
        else:
            if i % 2 == 1:
                coordinateList.append(getAstarPath(grid, (objectList[i-1][1][0], objectList[i-1][1][1]), objectList[i][1], walls))
                if objectList[i][1] not in walls:
                    walls.append(objectList[i][1])
                print('Walls, third call:', walls)
            else:
                walls.remove(objectList[i][1])
                coordinateList.append(getAstarPath(grid, (coordinateList[i-1][len(coordinateList[i-1])-2][0], coordinateList[i-1][len(coordinateList[i-1])-2][1]), objectList[i][1], walls))

        print('Coordinate list:', coordinateList)

        for step in range(len(coordinateList[i]) - 1):
            first = coordinateList[i][step]
            second = coordinateList[i][step + 1]
            print('Coordinates First, second:', first, second)
            print('Length of coordinate list of previous step:', len(coordinateList[i])-1)
            print('step:', step)
            if (first[0] == second[0]):
                if first[1] > second[1]:
                   moveList.append('up')
                else:
                   moveList.append('down')
            else:
               if (first[0] > second[0]):
                   moveList.append('left')
               else:
                   moveList.append('right')
            if step == len(coordinateList[i]) - 2 and i % 2 == 0:
               moveList.append('liftPackage')
            if step == len(coordinateList[i]) - 2 and i % 2 == 1:
               moveList.append('lowerPackage')
        print('Single moveList:', moveList)
    print('Entire moveList:', moveList)
    forkliftCommandInit(forklift, grid)
    game_loop(gameDisplay, clock, tick, grid, forklift, font, carryingPackageInfoBox, mousePackageInfoBox)

    pygame.quit()
    quit()


run()
