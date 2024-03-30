# 从键盘输入任意3个整数，然后输出这3个数的平均值。
# 输入：3个整数，用空格分隔。
# 输出：平均数（实数）。

a=input()
sum=0
for i in a.split(" "):
    sum+=int(i)
print(sum/3)