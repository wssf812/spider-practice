import requests
# from urllib.request import Request
import queue
import threading
import random
import re
from urllib import parse
# from bs4 import BeautifulSoup
import time
import os
from urllib.parse import quote
import string

# 多线程模式
# file = open("D:\\PC\pccode\\爬虫\\sousuowangzhi.txt","a+",encoding='utf-8')
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
# 第二层和第三层网址
with open("D:\\PC\\pccode\\爬虫\\jiayou.txt", "r", encoding="utf-8") as  f:
    for i in f:
        html = open("D:\\PC\\pccode\\爬虫\\" + i.replace("\n", "") + ".txt", "r", encoding=u'utf-8',
                    errors='ignore').read().encode("utf-8").decode('utf-8-sig')
        # re.S不包含外侧双引号,下同)的作用扩展到整个字符串,
        pat = re.compile(r'<a.*?href="(.*?)"', re.S)
        links = pat.findall(html)
        for j in links:
            list.append(j)
list2 = []
for path in list:
    url = parse.urljoin("https://baike.baidu.com", path)
    list2.append(url)
# 判断网址
# pat1 = re.compile(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]')
list3=[]
for k in list2:
    # 判断网址
    if re.match(r'^https|http?:/{2}\w.+$', k):
        list3.append(k)
url2=[]
# 网址去重
for zurl in set(list3):
  # 解决请求路径中含义中文或特殊字符
  url_ = quote(zurl, safe=string.printable);
  url2.append(url_)
print(len(url2))

# 创建队列python3貌似没有Queue模块,变成小写的queue
queue1 = queue.Queue()
# 判断次数
count=0
list444=[]
list333=[]
list111=[]
list222=[]
list555=[]
endurllist=[]
url111=[]
# 第四层url
for file11 in os.listdir('C:\\Users\\Dell\\Desktop\\reptileText\\'):
     with open("C:\\Users\\Dell\\Desktop\\reptileText\\"+str(file11),"r", encoding='utf-8') as nf:
            pat2 = re.compile(r'<a.*?href="(.*?)"', re.S)
            links2 = pat2.findall(nf.read().encode("utf-8").decode('utf-8-sig'))
            for j2 in links2:
                list111.append(j2)
for path in list111:
    # 获取url绝对路径地址，有的话就不变，没有就默认
    url = parse.urljoin("https://baike.baidu.com", path)
    list222.append(url)
for k2 in list222:
    # 判断网址
    if re.match(r'^https|http?:/{2}\w.+$', k2):
        list444.append(k2)
        # 去重
for zurl2 in set(list444):
        # 解决请求路径中含义中文或特殊字符
        url_ = quote(zurl2, safe=string.printable)
        if url_ in url2:
             print("和第三层网址重复")
        else:
            url111.append(url_)
print(len(url111))

# 第五层url
listfive=[]
listfive2=[]
listfive3=[]
fiveurl=[]
for five in os.listdir("D:\\text3\\"):
        with open("D:\\text3\\"+str(five),"r",encoding="utf-8") as fivefile:
            pat3 = re.compile(r'<a.*?href="(.*?)"', re.S)
            links3 = pat3.findall(fivefile.read().encode("utf-8").decode('utf-8-sig'))
            for j3 in links3:
                listfive.append(j3)
for path in listfive:
    url = parse.urljoin("https://baike.baidu.com", path)
    listfive2.append(url)
for k3 in listfive2:
    # 判断网址
    if re.match(r'^https|http?:/{2}\w.+$', k3):
        listfive3.append(k3)  # 去重
for zurl3 in set(listfive3):
    # 解决请求路径中含义中文或特殊字符
    url_ = quote(zurl3, safe=string.printable);
    if url_ in url111 or url_ in url2:
         print("和第三层，第四层网址重复")
    else:
        fiveurl.append(url_)
print(len(fiveurl))
# 将第五层网址写入到文件中
with open(r"D:\fiveurl.txt", "a+", encoding="utf-8") as fivenet:
     for fivelist in fiveurl[0:]:
            fivenet.write(fivelist+"\n")
print("成功")

class ThreadUrl(threading.Thread):
    def __init__(self, queue1):
        threading.Thread.__init__(self)#调用父类构造方法
        # super().__init__()
        self.queue1 = queue1
    # 面向对象的线程中必须实现run方法
    def run(self):
        while not self.queue1.empty():
            try:
                host = self.queue1.get()
                r = requests.get(host, headers=get_header(),timeout=300)
                r.encoding = 'utf-8'
                html1 = r.text
                time.sleep(0.5)
                with open("C:\\Users\\Dell\\Desktop\\endurl.txt","a",encoding="utf-8") as endfile:
                     endfile.write(host+"\n")
                global count
                time.sleep(0.5)
                count = count + 1
                with open("C:\\Users\\Dell\\Desktop\\text4\\"+str(count)+".txt" , "a+", encoding="utf-8") as nfiles:
                    nfiles.write(html1)
                    print("成功"+str(count))
                self.queue1.task_done()
            except:
                 print("网址无法运行"+str(count))
for host in url111[0:]:
    with open("C:\\Users\\Dell\\Desktop\\endurl.txt","r",encoding="utf-8") as endf:
        if host in endf.read():
            print("已经爬取了")
        else:
            queue1.put(host)
# 开启线程（10个）
for i in range(10):
    thread = ThreadUrl(queue1)
    thread.setDaemon(True)
    thread.start()
# 等待所有线程完成
queue1.join()
print("结束")



# 当把所有的网址全部爬去下来后用这个函数去除百度百科首页
def endquchong():
  html2 ="<title>百度百科_全球最大中文百科全书</title>"
  dirfile = "C:\\Users\\Dell\\Desktop\\reptileText"
  liebiao = []
  for files in os.listdir(dirfile):
     with open("D:\\text3\\"+files,"r",encoding="utf-8") as file:
        if html2 in file.read():
            print("ssss"+files)
            liebiao.append(files)
  for name in liebiao:
     os.remove("D:\\text3\\"+name)
     print("删除成功")

















































