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
import numpy as np
import matplotlib.pyplot as plt

#data = tsa.read_csv("juyo_2017_tohoku.txt")
juyo_2016 = tsa.read_csv("juyo-2016.txt")
#i=0
#for x in data:
#    print(i,x)
#    i=i+1

def show(name):
    data     = tsa.read_csv(name)
    day1     = data
    max_day1 = 100000000
    for i in day1:
        if(i<max_day1):
            max_day1=i

    print(name,"min",max_day1)
    for i in day1:
        if(i>max_day1):
            max_day1=i

    print(name,"max",max_day1)

    cunt=0
    sums=0
    for i in day1:
        sums+=i
        cunt=cunt+1
    print(name,"ave",sums/cunt)
    print(name,"sum",sums)

show("juyo-2016.txt")
show("juyo-2017.txt")
show("juyo-2018.txt")
show("juyo-2019.txt")
show("juyo_2017_tohoku.txt")

#plt.plot(day1)
#plt.show()
