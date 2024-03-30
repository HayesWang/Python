# 编写程序，输入任意的3个小数；将这3个小数相加，
# 将相加的结果以及按四舍五入方法转换成整数后的结果显示输出。
# 输入：3个小数，空格分隔；
# 输出：和，四舍五入后的整数，1行显示，空格分隔。
a=float(input())
b=float(input())
c=float(input())
sum=a+b+c
print(sum,end=' ')
if sum%1 >= 0.5:
    print(int(sum)+1)
else:
    print(int(sum))
