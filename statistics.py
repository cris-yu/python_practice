# 获取用户输入
def getnum():
    nums = []
    inumstr = input("press number(press enter to exit)")
    while inumstr != "":
        nums.append(eval(inumstr))
        inumstr = input("press number(press enter to exit)")
    return nums

# 计算平均值


def mean(numbers):
    s = 0.0
    for nums in numbers:
        s = s+nums
    return s/len(numbers)

# 计算方差


def dev(numbers, mean):
    sdev = 0.0
    for nums in numbers:
        sdev = sdev+(nums-mean)**2
    return pow(sdev/(len(numbers)-1), 0.5)

# 计算中位数


def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1]+numbers[size//2]/2)
    else:
        med = numbers[size//2]
    return med


n = getnum()
m = mean(n)
print("平均值:{},方差:{:.2}中位数:{}.".format(m, dev(n, m), median(n)))
