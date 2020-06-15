import requests
import xml2ass
url = input('输入视频链接：')
bv = url[len('https://www.bilibili.com/video/'):]
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
a = requests.get('http://api.bilibili.com/x/web-interface/archive/stat?bvid='+ bv, headers = headers)
dict_aid = eval(a.text)
aid = dict_aid['data']['aid']
# print(aid)
r = requests.get("https://www.bilibili.com/widget/getPageList?aid=" + str(aid),headers = headers)
#print(eval(r.text))
for i in eval(r.text):
    dict = i
cid = dict['cid']
#print(cid)
danmuku = requests.get('https://comment.bilibili.com/' + str(cid) + '.xml',headers = headers)
danmuku.encoding = 'utf-8'
#print(type(danmuku.text))
with open('./danmu.xml', 'w',encoding = 'utf-8') as file:
    file.write(danmuku.text)
file.close()
xml2ass.Danmaku2ASS('danmu.xml','danmu.ass',1920,540)

