a = [1,2,3,4,5,6,7,8,9]
#    0 1 2 3 4 5 6 7 8
print("作成した配列>" , a)

for i in a:
    if(i%2==0):
        print("偶数です>",i)


for index,item in enumerate(a):
    if(item%2==0):
        a[index]='even'
print("evenに変換した配列>" , a)


a[2]="three"
print("threeに変換した配列>" , a)
