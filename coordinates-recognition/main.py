from ImageToArrays import ImageToArrays
import math
import os
import copy
import PIL.Image
import numpy as np
import random
import sys
import pdb
import time


np.set_printoptions(threshold=np.nan)
start_time = time.time()

impath = 'python-image-recognition/images/numbers'

def getDigitImgs(digit):
    kk  = [ a for a in os.listdir('python-image-recognition/images/numbers') if a[0] == str(digit) ]
    return [ impath + '/' + a for a in kk]


def getDigitNorms(ssdigit):
    xx = list()
    for im in ssdigit:
        a = PIL.Image.open(im)
        a = np.asarray(a)
        b = [[0] * 8 for i in range(8) ]
        for j in range(len(a)):
            for k in range(len(a[0])):
                b[j][k] = 0 if a[j][k][0] > 120 else 1
        c = copy.deepcopy(b)
        xx.append(c)
    return xx


s0 = getDigitNorms(getDigitImgs(0))
s1 = getDigitNorms(getDigitImgs(1))
s2 = getDigitNorms(getDigitImgs(2))
s3 = getDigitNorms(getDigitImgs(3))
s4 = getDigitNorms(getDigitImgs(4))
s5 = getDigitNorms(getDigitImgs(5))
s6 = getDigitNorms(getDigitImgs(6))
s7 = getDigitNorms(getDigitImgs(7))
s8 = getDigitNorms(getDigitImgs(8))
s9 = getDigitNorms(getDigitImgs(9))

trainingSet = [s0,s1,s2,s3,s4,s5,s6,s7,s8,s9]
#  ----------------------------------------------------------------------------------------------------


for sdd in trainingSet:
    for i in range(len(sdd)):
        sdd[i] = [item for sublist in sdd[i] for item in sublist] # to jest spłaszczanie listy
        sdd[i] = np.asarray(sdd[i], dtype = np.float32 )
        sdd[i] = np.append(sdd[i], [1.0]) # z extra 1 tak jak trzeba zrobic wektor

u = list()
for i in trainingSet[:-1]:
    u.extend(i[:-1])


