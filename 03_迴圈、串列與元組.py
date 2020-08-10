# coding=UTF-8
#---------- list ----------
list1 = [1,2,3,4,5]
print(list1[-1])  # 串列取值可以為負值(-1取出最後一個(5))

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









