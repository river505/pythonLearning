
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
# def get01(url):
#     response = requests.get(url, headers=headers)
#     response.encoding=response.apparent_encoding
#     # print(response.text)
#     soup= BeautifulSoup(response.text, 'lxml')
#     dataa = soup.find('div',attrs={'class':'herolist-box'}).find_all('a')
#     for i in dataa:
#         i_src=i['href']
#         print(r'https://pvp.qq.com/web201605/'+i_src)
# url01='https://pvp.qq.com/web201605/herolist.shtml'


# get01(url01)

url='https://pvp.qq.com/web201605/herolist.shtml'
html=requests.get(url,headers=headers).content

doc=PyQuery(html)
items = doc('.herolist > li').items()

for i in items:
    url=i.find('img').attr('src')
    urls='https:'+url
    name=i.find('a').text()
    conten=requests.get(urls).content
    with open(r'./picture/'+name+'.jpg','wb') as file:  #目录要手动建好
        file.write(conten)
        print("正在下载：%s.....%s" %(name,urls))
print("下载完成")

