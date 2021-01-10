import wordcloud
txt = "life is short you need python"
w = wordcloud.WordCloud(background_color="black")
w.generate(txt)
w.to_file("balckcloud.png")
