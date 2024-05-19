# 输入公元年份和月份，输出该月份的天数。
# 输入：年，月（逗号分隔）
# 输出：天数

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

def days_of_month(year, month):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30
    
year, month = map(int, input().split(","))
print(days_of_month(year, month))
