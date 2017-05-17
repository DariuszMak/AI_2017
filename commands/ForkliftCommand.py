import random
from game.Package import Package
from astar.Astar import AStar
import logging
from game.Forklift import Forklift

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

objectList = []

coordinateList = []

moveList = []

#carrying = False


def singleMove(forklift,grid):
    print(coordinateList)
    print(moveList)
    print(forklift.direction)
    print(Forklift.getPossibleActions(
            forklift.x, forklift.y,
            forklift.direction,
            forklift.carryingPackage, grid))
    if moveList:
        random_number = random.randint(0, 1)

        if moveList[0] == 'up':
            if forklift.direction == 'up':
                forklift.moveForward(grid)
                moveList.pop(0)
            else:
                if forklift.direction == 'left':
                    forklift.turnRight(grid)
                elif forklift.direction == 'right':
                    forklift.turnLeft(grid)
                else:
                    if random_number:
                        forklift.turnRight(grid)
                    else:
                        forklift.turnLeft(grid)

        elif moveList[0] == 'down':
            if forklift.direction == 'down':
                forklift.moveForward(grid)
                moveList.pop(0)
            else:
                if forklift.direction == 'right':
                    forklift.turnRight(grid)
                elif forklift.direction == 'left':
                    forklift.turnLeft(grid)
                else:
                    if random_number:
                        forklift.turnRight(grid)
                    else:
                        forklift.turnLeft(grid)

        elif moveList[0] == 'left':
            if forklift.direction == 'left':
                forklift.moveForward(grid)
                moveList.pop(0)
            else:
                if forklift.direction == 'down':
                    forklift.turnRight(grid)
                elif forklift.direction == 'up':
                    forklift.turnLeft(grid)
                else:
                    if random_number:
                        forklift.turnRight(grid)
                    else:
                        forklift.turnLeft(grid)

        elif moveList[0] == 'right':
            if forklift.direction == 'right':
                forklift.moveForward(grid)
                moveList.pop(0)
            else:
                if forklift.direction == 'up':
                    forklift.turnRight(grid)
                elif forklift.direction == 'down':
                    forklift.turnLeft(grid)
                else:
                    if random_number:
                        forklift.turnRight(grid)
                    else:
                        forklift.turnLeft(grid)


        # print(moveList)
        #
        # if moveList:
        #     if moveList[0]:
        #         print("Step: " + str(moveList[0].pop(0)))
        #         print('Lenght: ' + str(len(moveList)))
        # else:
        #     moveList.append(getAstarPath(grid, (forklift.x, forklift.y), objectList[0][1]))
        # print(objectList[0][0])


def addNewMove(object, place):
    objectList.append((object, place))


def forkliftCommand(forklift, grid):
    #forklift.turnLeft(grid)
    #print(getAstarPath(grid, (forklift.x,forklift.y), (3,2)))

    singleMove(forklift, grid)
    printLog(forklift, grid)
    printPossibleActions(forklift, grid)


def printLog(forklift, grid):
    if forklift.carryingPackage:
        carryingInfo = '\t carrying a package'
    else:
        carryingInfo = '\t not carrying a package'

    if len(str(forklift.x)) == 1:
        info = 'x = ' + str(forklift.x) + '\t\ty = ' + str(forklift.y) + '\t' + forklift.direction + carryingInfo
    else:
        info = 'x = ' + str(forklift.x) + '\ty = ' + str(forklift.y) + '\t' + forklift.direction + carryingInfo
    logging.debug(info)


def printPossibleActions(forklift, grid):
    info = 'POSSIBLE ACTIONS: '
    info += str(Forklift.getPossibleActions(
            forklift.x, forklift.y,
            forklift.direction,
            forklift.carryingPackage, grid))
    logging.debug(info)

def get_walls(grid):
    walls = []
    counter_rows = 0
    for i in grid.grid:
        counter_columns = 0
        for j in i:
            #print(counter_rows, counter_columns, j)
            if isinstance(j, Package):
                walls.append((counter_rows, counter_columns))
            counter_columns += 1
        counter_rows += 1
    return walls

def getAstarPath(grid, start, end):
    astar = AStar()
    walls = get_walls(grid)
    astar.init_grid(grid._HEIGHT, grid._WIDTH, walls, start, end)
    return astar.solve()
