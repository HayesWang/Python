# 求n个数的最大公约数。其中：2<=n<50
# 输入：n个正整数，用空格隔开，在一行内输入。
# 输出：最大公约数和这n个数，分2行输出。
import math

a = input().split(" ")
l = [int(a[i]) for i in range(0,len(a))]
g=0
for i in range(0,len(l)):
    if i==0 :
        g=l[i]
    else:
        g=math.gcd(g,l[i])
print(g)
for i in range(0,len(l)):
    if i != len(l)-1:
        print(l[i],end=" ")
    else:
        print(l[i])
