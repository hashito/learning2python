import random
hand=input("グー(0)チョキ(1)パー(2)>")
hands=["グー","チョキ","パー"]
texts=["あいこ","勝ち","負け"]
judge=[
    [0,1,2],
    [2,0,1],
    [1,2,0]
    ]

try:
    hand = int(hand)
    if(hand>=0 and hand<=2):
        mhand = random.randrange(0,3)
        print(hands[mhand])
        print(texts[judge[hand][mhand]])
    else:
        print("ただしくにゅうりょくしてください")        
except:
    print("ただしくにゅうりょくしてください")

