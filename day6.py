def add_four (a,b,c,d):
    print("{}+{}+{}+{}={}".format(a,b,c,d,a+b+c+d))
    return a+b+c+d

a = int(input("1つ目の数値；"))
b = int(input("2つ目の数値："))
c = int(input("3つ目の数値："))
d = int(input("4つ目の数値："))
print("{}+{}+{}+{}={}".format(a,b,c,d,a+b+c+d))
add_four