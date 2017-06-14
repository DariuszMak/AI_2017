import os
import math
import numpy as np
import PIL.Image
import copy
import sys

kmax =  65
class Letter():
    
    def __init__(self, name,):
        self.name  = int(name)
        if name == '0':
            self.vectorFilePath = os.path.join('vectors','0-1-290')
            self.svectorFilePath = os.path.join('vectors','s0-1-290')
            self.max_v = 6
            self.min_v = -44
        elif name == '1':
            self.vectorFilePath = os.path.join('vectors','1-1-495')
            self.svectorFilePath = os.path.join('vectors','s1-1-495')
            self.max_v = 18
            self.min_v = -55
        elif name == '2':
            self.vectorFilePath = os.path.join('vectors','2-1-495')
            self.svectorFilePath = os.path.join('vectors','s2-1-495')
            self.max_v = 14 
            self.min_v = -60
        elif name == '3':
            self.vectorFilePath = os.path.join('vectors','3-1-495')
            self.svectorFilePath = os.path.join('vectors','s3-1-495')
            self.max_v = 20
            self.min_v = -60
        elif name == '4':
            self.vectorFilePath = os.path.join('vectors','4-1-495')
            self.svectorFilePath = os.path.join('vectors','s4-1-495')
            self.max_v = 56
            self.min_v = -62
        elif name == '5':
            self.vectorFilePath = os.path.join('vectors','5-1-495')
            self.svectorFilePath = os.path.join('vectors','s5-1-495')
            self.max_v = 26
            self.min_v = -63
        elif name == '6':
            self.vectorFilePath = os.path.join('vectors','6-1-495')
            self.svectorFilePath = os.path.join('vectors','s6-1-495')
            self.max_v = 24 
            self.min_v = -53
        elif name == '7':
            self.vectorFilePath = os.path.join('vectors','7-1-495')
            self.svectorFilePath = os.path.join('vectors','s7-1-495')
            self.max_v = 11
            self.min_v = -51
        elif name == '8':
            self.vectorFilePath = os.path.join('vectors','8-1-495')
            self.svectorFilePath = os.path.join('vectors','s8-1-495')
            self.max_v = -1
            self.min_v = -24
        elif name == '9':
            self.vectorFilePath = os.path.join('vectors','9-0.8-20')
            self.svectorFilePath = os.path.join('vectors','s9-0.8-20')
            self.max_v = -20
            self.min_v = -40

        v_file = open(self.vectorFilePath, 'rb')
        self.vector = np.load(self.vectorFilePath)
        self.svector = np.load(self.svectorFilePath)


class Recognise():

    digits = [ Letter('0'),
                Letter('1'),
                Letter('2'),
                Letter('3'),
                Letter('4'),
                Letter('5'),
                Letter('6'),
                Letter('7'),
                Letter('8'),
                Letter('9'),
            ]

    beta = 0.1
    def __init__(self, image):
        #  a = np.asarray(image)
        #
        #  b = [[0] * 8 for i in range(8) ]
        #  for j in range(len(a)):
        #      for k in range(len(a[0])):
        #          b[j][k] = 0 if a[j][k][0] > 120 else 1
        #  c = copy.deepcopy(b)
        c = image

        c = [item for sublist in c for item in sublist] # to jest spłaszczanie listy
        c = np.asarray(c, dtype = np.float32 )
        c = np.append(c, [1.0]) # z extra 1 tak jak trzeba zrobic wektor

        self.image = c


    def f(u):
        return 1 / (1 + math.exp(-Recognise.beta * u))

    def getRating(self, digit):
        x = [None] * kmax
        for i in range(len(digit.vector)):
            ksum = 0
            for k in range(len(digit.vector[i])):
                ksum +=  digit.vector[i][k] * self.image[k]
            x[i] = Recognise.f( ksum )
        x[k] = 1

        ksum = 0
        for k in range(len(digit.svector)):
            ksum += digit.svector[k] * x[k] 
        #  print(u)

        return ksum
    
    def getPercentage(self, digit):
        rating = self.getRating(digit)
        normalized = 100 * (rating - digit.min_v ) / (digit.max_v - digit.min_v) 
        return normalized


    def identify(self):
        max_v, maxargs = -1000, -1000
        for digit in Recognise.digits:
            digit_per = self.getPercentage(digit) 
            if self.getPercentage(digit) > max_v:
                max_v = digit_per
                recognised = digit.name
        return recognised


             
if __name__ == '__main__':
    ii = range(10)
    jj = range(1,10)
    for i in ii:
        for j in jj:
            imPath = 'python-image-recognition/images/numbers/0.1.png'
            imPath = 'python-image-recognition/images/numbers/' + str(i) + '.' + str(j) + '.png'
           
            im = PIL.Image.open(imPath)
            s0 = Recognise(im)
            #  print(s0.getPercentage(s0.digits[0]))
            print(i, j, s0.identify()) 
