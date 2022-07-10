import requests
import os
import time
from bs4 import BeautifulSoup
from pyquery import PyQuery
headers={
# 'Accept':'image/avif,image/webp,*/*',
#
# 'Accept-Encoding':'gzip, deflate, br',
#
# "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
# "Connection":"keep-alive",
# "Host":"t1.huishahe.com",
# "Referer":"https://www.mmonly.cc/",
# "Sec-Fetch-Dest":"image",

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
url01='http://v26-web.douyinvod.com/a661dd2cd10c6e062024032b5a1145a8/62c960c8/video/tos/cn/tos-cn-ve-15c001-alinc2/61a7a8e365ca471aaa8ef7a94669ee3e/?a=6383&ch=42&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=1342&bt=1342&cs=0&ds=3&ft=X1nbLXvvBQSqU88ZJ8Z.BOMzJ4lcBas2F2bLPosHiiZm&mime_type=video_mp4&qs=0&rc=OjNmOWhlZjc8N2VlOjQ4N0BpMzc2b2c6ZnRtZDMzNGkzM0AtMl4xYDYxNTMxX18zMzMzYSNpZGoxcjRnNGtgLS1kLTBzcw%3D%3D&l=2022070918043401021206816133604370'

conten = requests.get(url01).content
with open(r'./douyin/床板.mp4', 'wb') as file:  # 目录要手动建好
    file.write(conten)


