#给出一段文本，统计其中出现的词汇个数，统计对象以名词为主，
#连词副词形容词等准备在stop.txt，用于跳过统计
with open('../../data/阿Q正传.txt','r',encoding='utf8') as novelFile:
    novel = novelFile.read()

#分词工具 ：jieba
import jieba
novelList = list(jieba.lcut(novel))

#加载停用词
stops=[line.strip() for line in open('../../data/stop.txt','r',encoding='utf8').readlines()]
countDict={}

for word in novelList:
    if word not in stops:
        if len(word)==1: #长度为一不记录
            continue
        else:
            countDict[word]=countDict.get(word,0)+1

itemlist=list(countDict.items())
itemlist.sort(key = lambda s:s[1],reverse=True)
for word in itemlist[:10]:
    print(word)


#词云
from wordcloud import WordCloud,ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
import cv2


#读入背景图片 形状相同
bg_pic = cv2.imread(r'../../img/SatomiIshihara.jpg.jpg')
#生成词云图片
wordcloud = WordCloud(mask=bg_pic,background_color='white',
    scale=1.5,font_path=r'../../data/msyh.ttc').generate(' '.join(countDict.keys()))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
#保存图片
wordcloud.to_file('../../img/阿Q正传.jpg')