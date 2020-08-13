# coding=UTF-8
#---------- list ----------
list1 = [1,2,3,4,5,6]
print(list1[-1])  # 串列取值可以為負值(-1取出最後一個(5))

# append (附加)，extend(延伸)，insert(插入)，pop(拋出)
# append 可以是元素也可以是串列，append 會將串列當成一個元素加入list
list2 = [1,2,3,4,5,6]
list1.append(7) #list2 = [1,2,3,4,5,6,7]
list1.append([8,9]) #list2 = [1,2,3,4,5,6,7,[8,9]]
# extend 只能是串列
list3 = [1,2,3,4,5,6]
list3.extend([8,9]) #list3 = [1,2,3,4,5,6,8,9]
# insert 指定串列新增位置，索引超過串列大小放最後
list4 = [1,2,3,4,5,6]
list4.insert(1,55) # [1, 55, 2, 3, 4, 5, 6]
[1, [10, 11], 55, 2, 3, 4, 5, 6]
list4.insert(1,[10,11]) # [1, [10, 11], 55, 2, 3, 4, 5, 6]
# pop 無參數，取出最後一個。有參數，取出指定元素
list5 = [1,2,3,4,5,6]
list5.pop() # [1, 2, 3, 4, 5]
list5.pop(1) # [1, 3, 4, 5]

#---------- tuple函式 ----------
# tuple元組，結構與list相同，但其不能修改(不能修改的list)
# 優點 : 比list快。 資料較為安全(不能更改)

# list 與 tuple 轉換
tuple11 = (1,2,3,4,5,6)
list11 = list(tuple11)

list12 = [1,2,3,4,5,6]
tuple12 = tuple(list12)


#---------- range函式 ----------
ra = range(5) # 0~4
print(list(ra))
# 變數 = range(起始值, 終止值)
rb = range(3,8) 
print(list(rb)) # 3~7 包含頭不含尾
# 變數 = range(起始值, 終止值, 間隔值)  間隔值可為負
rb1 = range(3,8,2)
print(list(rb1)) # [3, 5, 7]
rb2 = range(8,3,-2)
print(list(rb2)) # [8, 6, 4]

# python 的for 更像是foreach
for i in range(1,10):
    for j in range(1,10):
        ans = i * j
        print('%2dx%2d = %-2d   '%(i, j, ans), end='')
    print()
wh1 = 1
while(wh1 < 10):
    wh2 = 1
    while(wh2 < 10):
        whans = wh1 * wh2
        print('%2dx%2d = %-2d   '%(wh1, wh2, whans), end='')
        wh2+=1
    print()  
    wh1+=1








