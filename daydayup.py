# daydayupQ1
'''dayup = pow(1.001, 365)
daydown = pow(0.999, 365)
print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))'''

# daydayupQ2  引入变量
'''dayfactor=0.01
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup, daydown))'''

# daydayupQ3  引入模运算  抽象+自动化
'''dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6, 0]:  # 判断在休息日
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print("工作日的力量: {: .2f}, ".format(dayup))'''

# daydayupQ4


def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:  # 判断在休息日
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup


dayfactor = 0.01
while dayup(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是: {: .3f},".format(dayfactor))
