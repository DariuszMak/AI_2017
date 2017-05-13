import random
import logging
from game.Forklift import Forklift

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')


def forkliftCommand(forklift, grid):
    # random_number = random.random()
    # if random_number < 0.01:
    #     forklift.moveForward(grid)
    # elif random_number < 0.02:
    #     forklift.moveBackward(grid)
    # elif random_number < 0.03:
    #     forklift.turnLeft(grid)
    # elif random_number < 0.04:
    #     forklift.turnRight(grid)

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
        carryingInfo = 'carrying'
    logging.debug(info)


def printPossibleActions(forklift, grid):
    info = 'POSSIBLE ACTIONS: '
    info += str(Forklift.getPossibleActions(
            forklift.x, forklift.y,
            forklift.direction,
            forklift.carryingPackage, grid))
    logging.debug(info)
