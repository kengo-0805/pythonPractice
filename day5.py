'''
# 問題5-1

tango = []
while True:
    s = input("単語を入力：")
    if s == "":
        break
    else:
        tango.append(s)

for i in range(len(tango)):
    print("{}".format(tango[i]))

# 問題5-3
inline = input("英語で動物の名前を入力；") 
d = {"cat" : "猫","dog" : "犬"}
print("「{}」です．".format(d[inline]))
'''
# 問題5-2

odd = []
even = []
count = 0

while True:
    num = input("整数を入力；")
    if num == "":
        break
   
    suuzi = int(num)

    if (suuzi % 2) == 0:
        even.append(suuzi)
    else:
        odd.append(suuzi)
    count += 1

for suuzi in even:
    print(suuzi,end=" ")

print("奇数：{}".format(odd))
print("偶数；{}".format(even))