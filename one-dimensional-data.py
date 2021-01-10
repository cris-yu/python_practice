# 从空格分隔的文件中读入数据
txt = open("fname.txt").read()
ls = txt.split()
ls.close()

# 从特殊符号分隔的文件中读入数据
txt = open("fname.txt").read()
ls = txt.split("$")
ls.close()

# 从空格分隔的文件中写入数据
ls = ['中国', '美国', '日本']
f = open(ls, 'w')
f.write(' '.join(ls))
f.close()

# 从特殊符号分隔的文件中读入数据
ls = ['中国', '美国', '日本']
f = open(ls, 'w')
f.write('$'.join(ls))
f.close()
