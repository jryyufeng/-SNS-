# -*-coding:utf-8-*- 
from bs4 import BeautifulSoup
import urllib2,urllib
import re

# headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, li'
#                           'ke Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
def zht(url,x,a,b,c):
    global content
    req=urllib2.Request(url,headers=headers)
    try:
        content=urllib2.urlopen(req,timeout=80).read()
    except Exception,e:
        #print 'time out'+a+b+c
        pass
    soup=BeautifulSoup(content,'lxml')
    t1=str(soup.find_all(attrs={"class":"Avatar User-avatar"}))
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    img = re.findall(imgre,t1)
    for imgurl in img:
        urllib.urlretrieve(imgurl, 'F:/zhihu/E/'+a+b+c+'%s.jpg' % x)


