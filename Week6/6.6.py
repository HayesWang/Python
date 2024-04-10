# 求a+aa+aaa+aaaa+…+aa...a（n个），其中a为1～9之间的整数。
# 例如：当a = 1, n = 3时，求1+11+111之和为123；
# 输入：组成序列的数字a和求和项的数量n
# 输出：算式和结果
a,n=input().split(" ")
a=int(a)
n=int(n)
sum=0
for i in range(0,n+1):
    for j in range(0,i):
        sum+=a*pow(10,j)
        print(a,end="")
    if i != 0 and i != n:
        print("+",end="")
print("=",end="")
print(sum)