import requests
from bs4 import BeautifulSoup
from lxml import etree

list = []

url = 'http://news.163.com/rank/'
url_content = requests.get(url).content

selector = etree.HTML(url_content)
links = selector.xpath('//tr/td/a')

with open('get_url.txt','w') as file:
    for link in links:
        text = link.xpath('text()')
        href = link.xpath('@href')
        a = str(text[0].encode('utf-8')+'\n'+href[0]+'\n')
        file.write(a)




# soup = BeautifulSoup(respon,'html.parser')
# with open('demo.txt','w') as file:
#     for x in soup.find_all('a'):
#         file.write(x.get('href')+'\n')


