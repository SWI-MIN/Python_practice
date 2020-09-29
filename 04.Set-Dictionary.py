# 集合的運算
# 變數名稱 = {值1,值2,值3}
s1={1,2,3}
s2={3,4,5}
print(3 in s1)         # 3在集合裡  T or F
print(3 not in s1)     # 3不在集合裡  T or F

print(s1 & s2)       # 交集
print(s1 | s2)       # 聯集
print(s1 - s2)       # 差集
print(s1 ^ s2)       # 反交集XOR  連集減交集  (s1|s2)-(s1&s2)

s=set("你打我撒~WWWWWWWWWWWWWWWW")    # 把字串中的字母拆解成 Set，重複的只會取一個
print(s)
print('你' in s)

print('-------------------------------------')

# 字典的運算
# Dictionary 字典
# 變數名稱 = {'鍵':'值'}
dic={"apple":"蘋果",'DATA':'資料',"bug":"蟲蟲"}
print(dic)
print(dic['apple'])
dic["apple"]="小小小蘋果" # 更新
print(dic['apple'])
dic['School'] = "FCU" # 添加
print(dic)
print('apple' in dic)
print('apple' not in dic)
del dic['DATA']
print(dic)

print('-------------------------------------')

# dic={x:x*2 for x in 列表}     從列表的資料產生字典
dic={x:x*2 for x in [3,4,5]}
print(dic)


