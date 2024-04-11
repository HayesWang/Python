# 输入一个字符串，删除串中的重复字符。
# 输入：要检查的字符串 例如：abacaeedabcdcd。
# 输出：  删除重复字符后的字符串。例如：abced。
a = input()
memory = [0]*99999
for i in range(0,len(a)):
    if memory[ord(a[i])-97] == 0:
        print(a[i],end="")
        memory[ord(a[i])-97]=1
