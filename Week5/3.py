# 请输入一个不含0的8位的十进制整数，编写程序取出该整数的中间4位数，
# 分别输出取出的这4位数以及该4位数加上1024的得数。
# 输入：一个整数。
# 输出：两个整数，用空格分隔。

x=int(input())
x=x/100
x=x%10000
print(int(x),int(x+1024))