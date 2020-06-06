
nums=[]

while(True):
    i = input("number add('q'=end)>")
    if(i.isdecimal()):
        nums.append(int(i))
        print("add number",int(i))
    elif(i=="q"):
        break
    else:
        print("this is string")

print("command is")
print(" max")
print(" min")
print(" ave")
print(" all")
print(" len")
print(" q")

while(True):
    i = input("command >")
    if(i=="max"):
        print(max(nums))
    elif(i=="min"):
        print(min(nums))
    elif(i=="ave"):
        print(sum(nums)/len(nums))
    elif(i=="all"):
        print(nums)
    elif(i=="len"):
        print(len(nums))
    elif(i=="q"):
        break
    else:
        print("this is no command",i)
