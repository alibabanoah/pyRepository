# *-* coding:utf-8 *-*
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
print('开始请求数据......')

tangshiURL = "http://so.gushiwen.org/gushi/tangshi.aspx"
rongchiURL = "http://so.gushiwen.org/gushi/songsan.aspx"
chuciURL = "http://so.gushiwen.org/gushi/chuci.aspx"

def getgushiID():
    gushiID = 787,798,938
    return gushiID


def requestgushiwen():
    print('请求数据')
    url = 'http://so.gushiwen.org/shiwen2017/ajaxshangxi.aspx'
    value= {
         'id':787,
    }
    result = getHtml(url,value)
    return result

def getHtml(url,values):
    user_agent='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    headers = {'User-Agent':user_agent}
    data = urllib.parse.urlencode(values)
    response_result = urllib.request.urlopen(url+'?'+data).read()
    html = response_result.decode('utf-8')
    return html

def shangxiParser(): #解析赏析
    shagnxi = requestgushiwen()
    soup = BeautifulSoup(shagnxi, 'html.parser')
    asoup = soup.getText()

    for string in soup.stripped_strings:
        print(repr(string),'<----')

print(shangxiParser())