#coding:utf-8

import requests
import re
from time import sleep
from bs4 import BeautifulSoup

url = 'https://image.baidu.com/search/index?ct=201326592&z=0&s=0&tn=baiduimage&ipn=r&word=%E5%A4%B4%E5%83%8F%20%E4%B8%8D%E5%90%8C%E9%A3%8E%E6%A0%BC%20%E4%B8%AA%E6%80%A7&pn=0&istype=2&ie=utf-8&oe=utf-8&cl=2&lm=-1&st=-1&fr=&fmq=1461834053046_R&ic=0&se=&sme=&width=&height=&face=0'
page = requests.get(url).text
'''
#beautifulsoup创建对象
soup = BeautifulSoup(page,'html.parser',from_encoding=encoding)
print soup.li

'''
#使用正则搜索
reg = re.compile('https://.*?\.jpg')
imglist = re.findall(reg,page)
#去重复
for y in imglist:
    while imglist.count(y)>1:
        del imglist[imglist.index(y)]
x = 0
#遍历网址
for imgurl in imglist:
    #获得网址内容
    imgsrc = requests.get(imgurl).content
    #以二进制编码写入文件
    imgfile = open('%s.jpg'%x,'wb')
    imgfile.write(imgsrc)
    x+=1


