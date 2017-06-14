import math
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

lastForkliftPosition = None


# carrying = False


def singleMove(forklift, grid):
    # print(coordinateList)
    # print(moveList)
    # print(forklift.direction)
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

        elif moveList[0] == 'liftPackage':
            forklift.liftPackage(grid)
            moveList.pop(0)

        elif moveList[0] == 'lowerPackage':
            forklift.lowerPackage(grid)
            forklift.moveBackward(grid)
            moveList.pop(0)


            # print(moveList)
            #
            # if moveList:
            #     if moveList[0]:
            #         print("Step: " + str(moveList[0].pop(0)))
            #         print('Lenght: ' + str(len(moveList)))
            # else:
            #     moveList.append(getAstarPath(grid, (forklift.x, forklift.y), objectList[0][1]))
            # print(objectList[0][0])


def calculatePath(forklift, grid, walls):
    global coordinateList
    global objectList
    global lastForkliftPosition

    if lastForkliftPosition is None:
        lastForkliftPosition = (forklift.x, forklift.y)
    else:
        lastForkliftPosition = coordinateList[-1][-2]
    coordinateList = []

    print('coordinate list special:', coordinateList)
    print('Walls second call:', walls)

    for i in range(len(objectList)):
        print('There is something in object list:')
        print('Object list:', objectList)
        if objectList[i][1] in walls:
            walls.remove(objectList[i][1])
            if i == 0:
                coordinateList.append(getAstarPath(grid, lastForkliftPosition, objectList[i][1], walls))
            else:
                coordinateList.append(getAstarPath(grid, (coordinateList[i - 1][len(coordinateList[i - 1]) - 2][0],
                                                          coordinateList[i - 1][len(coordinateList[i - 1]) - 2][1]),
                                                   objectList[i][1], walls))
                # x, y = coordinateList[-1][-1]
                # coordinateList[-1][-1] = (x, y, -1)
        else:
            if i == 0:
                coordinateList.append(
                    getAstarPath(grid, lastForkliftPosition, objectList[i][1], walls))
            else:
                coordinateList.append(
                    getAstarPath(grid, (objectList[i - 1][1][0], objectList[i - 1][1][1]), objectList[i][1], walls))
            if objectList[i][1] not in walls:
                walls.append(objectList[i][1])
            # coordinateList[-1].append((-2, -2))
            print('Walls, third call:', walls)

        print('Coordinate list:', coordinateList)

        for step in range(len(coordinateList[i]) - 1):
            first = coordinateList[i][step]
            second = coordinateList[i][step + 1]
            print('Coordinates First, second:', first, second)
            print('Length of coordinate list of previous step:', len(coordinateList[i]) - 1)
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

    objectList = []
    print('Entire moveList:', moveList)


def addNewMove(object, place):
    objectList.append((object, place))


def forkliftCommandInit(forklift, grid):
    print('Here is forklift command init')
    pass


def forkliftCommand(forklift, grid):
    # forklift.turnLeft(grid)
    # print(getAstarPath(grid, (forklift.x,forklift.y), (3,2)))

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
            # print(counter_rows, counter_columns, j)
            if isinstance(j, Package):
                walls.append((counter_rows, counter_columns))
            counter_columns += 1
        counter_rows += 1
    return walls


def getAstarPath(grid, start, end, walls):
    astar = AStar()
    # walls = get_walls(grid)
    print('Walls')
    print(walls)
    astar.init_grid(grid._HEIGHT, grid._WIDTH, walls, start, end)
    return astar.solve()


def getPackageDistance(grid, package, x, y):
    if isinstance(package, Package):
        packageProperties = [False] * 5
        print(packageProperties)
        if package.flammable:
            packageProperties[0] = True
        if package.explosive:
            packageProperties[1] = True
        if package.radioactive:
            packageProperties[2] = True
        if package.medical:
            packageProperties[3] = True
        if package.food:
            packageProperties[4] = True

        boolTemp = False
        for booleanValue in packageProperties:
            if booleanValue:
                boolTemp = True

        if not boolTemp:
            return None

        print(packageProperties)
        generalList = []
        generalCounter = 0

        for property in packageProperties:
            if property:
                list = [20 for x in range(5)]
                # print(list)
                if generalCounter == 0:
                    list[0] = 0
                if generalCounter == 1:
                    list[1] = 0
                if generalCounter == 2:
                    list[2] = 0
                if generalCounter == 3:
                    list[3] = 0
                if generalCounter == 4:
                    list[4] = 0

                counter_rows = 0

                package_x = 0
                package_y = 0

                for i in grid.grid:
                    counter_columns = 0
                    for j in i:
                        if j is package:
                            package_x = counter_rows
                            package_y = counter_columns
                        counter_columns += 1
                    counter_rows += 1
                counter_rows = 0
                for i in grid.grid:
                    counter_columns = 0
                    for j in i:
                        if isinstance(j, Package):
                            distance = math.sqrt((x - counter_rows) ** 2 + (y - counter_columns) ** 2)
                            if j.flammable and list[0] > distance:
                                list[0] = distance
                            if j.explosive and list[1] > distance:
                                list[1] = distance
                            if j.radioactive and list[2] > distance:
                                list[2] = distance
                            if j.medical and list[3] > distance:
                                list[3] = distance
                            if j.food and list[4] > distance:
                                list[4] = distance
                                # print(distance)
                        counter_columns += 1
                    counter_rows += 1
                generalList.append([generalCounter + 1] + list)
            generalCounter += 1
        # print(grid.grid[x][y])
        if grid.grid[x][y] is not None:
            return None
        return generalList
    else:
        return None
