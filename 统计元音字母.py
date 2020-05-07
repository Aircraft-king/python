s = input("请输入字符串：")
num = 0
for i in s :
    if i in ['a','A','e','E','i','I','o','O','u','U']:
        num += 1
print(num)
