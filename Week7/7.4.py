# 编写程序，找出[m,n]范围内是7的倍数或带7的全部正整数(注意：如果一个是既是7的倍数又是带7的数，
# 就输出2次，先输出倍数，再输出带7的整数，如：7 is a multiple of 7 7 contains 7)。
# 其中，m和n为正整数。
# 样例
# 1 20
# 7 is a multiple of 7
# 7 contains 7
# 14 is a multiple of 7
# 17 contains 7

m,n=input().split(" ")
m=int(m)
n=int(n)

def ismultiple7(n):
    if n % 7 == 0:
        return True
    else:
        return False
def iscontains7(n):
    s = str(n)
    for i in range(0, len(s)):
        if s[i] == "7":
            return True
    return False

for i in range(m,n+1):
    if ismultiple7(i):
        print(i,"is a multiple of 7")
    if iscontains7(i):
        print(i,"contains 7")