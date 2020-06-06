#number = 1
#while number <= 10000:
 #   print(number)
  #  number += 1
#for y in range(1, 1000):
#    b=True
#    for x in range(2,y):
#        if (y % x == 0):
#            b=False
#    if(b):
#        print(y)
#


num = input('数字を入力してください')
if int(num) % 4 == 0:
    print('うるう年です')
else:
    print('うるう年ではないです')

