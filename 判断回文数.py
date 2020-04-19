a = int (input("请输入一个5位的数："))
g = a % 10
s = (a // 10) % 10
q = (a // 1000) % 10
w = a // 10000
if g == w and s == q:
        print(a,"是一个回文数")
else:
    print(a, "不是一个回文数")
