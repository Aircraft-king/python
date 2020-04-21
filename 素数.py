a = int (input("请输入一个正整数："))
i = 2
while i <= (a / 2) + 1 :
    if a % i == 0: break
    i += 1
else:
    print(a,"是素数")
