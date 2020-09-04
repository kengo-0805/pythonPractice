# デバッグサンプル
print("1から50までの偶数・奇数を表示する")
print("偶数")
for i in range(1,51):
    n = i % 2
    if n == 0:
        print("{} ".format(i),end="")
print("\n奇数")
for i in range(0,51):
    n = i % 2
    if n == 1:
        print("{} ".format(i),end="")
