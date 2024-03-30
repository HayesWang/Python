# 输入整数a和b，若a*a+b*b大于等于100，则输出a*a+b*b百位及以上的数字，
# 否则输出a*a+b*b。例如，输入25 25 ，它们的平方和为625+625=1250，百位及以上数为12.
# 输入：两个整数，中间用空格隔开
# 输出：一个整数。
a, b = input().split(' ')
a = int(a)
b = int(b)
sum = int(a * a + b * b)
if sum >= 100:
    print(int(sum / 100))
else:
    print(sum)
