arr_old = [10 , 23 , 35 , 46 , 57 , 68 , 79 , 80 , 92 , 103 ]
print("原始数组是：")
print(arr_old)
arr = int(input("请输入一个新的数："))
ind = 0
ans = arr_old.copy()
for i in range(0,len(arr_old)):
    if arr < arr_old [i]:
        ans.insert(i,arr)
        break
print("插入新数后的数组是：")
print(ans)
