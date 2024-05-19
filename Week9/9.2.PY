# 输入两个字符串s, t，(字符串中没有空格，包含大小写字母、数字以及其他符号）
# 按从小到大顺序输出在s或t中出现过(不区分大小写)的所有字符，所有字母均按大写输出
# 重复的字符只输出1次。
# 输入：1行，两个字符串中间用空格隔开，字符串不含空格
# 输出：结果字符串，按ASCII编码从小到大排序。

s,t = input().split(" ")
s=s.upper()
t=t.upper()
dic=[0]*128
for i in range(0,len(s)):
    dic[ord(s[i])]=1

for i in range(0,len(t)):
    dic[ord(t[i])]=1

for i in range(0,128):
    if dic[i]==1:
        print(chr(i),end="")

