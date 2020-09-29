# List 有順序、可動列表
numlist=[3,4,5,6,7]
print(numlist)          
print(numlist[1])       # 取表中第一個資料
numlist[1]=44444444     # 更新表資料
print(numlist)
print(numlist[1:4])     # 取表中第1個到第4個資料，包含頭不包含尾
numlist[1:4]=[]         # 刪除中第1個到第4個資料，包含頭不包含尾
print(numlist)        
numlist=numlist+[8,9]   # 列表串接
print(numlist)        
numlist+=[8,9]          # 列表串接
print(numlist) 

length=len(numlist)
print(length)           # 取得列表長度  做法1
print(len(numlist))     # 取得列表長度  做法2

# 二維
numlist=[[0,1,2],[0,1,2]]

#################################################################

# Tuple 有順序、不可動列表
numtuple=(3,4,5,6,7)

# list 跟 tuple 的差別只在於tuple不可變動