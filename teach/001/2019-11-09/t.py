# coding: utf-8
#print('hi!')
#for i in range(100000001):
    #print('{0}'.format(i))
#s = 0
#for x in range(1,11):
    #s += x
#print(s)
#for i in range(2,100):
 #   if 0 not in [i%j for j in range(2,i/2+1)]:
  #      print (i)



# coding: utf-8
import tsa

data = tsa.read_csv("juyo_2017_tohoku.txt")
y=[]
i=0
for x in data:
    print(i,x)
    y.append(i)
    i=i+1

import numpy as np
import matplotlib.pyplot as plt

plt.plot(data[24:48])
plt.show()