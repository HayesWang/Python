# 编写一个程序，读入n个用户姓名和电话号码，按姓名的字典顺序排列后，
# 输出用户的姓名和电话号码，n从键盘输入。
# 样例：
# 输入：
# 3
# zhang 122
# wang 233
# li 567
# 输出：
# li 567
# wang 233
# zhang 122

n = int(input())
list = {}
for i in range(0, n):
    name, phone = input().split(" ")
    list[name] = phone

for key in sorted(list.keys()):
    print(key, list[key])