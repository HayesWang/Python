# 输入一个字符串（不包含空格，至少有1个字符），除首尾字符外，

# 将其余的字符按ascii码降序排列，然后输出。

s=input()
s1=sorted(s[1:-1],reverse=True)
if len(s1)<=2:
    print(s)
else:
    print(s[0]+"".join(s1)+s[-1])
