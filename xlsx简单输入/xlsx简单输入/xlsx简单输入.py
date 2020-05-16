import xlwt
from datetime import datetime


wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 'S09')
ws.write(0, 1, '女')
ws.write(0, 2, '89.2')
ws.write(0, 3, '88.4')
ws.write(0, 4, '86')
ws.write(0, 5, '87.9')
ws.write(1, 0, 'S10')
ws.write(1, 1, '女')
ws.write(1, 2, '90.5')
ws.write(1, 3, '86.3')
ws.write(1, 4, '87')
ws.write(1, 5, '87.9')
ws.write(2, 0, 'S11')
ws.write(2, 1, '男')
ws.write(2, 2, '88.7')
ws.write(2, 3, '89.4')
ws.write(2, 4, '89')
ws.write(2, 5, '89.0')

wb.save('ex06.xls')