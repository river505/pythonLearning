import requests

url =  'https://www.douyin.com/video/7117652393600306462'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
}

response = requests.get(url,headers=headers)
response.encoding=response.apparent_encoding
print(response.text)

