import requests
import xml2ass
aid = input('请输入aid:')
r = requests.get("https://www.bilibili.com/widget/getPageList?aid=" + aid)
print(eval(r.text))
for i in eval(r.text):
    dict = i
cid = dict['cid']
print(cid)
danmuku = requests.get('https://comment.bilibili.com/' + str(cid) + '.xml')
danmuku.encoding = 'utf-8'
print(type(danmuku.text))
with open('./danmu.xml', 'w',encoding = 'utf-8') as file:
    file.write(danmuku.text)
file.close()
xml2ass.Danmaku2ASS('danmu.xml','danmu.ass',1920,540)


