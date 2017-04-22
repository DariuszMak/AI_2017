import random
import logging

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


def printLog(forklift, grid):
    if len(str(forklift.x)) == 1:
        info = 'x = ' + str(forklift.x) + '\t\ty = ' + str(forklift.y)
    else:
        info = 'x = ' + str(forklift.x) + '\ty = ' + str(forklift.y)
    logging.debug(info)
