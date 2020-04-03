import random

print()


hand=input("グー(0)チョキ(1)パー(2)>")
try:
    hand = int(hand)
    if(hand>=0 and hand<=2):
        mhand = random.randrange(0,3)
        if(mhand == 0):
            print("グー")
        elif(mhand == 1):
            print("チョキ")
        elif(mhand == 2):
            print("パー")

        if(mhand==hand):
            print("あいこ")
        elif(hand==0):
            if(mhand==1):
                print("勝ち")
            if(mhand==2):
                print("負け")
        elif(hand==1):
            if(mhand==0):
                print("負け")
            if(mhand==2):
                print("勝ち")
        elif(hand==2):
            if(mhand==0):
                print("勝ち")
            if(mhand==1):
                print("負け")
    else:
        print("ただしくにゅうりょくしてください")        
except:
    print("ただしくにゅうりょくしてください")

