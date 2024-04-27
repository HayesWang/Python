# 去掉一个字符串中除头部和尾部空格外的所有空格。
# 样例：
#    abc  de
#    abcde
a = input()
firstletter = 0
lastletter = 0
for i in range(0,len(a)):
    if a[i] != " " and firstletter == 0:
        firstletter = i
    if a[i] != " ":
        lastletter = i

for i in range(0,firstletter):
    print(a[i],end="")
for i in range(firstletter,lastletter+1):
    if a[i] != " ":
        print(a[i],end="")
for i in range(lastletter+1,len(a)):
    print(a[i])