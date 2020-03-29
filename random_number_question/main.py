import random

in_val = input("数字を入力してください>")
print("入力>",in_val)
in_val=int(in_val)

ran_val = random.randrange(11)
print("ランダムな数>",ran_val)

if(in_val>ran_val):
    print("大きい")
elif(in_val<ran_val):
    print("小さい")
else:
    print("同じ")
