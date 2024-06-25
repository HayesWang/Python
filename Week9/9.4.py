# 所谓孪生素数是指间隔为 2 的相邻素数，例如最小的孪生素数是3和5,5和7也是孪生数。
# 编写程序，求给定区间[m,n]中的孪生数的数量。例如[2,10]中的孪生数有(3,5)和(5,7)，
#则[2,10]中孪生数的数量为2.

# 输入：正整数m,n,    m,n>1.
# 输出：[m,n]中的孪生的数量
import math

def sushu(x):
    if (x <= 1):
        return False
    if (x == 2):
        return True
    if (x%2 == 0):
        return False
    for i in range(3,int(math.sqrt(x))+1,2):
        if (x%i == 0):
            return False
    return True

m , n = map(int,input().split(" "))
ctr = 0
for i in range(m,n+1):
    if (sushu(i-2) and sushu(i)):
        ctr+=1
print(ctr)