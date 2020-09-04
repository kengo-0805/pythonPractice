'''
# 問題3-1
x = input("1つ目の数字：")
y = input("2つ目の数字：")
s1 = float(x)
s2 = float(y)
if s2 == 0:
    print("0での割り算はできません")
else:
    print("足し算：{} 引き算：{} 掛け算：{} 割り算：{}".format(s1+s2,s1-s2,s1*s2,s1/s2))
'''

# 問題3-2
text = input("文字を入力してください：")
count = len(text)
if count < 5:
    print("短い文章")
elif 5 < count < 20:
    print("中くらいの文章")
elif count < 20:
    print("長い文章")
print(count)