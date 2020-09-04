'''
# 問題4-1
while True:
    hello = input("Helloと入力：")
    if hello == "Hello":
        print("Helloと入力されました")
        break
    print("Helloと入力してください")
'''
# 問題4-2
x = input("1つ目の数値：")
y = input("2つ目の数値：")

s1 = float(x)
s2 = float(y)

if s1 == s2:
    print("異なる数値を入力してください")
elif s1 > s2: # 1つ目が2つ目よりおおきい
    print(s2)
    while True:
        if s1 <= s2:
            break
        s2 = s2 + 1
        print(s2)

elif s1 < s2: # 1つ目が2つ目よりちいさい
    print(s1)
    while True:
        if s1 >= s2:
            break
        s1 = s1 + 1
        print(s1)
        