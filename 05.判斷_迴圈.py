###########判斷###########
# if 條件:
#     條件成立做這事，不成立往下
# elif 條件:
#     條件成立做這事，不成立往下
# else:
#     以上條件都不成立做這事

x=input("請輸入數字")
x=int(x)        # 轉型態
if x>100:
    print("超過100")
elif x>50:
    print("超過50")
else:
    print("小於50")

###########迴圈###########
# while
# for
# while + for OR for + while
####控制迴圈####
# break 	    终止迴圈，並且跳出整個迴圈
# continue    终止當前迴圈，跳出此次迴圈，執行下一次迴圈
# pass        pass是空語句，是為了保持程式结構的完整

numbers = [12,37,5,42,8,3]
even = []
odd = []
while len(numbers) > 0 :
    print(numbers)
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
        print(even)
        print(odd)
    else:
        odd.append(number)
        print(even)
        print(odd)

##################################   
for numm in range(10,20):  #  印出 10 到 20 之间的数字(含頭不含尾)
    print(numm)

##################################
for num in range(10,20):  # 迭代 10 到 20 之间的数字
    for i in range(2,num): # 根据因子迭代
        if num%i == 0:      # 确定第一个因子
            j=num/i          # 计算第二个因子
            print ('%d 等于 %d * %d' % (num,i,j))
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
          print (num, '是一个质数')
