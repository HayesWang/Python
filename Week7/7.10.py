# 单词加密。输入一个字符串和一个非负整数k，对字符串中的每一个字母，
# 用字母表中其后的第k个字母代替，不够k个时再从字母a循环计数。
# 例如k=3是，a用d代替，A用D代替，x用a代替，y用b代替，保持大小写不变。
# 字符串中的非字母字符不变。字符串的长度不超过100。
# 输入：一个字符串（无空格）和非负整数k，之间用空格分隔
# 输出：加密的字符串。

def encrypt(s, k):
    res = ''
    for c in s:
        if c.isalpha():
            if c.islower():
                res += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
            else:
                res += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            res += c
    return res

s, k = input().split()
k = int(k)
print(encrypt(s, k))

