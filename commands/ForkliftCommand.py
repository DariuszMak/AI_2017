import random
import logging

logging.basicConfig(level=logging.ERROR, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')

def forkliftCommand(forklift, grid):
    if len(str(forklift.x)) == 1:
        info = 'x = ' + str(forklift.x) + '\t\ty = ' + str(forklift.y)
    else:
        info = 'x = ' + str(forklift.x) + '\ty = ' + str(forklift.y)
    logging.debug(info)



def update(forklift):
    pass
