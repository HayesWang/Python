# 编程判断任意一个正整数各位数字之和是奇数还是偶数。
# 如果和是奇数输出1，偶数输出0
x = input()
sum = 0
for i in range(0,len(x)):
    sum += int(x[i])
if sum % 2 == 0:
    print("0")
else:
    print("1")