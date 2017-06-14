from ImageToArrays import ImageToArrays
from recognise import Recognise



a = ImageToArrays(['grid10.png'])
a.generateArraysNormalized()
mysum = 0
for i in range(10):
     print('-' * 40)
     for j in range(8):
         print(i,end='\t'); 
         s0 = Recognise(a.arraysNormalized[0][i][j]) ; print(s0.identify(), end='\t' ), print(i==s0.identify())
         if i==s0.identify():
             mysum += 1


print(mysum/80)
