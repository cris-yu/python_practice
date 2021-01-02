# singlebranch
'''guess = eval(input())
if guess == 99:
    print("恭喜你猜对了")

# doublebranch
guess = eval(input())
if guess == {1, 99}:
    print("恭喜你猜对了")
else:
    print("请重新输入")

# 二分支紧凑表达方式
guess = eval(input())
print("猜{}了".format("对"if guess == 99 else"错"))'''

# 多分支结构 if elif else
score = eval(input())
if score >= 60 and score < 70:
    grade = "D"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 90 and score <= 100:
    grade = "A"
else:
    print("成绩不合格")
print("输入的成绩等级为{}".format(grade))
