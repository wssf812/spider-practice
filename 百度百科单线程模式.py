import random
import re
import string
from urllib.parse import quote
from urllib import parse
import os
import requests
import time
# 单线程模式
header = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
          "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
          "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
          "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
          "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
          "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
          "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
          "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
          "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
          "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
def get_header():
    headers = {"User-Agent": random.choice(header),
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
               "Accept-Encoding": "gzip"}
    return headers
list = []
with open("D:\\PC\\pccode\\爬虫\\jiayou.txt", "r", encoding="utf-8") as  f:
    for i in f:
        html = open("D:\\PC\\pccode\\爬虫\\" + i.replace("\n", "") + ".txt", "r", encoding=u'utf-8',
                    errors='ignore').read().encode("utf-8").decode('utf-8-sig')
        # re.S不包含外侧双引号,下同)的作用扩展到整个字符串,
        pat = re.compile(r'<a.*?href="(.*?)"', re.S)
        links = pat.findall(html)
        for j in links:
            list.append(j)
list1=[]
for path in list:
    # 构建完整的绝对URL
    url = parse.urljoin("https://baike.baidu.com", path)
    list1.append(url)
list2 = []
# 判断网址
# pat1 = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
for k in list1:
    # 判断网址
    if re.match(r'^https|http?:/{2}\w.+$', k):
        list2.append(k)
url2=[]
# 网址去重
for zurl in set(list2):
  # 解决请求路径中含义中文或特殊字符
  url_ = quote(zurl, safe=string.printable);
  url2.append(url_)#第三层网址
print(len(url2))


list333=[]
list111=[]
list222=[]
list444=[]
url111=[]
def wangzhijiexi(a):
 try:
  for n,iaaa in url2:
   html = requests.get(iaaa,headers=get_header())
   html.encoding="utf-8"
   html1=html.text
   file2 = open("C:\\Users\\Dell\\Desktop\\reptileText\\" + str(n + a) + ".txt", "a", encoding='utf-8')
   file2.write(html1)
   print("成功")
   time.sleep(2)
   pat = re.compile(r'<a.*?href="(.*?)"', re.S)
   links = pat.findall(html1)
   for j in links:
     list111.append(j)
  for path in list111:
     url = parse.urljoin("https://baike.baidu.com", path)
     list222.append(url)
  for k in list222:
        # 判断网址
        if re.match(r'^https|http?:/{2}\w.+$', k):
            list444.append(k)
  # 去重
  for zurl in set(list444):
        # 解决请求路径中含义中文或特殊字符
      url_ = quote(zurl, safe=string.printable);
      if url_ in url2:
           print("和第三层网址重复")
      else:
          url111.append(url_)
  return url111
 except:
     print("网页执行错误")

ii=0
for file11 in os.listdir('C:\\Users\\Dell\\Desktop\\reptileText\\'):
    if int(file11[:-4])>int(ii):
        ii=file11[:-4]
print("你上次爬到",ii,"页，请从下一页开始爬")
a=input("请输入起始页：")
a=int(a)

for n,iaaa in wangzhijiexi(a):
   html = requests.get(iaaa,headers=get_header())
   html.encoding="utf-8"
   html1=html.text
   file3 = open("C:\\Users\\Dell\\Desktop\\reptileText1\\" + str(n + a) + ".txt", "a", encoding='utf-8')
   file3.write(html1)
   print("成功")


#一些网址集合
# urlaaa = ["https://baike.baidu.com/art",
#           "https://baike.baidu.com/science",
#           "https://baike.baidu.com/ziran",
#           "https://baike.baidu.com/wenhua",
#           "https://baike.baidu.com/dili",
#           "https://baike.baidu.com/shenghuo",
#           "https://baike.baidu.com/shehui",
#           "https://baike.baidu.com/renwu",
#           "https://baike.baidu.com/jingji",
#           "https://baike.baidu.com/tiyu",
#           "https://baike.baidu.com/lishi"]
