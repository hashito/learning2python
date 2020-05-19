word=input("文字列を入力してください> ")

print("command:")
print(" show")
print(" reverse")
print(" (number)")
print(" exit")

while(True):
    c=input("commandを入力してください> ")
    if(c=="reverse"):
        print(''.join(reversed(word)))
    elif(c.isdecimal()):
        if(0<=int(c) and len(word)>int(c)):
            print(word[int(c)])
        else:
            print("over max:",len(word))
    elif(c=="show"):
        print(word)
    elif(c=="exit"):
        break
    else:
        print("no command")

