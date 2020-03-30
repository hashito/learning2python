# [正解]  print("0 1 2 3 4 5 6 7 .. 98 99")
# [不正解] print("2 4 6 8 10 12 14 .. 96 88")

print("--ぐう数--")
for i in range(100):
#    if (i % 2 == 0 ) and i != 0:
    if (i % 2 == 0 ):
        print(i)

print("--き数--")
for i in range(100):
    if not(i % 2 == 0 ):
        print(i)