from ImageToArrays import ImageToArrays
from recognise import Recognise

def isEmpty(image):
    mysum = 0
    maxsum = 5
    for x in image:
        for y in x:
            if y > 0:
                mysum +=1 

    if mysum >= maxsum:
        return False
    else:
        return True

a = ImageToArrays(['coordinates.png'])
a.generateArraysNormalized()


print(isEmpty(a.arraysNormalized[0][0][0]))


mysum = 0
for i in range(10):
     print('-' * 40)
     for j in range(8):
         if j == 2 or j == 5:
             print('\t', end='')
             continue
         if isEmpty(a.arraysNormalized[0][i][j]):
             print(' ', end='')
         else:
             s0 = Recognise(a.arraysNormalized[0][i][j])
             print(s0.identify(), end='' )
         if j == 1 or j == 4:
             print('\t', end='')
     print()
