from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
import time
from collections import Counter


def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = sum(eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
    balance = sum(balanceAr)/len(balanceAr)
    for eachRow in newAr:
        for eachPix in eachRow:
            if sum(eachPix[:3])/len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr





def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(1,10)
    for eachNum in numbersWeHave:
        #print eachNum
        for furtherNum in numbersWeHave:
            # you could also literally add it *.1 and have it create
            # an actual float, but, since in the end we are going
            # to use it as a string, this way will work.
            #  print(str(eachNum)+'.'+str(furtherNum))
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(furtherNum)+'.png'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiarl = str(eiar.tolist())
            lineToWrite = str(eachNum)+'::'+eiarl+'\n'
            numberArrayExamples.write(lineToWrite)


def whatNumIsThis(filePath):

    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    #  import pdb; pdb.set_trace()
    loadExamps = loadExamps.split('\n')[:-1]
    #  import pdb;pdb.set_trace()
    
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamps:
        splitEx = eachExample.split('::')
        currentNum = splitEx[0]
        currentAr = splitEx[1]
        #  print(currentNum)
        
        eachPixEx = currentAr.split('],')
        eachPixInQ = inQuestion.split('],')
        x = 0
        while x < len(eachPixEx):
            print('in EX')
            print(eachPixEx[x])
            print('in Q')
            print(eachPixInQ[x])
            if eachPixEx[x] == eachPixInQ[x]:
                matchedAr.append(int(currentNum))
                print('curNum')
                print(int(currentNum))


            x+=1
                
    print(matchedAr)
    x = Counter(matchedAr)
    print(x)
    print(x[0])

whatNumIsThis('images/test.png')


#  createExamples()

#  i = Image.open('0.1.png')
#  iar = np.array(i)
#  i2 = Image.open('y0.4.png')
#  iar2 = np.array(i2)
#  i3 = Image.open('y0.5.png')
#  iar3 = np.array(i3)
#  i4 = Image.open('../sentdex.png')
#  iar4 = np.array(i4)
#
#
#  iar = threshold(iar)
#  iar2 = threshold(iar2)
#  iar3 = threshold(iar3)
#  iar4 = threshold(iar4)
#
#  fig = plt.figure()
#  ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
#  ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
#  ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
#  ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)
#
#  ax1.imshow(iar)
#  ax2.imshow(iar2)
#  ax3.imshow(iar3)
#  ax4.imshow(iar4)
#
#
#  plt.show()
