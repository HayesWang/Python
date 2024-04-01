# 计算银行存款本息。输入存款金额money（单位：元），存期years，
# 年利率rate，计算到期存款本息（保留2位小数）。计算公式如下：
# sum=money*((1+rate)^years)
# 输入:存款金额，存期，年利率。均为浮点数，且用逗号分隔
# 输出：存款本息（保留2位小数）
money , years , rate = input().split(",")
money=float(money)
years=float(years)
sum=money*((1+float(rate))**years)
sum=int(sum*100000)/100000
print("%.2f"%sum)