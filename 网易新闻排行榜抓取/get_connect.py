#coding:utf-8
import requests
from lxml import etree
from bs4 import BeautifulSoup
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def get_title_url():
    with open('get_url.txt') as file:
        con = file.readlines()
        url_list = []
        title_list = []
        num = 0
        for x in con:
            if num%2 ==1:
                url_list.append(x)
            else:
                title_list.append(x)
            num+=1
        zip_list = zip(title_list,url_list)
        #返回[title,list]列表集合
        return zip_list

def get_content():
    zip_list = get_title_url()
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    ab=0
    for x in zip_list:
        con = requests.get(x[1].strip('\n')).content
        sele = etree.HTML(con)
        p = sele.xpath("//p/text()")
        utf_title = x[0].encode('utf-8')
        print utf_title
        txt_title = 'info/'+str(ab)+'.txt'
        print txt_title
        with open(txt_title,'a+') as file:
            for y in p:
                a = y.encode('utf-8')+'\n'
                file.write(a)
        # print ab
        ab+=1        
        # for y in p:
        #     a = y.encode('utf-8') 
        #     with open('content.txt','w') as file:
        #         file.write(a)
                # break
    return
get_content()