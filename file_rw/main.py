
with open("out.txt",mode="r") as f:
    print("あなたの好きな文字はこちらです? > ",f.read())


w = input("好きな文字を入力してください > ")
print("好きな文字はこちらですね > ",w)

with open("out.txt",mode="w") as f:
    f.write(w)
