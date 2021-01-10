import jieba
import wordcloud
txt = "这个世界上绝大多数的情绪问题都可以靠「早睡早起」「努力工作」「看书」和「做运动」解决。人就是这样，总会遇到这样那样的破事，"
w = wordcloud.WordCloud(width=1000, height=700,
                        font_path="chinesecloud/MSYHBD.TTC")
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("1.png")
