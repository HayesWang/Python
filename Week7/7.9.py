# 求一组数(整数数组)中的最大值，然后统计该最大值在这组数中出现的次数。
# 输入：n个整数。n<200。
# 输出：最大值及出现的次数。数据间以一个逗号隔开。

lis = list(map(int, input().split(" ")))
max = int(sorted(lis)[-1])
# print(lis)
count = 0
for i in range(0, len(lis)):
    if int(lis[i]) == max:
        count += 1
print(max, count, sep=",")
