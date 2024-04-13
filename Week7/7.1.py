# 去掉一个字符串中除头部和尾部空格外的所有空格。
# 样例：
#    abc  de
#    abcde
a=input().split(" ")
for i in range(0,len(a)):
    print(a[i],end="")