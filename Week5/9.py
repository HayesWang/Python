# 输入任意一个正整数，计算各位数字的平方和。
# 如：1234 则：计算1*1+2*2+3*3+4*4=30
# 输入：一个正整数
# 输出：平方和

a=int(input())
s=str(a)
sum=0
for i in range(0,len(s)):
    sum+=int(s[i])**2
print(sum)
