# *-* coding:utf-8 *-*
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re

ListgushiwenURL = []
ListshiwendetailURL = []

def GetListgushiwenURL(): # Read URL data from config file 'gushiwenURL.txt' to List Listgushiwen
    with open("gushiwenURL.txt",encoding='utf-8') as f:
        for line in f.readlines():
            ListgushiwenURL.append(line)

GetListgushiwenURL() # Call function GetgushiwenURL to get URL data

def genegushiURL():
    for listgushiURL in ListgushiwenURL:
        yield re.split(r'[,]',listgushiURL)

for f in genegushiURL():
    print(f[0],'output gushiwen')



def getgushiID():
    gushiID = 787,798,938
    return gushiID

def requesturl(url,par):
    print('请求数据')
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

def URLParser():
    for URL in genegushiURL():
        shagnxi = requesturl(URL[0],par=None)
        soup = BeautifulSoup(shagnxi, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('href')[1:8] == "shiwenv":
                ListshiwendetailURL.append(link.get('href'))
URLParser()

def CommentParser(): #解析译文与赏析
    #for link in ListshiwendetailURL:
        #alllink = "https://so.gushiwen.org"+link
        shagnxi = requesturl("https://so.gushiwen.org/shiwenv_85c1b0fcb6f9.aspx",par=None)
        soup = BeautifulSoup(shagnxi, 'html.parser')
        s_soup=soup.find_all('div',attrs={"onclick":re.compile(r"shangxiShow.")})
        f_soup=soup.find_all('div',attrs={"onclick":re.compile(r"fanyiShow.")})
        print(s_soup,'++++++++++++++++++++')
        print(f_soup, '++++++++++++++++++++')
        #for string in soup.stripped_strings:
        #    print(repr(string),'<----')
        #print(URL[0],"新的")

CommentParser()

#for  link in  ListshiwendetailURL:
#    print("-----》","https://so.gushiwen.org"+link,"《------")
