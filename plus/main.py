import random
r = random.randrange(9)+1
#print(r) #1-9

r1 = random.randrange(9)+1
#print(r1) #1-9
print(r,"+",r1)
#print("{} + {}".format(r,r1))
#print("{1} + {0}".format(r,r1))

in1 = input("こたえをにゅうりょく>")
anser = r + r1
if(anser == int(in1)):
    print("正解です")

