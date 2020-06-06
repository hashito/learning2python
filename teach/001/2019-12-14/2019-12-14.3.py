import random
import time

a = 0
b = 0
goal = 100
user = input('aとbのどちらのカメが勝つか?')

print('競争開始!')
while (a < goal) and (b < goal):
    print('---')
    a += random.randint(1,6)
    b += random.randint(1,6)
    print('a:' + '>' * a + '@')
    print('b:' + '>' * b + '@')
    time.sleep(1)

if a == b:
    winner = '同時'
elif a > b:
    winner = 'a'
else:
    winner = 'b'

if winner == user:
    print('当たり!') 
else:
    print('はずれ')
