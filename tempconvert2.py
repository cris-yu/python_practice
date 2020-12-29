tempstr = input()
if tempstr[-1] in ['F', 'f']:
    C = (eval(tempstr[0:-1]-32)/1.8)
    print("{:.2f}C".format(C))
elif tempstr[-1] in ["c", "C"]:
    F = 1.8*eval(tempstr[0:-1]+32)
    print("{:.2f}F".format(F))
else:
    print("输入格式错误")
