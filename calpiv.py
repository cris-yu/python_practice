# 圆周率计算
from random import random
from time import perf_counter
darts = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1, darts+1):
    x, y = random(), random()
    dist = pow(x**2+y**2, 0.5)  # 开根号下X的平方+Y的平方
if dist <= 1.0:
    hits = hits+1
pi = 4*(hits/darts)  # 圆内的点/整个撒点数量
print("圆周率值是：{:}".format(pi))
print("运行时间是：{:.2f}s".format(perf_counter()-start))
