

# 問題2-1
s1 = input("1つ目の数：")
s2 = input("2つ目の数：")
s3 = input("3つ目の数：")
x = int(s1)
y = int(s2)
z = int(s3)
print("{}+{}+{}={}".format(x,y,z,x+y+z))

# 問題2-2
name = input("名前：")
age = input("年齢：")
print("{}さんは{}歳です．".format(name,age))

# 問題2-3
PI = 3.14
ra = input("円の半径(cm)：")
r = float(ra)
print("円周の長さ：{} 面積；{}".format(2*PI*r,PI*r*r))