# 写出正整数的三位分节格式。如，当用户输入82668634时，程序应该输出82,668,634。
# 输入：正整数
# 输出：三位分解格式。
# 样例：
# 82668634
# 82,668,634
s=input()
ctr=0
ctr=len(s)%3
for i in range(0,len(s)):
    if i !=len(s)-1 and ctr==0 and i!=0:
        print(",",end=(''))
        ctr=3
    if ctr==0 and i==0:
        ctr=3
    print(int(s[i]),end=(''))
    ctr=ctr-1

