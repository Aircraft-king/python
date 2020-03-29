s=int(input('请输入一个三位数：'))
q=int(s/100)
b=int(s/10)-q*10
g=s-100*q-b*10
s=q*q*q+b*b*b+g*g*g
print('立方和:')
print(s)
input('pause')