learning_now = sys.argv[1]
print(learning_now)
if learning_now == '0':
    z = [1] * 25 + [0] * 25 +  [0] * 25+ [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 
elif learning_now == '1':
    z = [0] * 25 + [1] * 25 +  [0] * 25+ [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 
elif learning_now == '2':
    z = [0] * 25 + [0] * 25 +  [1] * 25+ [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 
elif learning_now == '3':
    z = [0] * 25 + [0] * 25 +  [0] * 25+ [1] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 
elif learning_now == '4':
    z = [0] * 25 + [0] * 25 +  [0] * 25+ [0] * 25 + [1] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 
elif learning_now == '5':
    z = [0] * 25 + [0] * 25 +  [0] * 25+ [0] * 25 + [0] * 25 + [1] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 
elif learning_now == '6':
    z = [0] * 25 + [0] * 25 +  [0] * 25+ [0] * 25 + [0] * 25 + [0] * 25 + [1] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 
elif learning_now == '7':
    z = [0] * 25 + [0] * 25 +  [0] * 25+ [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [1] * 25 + [0] * 25 + [0] * 25 + [0] * 25 
elif learning_now == '8':
    z = [0] * 25 + [0] * 25 +  [0] * 25+ [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [1] * 25 + [0] * 25 + [0] * 25 
elif learning_now == '9':
    z = [0] * 25 + [0] * 25 +  [0] * 25+ [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [0] * 25 + [1] * 25 + [0] * 25 
else:
    assert False
    





z = np.asarray(z, dtype=np.float32) 

kmax = len(s0[0])
pmax = len(u) 


wold = [ [0] * kmax for k in range(kmax -1) ]
wnew = [ [1] * kmax for k in range(kmax -1) ]


wold = np.array(wold, dtype = np.float32)
wnew = np.array(wnew, dtype = np.float32)


for i in range(len(wold)):
    for j in range(len(wold[0])):
        wold[i][j] = random.random()
        wnew[i][j] = random.random()

snew = [1] * kmax
sold = [0] * kmax


snew = np.asarray(snew, dtype = np.float32)
sold = np.asarray(sold, dtype = np.float32)

for i in range(len(sold)):
    sold[i] = random.random()
    snew[i] = random.random()

c = float(sys.argv[2]) # 3.0   1.5 5
eps = 0.0001  # 0.000001
beta = 0.1  # 3.0

################################################################################

def f(u):
    #  print(1 / (1 + math.exp(-beta * u)))
    return 1 / (1 + math.exp(-beta * u))


def fp(u):
    fu_value = f(u)
    return beta * fu_value * (1 - fu_value)

def is_greater_than_eps(wnew, wold, snew, sold):
    for i in range(len(wnew)):
        for j in range(len(wnew[i])):
            if abs(wnew[i][j] - wold[i][j]) >= eps:
                return True

    for i in range(len(snew)):
        if abs(snew[i] - sold[i]) >= eps:
            return True

    return False

################################################################################


def printU(u):

    x = [None] * kmax

    for i in range(len(wnew)):
        ksum = 0
        for k in range(len(wnew[i])):
            ksum +=  wnew[i][k] * u[k]
        x[i] = f( ksum )
    x[k] = 1

    ksum = 0
    for k in range(len(snew)):
        ksum += snew[k] * x[k] 
    #  print(u)
    print(ksum)


x = [ [0] * kmax for p in range(pmax)]
x = np.asarray(x, dtype = np.float32)


y = [0] * pmax
y = np.asarray(y, dtype = np.float32)


ES = [0] * kmax
ES = np.asarray(ES, dtype = np.float32)


EW = [ [0] * kmax for k in range(kmax -1) ]
EW = np.asarray(EW, dtype = np.float32)
max_iterations = 500
for iteration in range(max_iterations):
    printU(s0[-1])
    printU(s1[-1])
    printU(s2[-1])
    printU(s3[-1])
    printU(s4[-1])
    printU(s5[-1])
    printU(s6[-1])
    printU(s7[-1])
    printU(s8[-1])
    printU(s9[-1])
    print('-' * 50)
    file_vec = open('./vectors/' + sys.argv[1] + '-' + sys.argv[2] + '-' +str(iteration) , 'wb')
    np.save(file_vec, wnew)
    file_vec.close()
    file_vec = open('./vectors/s' + sys.argv[1] + '-' + sys.argv[2] + '-' +str(iteration) , 'wb')
    np.save(file_vec, snew)
    file_vec.close()
    print('-' * 50)
    print('iteration' + str(iteration) + '/' + str(max_iterations))
    time_now = time.time()
    time_delta = int(time_now - start_time )
    print("elapsed time: ",  time_delta // 60, time_delta % 60 )



    if not is_greater_than_eps(wnew,wold, snew,sold):
        break
    

    for p in range(len(x)):
        for i in range(len(wold)):
            x[p][i] = f( sum(np.multiply(wold[i], u[p])))
        x[p][-1] = 1.0

    for p in range(len(y)):
        y[p] = f( sum (np.multiply(sold, x[p])))

    # pochES


    for i in range(len(x[0])):
        suma = 0
        for p in range(len(y)):
            ksum = sum (np.multiply(sold, x[p]))
            suma += (y[p] - z[p] ) * fp( ksum ) * x[p][i]
        ES[i] = suma

    # pochEW

    print('a')
    pmax  = len(x)
    for i in range(len(EW)):
        for j in range(len(EW[0])):
            suma = 0
            for p in range(pmax):
                suma += (y[p] - z[p] ) * fp( sum( np.multiply(sold, x[p]) ) ) * sold[i] * fp( sum( np.multiply(wold[i], u[p])) ) * u[p][j]
            EW[i][j] = suma

    print('b')
    # nowe wartości
    for i in range(len(snew)):

        snew[i] = sold[i] -c*ES[i]

    wold = copy.deepcopy(wnew)
    sold = copy.deepcopy(snew)


    for i in range(len(wnew)):
        for j in range(len(wnew[i])):
            wnew[i][j] = wnew[i][j] - c*EW[i][j]

#---------------------------------------------------------------------------------------------------- 
print('KONIEC')


for digit in trainingSet: 
    for u in digit:
        x = [None] * kmax

        for i in range(len(wnew)):
            ksum = 0
            for k in range(len(wnew[i])):
                ksum +=  wnew[i][k] * u[k]
            x[i] = f( ksum )
        x[k] = 1

        ksum = 0
        for k in range(len(snew)):
            ksum += snew[k] * x[k] 
        #  print(u)
        print(ksum)
    print('-' * 50)

