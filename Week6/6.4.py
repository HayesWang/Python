# 编写程序检验由三边能否构成三角形，检验方法是任意两边和均要大于第三边。
# 输入:三边长度（一行输入，空格分隔）
# 输出：如果可以构成三角形，输出YES，否则输出ERROR DATA
a = input().split(" ")
a.sort()
if float(a[0]) + float(a[1]) > float(a[2]):
    print("YES")
else:
    print("ERROR DATA")

