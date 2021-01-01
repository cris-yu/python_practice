# weeknameprint
weekstr = "周一周二周三周四周五周六周日"
weekid = eval(input("请输入数字（1-7）："))
pos = (weekid-1)*2
print("today is " + weekstr[pos:pos+2])
