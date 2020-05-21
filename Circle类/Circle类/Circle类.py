#!/usr/bin/python
p = 3.14
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r*self.r*p
    def girth(self):
        return 2*p*self.r

for i in range(1,10):
    cir = Circle(i)
    print('半径为 %d 的圆' % i)
    print('面积为：%.2f' % cir.area())
    print('周长为：%.2f' % cir.girth())