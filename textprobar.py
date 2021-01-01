# 文本进度条1
'''import time
scale = 50
print("------执行开始-----")
for i in range(scale+1):
    a = '■' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    print("\r{:>.3f}%[{}{}]".format(c, a, b), end="")  # \r表示不换行
    time.sleep(0.1)
print("------执行结束-----")'''

# 文本进度条2
import time
scale = 50
print("执行开始".center(scale//2, "-"))
Start = time.perf_counter()
for i in range(scale+1):
    a = '■' * i
    b = '.' * (scale-i)
    c = (i/scale)*100
    dur = time.perf_counter()-Start
    print("\r{:^.3f}%[{}{}]{:.2f}s".format(
        c, a, b, dur), end="")  # \r   end=""  表示不换行
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, "-"))  # \n表示另起一行
