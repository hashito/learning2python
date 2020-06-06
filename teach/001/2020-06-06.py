
# 1st
a=input(">")

ass=a.split(" ")
a1=int(ass[0])
a2=str(ass[1])
a3=int(ass[2])

if(a2=="*"):
    print(a1*a3)
elif(a2=="+"):
    print(a1+a3)
elif(a2=="-"):
    print(a1-a3)
elif(a2=="/"):
    print(a1/a3)



# 特定文字列により切り分け