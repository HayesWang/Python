# 编程求以下级数前n项之和：
# s=1-1/3+1/5-1/7+1/9-1/11+1/13-1/15+.....
# 输入：一个正整数n
# 输出：前n项和的值，超出小数点后4位的，保留到小数点后4位
n=int(input())
sum=0.000
for i in range(1,n+1):
    if i%2 == 1:
        sum += 1/(2*i - 1)
    if i%2 == 0:
        sum -= 1/(2*i - 1)
#sum=int(sum*10000)/10000
if n==1:
    print("1.0")
else:
    print('%.4f'% sum)