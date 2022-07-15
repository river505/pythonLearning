import requests
import re
import pandas as pd

url = 'https://pvp.qq.com/web201605/herolist.shtml'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
r = response.text

wangzhi = re.compile(r'<a href="herodetail/(\d*).shtml" target="_blank"')
hero_xuhao_list = re.findall(wangzhi, r)
df = []
columns = ['英雄', '被动', '技能1', '技能2', '技能3', '技能4']
for id in hero_xuhao_list:
    detail_url = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(id)

    response1 = requests.get(detail_url, headers=headers)
    response1.encoding = response1.apparent_encoding

    names = re.compile('<label>(.*?)</label>')
    name = names.findall(response1.text)[0]
    # 没有这个[0]，会使得excel中的数据是['云中君']，即中文名外面还有引号和[]
    skills = re.compile('<p class="skill-desc">(.*?)</p>', re.S)
    skill = skills.findall(response1.text)
    beidong = skill[0]
    jineng1 = skill[1]
    jineng2 = skill[2]
    jineng3 = skill[3]
    jineng4 = skill[4]
    b = df.append([name, beidong, jineng1, jineng2, jineng3, jineng4])
    d = pd.DataFrame(df, columns=columns)
    d.to_csv("王者荣耀英雄与技能.csv", index=False)
