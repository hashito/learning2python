points=[]
points.append(int(input("こくご")))
points.append(int(input("さんすう")))
points.append(int(input("りか")))
points.append(int(input("しゃかい")))
points.append(int(input("えいご")))

print(points)
max=points[0]
min=points[0]
sum=0
for i in points:
    if(max<i):
        max=i

for i in points:
    if(min>i):
        min=i

for i in points:
    sum+=i
ave = sum / len(points)

print(max,min,ave)