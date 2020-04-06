a = int(input("请输入工资："))
y = float(0)
if a>=5000:
    if a<36000:
        y = 0.03 * (a - 5000)
    elif a <1440000:
        y = 0.1 * (a - 5000) - 2520
    else: y = 0.2 * (a - 5000) - 16920
else: y = 0 
print("应交税款为：",y)
input(' ')
