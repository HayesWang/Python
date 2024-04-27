# 从键盘输入一个正整数（>1)，然后将该整数分解为1和各个质因子的相乘，
# 如果输入的整数本身就是质数，则应分解为1和该数本身相乘。
# 18
# 1*2*3*3
n = int(input())
list = []
list.append(1)
while n > 1:
    for i in range(2, n + 1):
        if n % i == 0:
            list.append(i)
            n = n // i
            break
for i in range(0, len(list)):
    print(list[i], end="")
    if i != len(list) - 1:
        print("*", end="")

