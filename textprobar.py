# 文本进度条
import time
scale = 50
print("------执行开始-----")
for i in range(scale+1):
    a = '■' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    print("\r{:>.3f}%[{}{}]".format(c, a, b), end="")  # \r表示不换行
    time.sleep(0.1)
print("------执行结束-----")
