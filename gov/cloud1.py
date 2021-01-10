# 生成词云
'''import jieba
import wordcloud
f = open("gov/新时代中国特色社会主义.txt", "r", encoding="utf-8")
excludes = {"和", "的", "是", "在"}
t = f.read()

f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="gov/MSYH.TTC",
                        width=1000, height=700, background_color="white", stopwords=excludes, max_words=200)  # stopwords禁止显示某些词
w.generate(txt)
w.to_file("cloud1.png")'''

# 生成有形状的词云
import jieba
import wordcloud
from imageio import imread
mask = imread("gov/bitlogo.png")  # 引入词云形状
f = open("gov/新时代中国特色社会主义.txt", "r", encoding="utf-8")
excludes = {"和", "的", "是", "在"}
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="gov/MSYH.TTC",
                        width=1000, height=700, background_color="white", stopwords=excludes, max_words=200, mask=mask)  # stopwords禁止显示某些词
w.generate(txt)
w.to_file("cloud2.png")
