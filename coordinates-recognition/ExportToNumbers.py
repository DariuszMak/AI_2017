from ImageToArrays import ImageToArrays
from recognise import Recognise
import sys
from PIL import Image
import numpy as np


a = ImageToArrays(['gridt' + sys.argv[1]+ '.png'])
a.generateArraysNormalized()
for i in range(10):
     for j in range(8):
         im = a.arraysNormalized[0][i][j]
         print(im)
         for x in range(8):
             for y in range(8):
                 im[x][y] -= 0.9
         npim = np.asarray(im)
         #  print(npim)

         im = Image.fromarray(npim, mode = '1')
         im.save('aaa.png')
         break
     #  break


