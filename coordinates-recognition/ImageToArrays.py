import numpy as np
import PIL.Image


class ImageToArrays():

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, imagePathList):

        self.imageList = list()
        self.npArrayList = list()

        for imagePath in imagePathList:
            im = PIL.Image.open(imagePath)
            self.imageList.append(im)
            self.npArrayList.append(np.asarray(im))

        self.width = 8  
        self.height = 10
        self.step = 9

    def _getArrays(self, nparray):
        letters = [[None for i in range(self.width)]
                        for i in range(self.height)]

        for i in range(len(letters)):
            for j in range(len(letters[i])):
                letters[i][j] = np.asarray(
                    [k[j * self.step:(j + 1) * self.step - 1] for k in nparray[i * self.step:(i + 1) * self.step - 1]])
        return letters

    def _getArraysNormalized(self, letters):
        lettersNormalized = [[None for i in range(self.width)] for j in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                lettersNormalized[i][j] = [0] * (self.step-1)
                for z in range(self.step-1):
                    lettersNormalized[i][j][z] = [0] * (self.step-1)

                pass

        for i in range(len(letters)):
            for j in range(len(letters[i])):
                for x in range(self.step-1):
                    for y in range(self.step-1):
                        lettersNormalized[i][j][x][y] = 0 if letters[i][j][x][y][0] > 0 else 1
        return lettersNormalized


    def generateArraysNormalized(self,):
        self.arraysNormalized = list()
        for i in self.npArrayList:
            a = self._getArrays(i)
            b = self._getArraysNormalized(a)
            self.arraysNormalized.append(b)


    def alhpabet():
        for i in ImageToArrays.alphabet:
            yield i

if __name__ == '__main__':
    a = ImageToArrays(['grid10.png'])
    a.generateArraysNormalized()
    print(a.arraysNormalized[0][0][0])
    #  npar = a._getArrays(a.npArrayList[0])
    #  arnorm = a._getArraysNormalized(npar)

    #  l = 0
    #  for i in a.letters:
    #      for j in i:
    #          a = PIL.Image.fromarray(j)
    #  a.save(str(l) + str('.png'))
    #          l += 1

