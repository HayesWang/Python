# 输入总秒数，转换为相应的时、分、秒。
# 输入：整数
# 输出：时分秒，整数，西文冒号分隔
# 样例
# 输入：3661
# 输出：1:01:01
# 格式提示：
# print(f'{hours}:{minutes:0>2}:{seconds:0>2}')

t=int(input())
hours=t//3600
t=t-hours*3600
minutes=t//60
t=t-minutes*60
seconds=t
print(f'{hours}:{minutes:0>2}:{seconds:0>2}')