a = float(input("请输入三角形的边长a："))
b = float(input("请输入三角形的边长b："))
c = float(input("请输入三角形的边长c："))
p = (a + b + c)/2
s = (p * (p - a) * (p - b) * (p - c) ) ** 0.5
print("三角形三边分别为：a=",a,",b=",b,",c=",c)
print("三角形的面积=",s)
input(' ')