USD_VS_RMB = 6.7
rmb_value = 0
rmb_str_value = input('请输入人民币（CNY）：')
print('你输入的人民币是：' + rmb_str_value)
try:
    rmb_value = eval(rmb_str_value)
except:
    print('请输入数字！')
else:
    usd = rmb_value / USD_VS_RMB
    print('对应的美元是：', format(usd, '0,.15f'))
    input('pause')
