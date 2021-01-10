# 从csv格式的文件中读入数据
'''fo open("ls.csv")
ls = []
for line in fo:
    line = line.replace("\n", "")
    ls.append(line.split(","))
fo.close()

# 将数据写入csv格式的文件
ls = [[], [], []]  # 二维列表
f = open(fname, 'w')
for item in ls:
    f.write(','.join(item)+'\n')
f.close()'''

# 二维数据逐一处理
ls = [[1, 2], [3, 4], [4, 5]]
for row in ls:
    for column in row:
        print(column)
