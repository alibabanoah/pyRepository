# *-* coding:utf-8 *-*
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
import ssl
import time
import MySQLdb
import traceback
ssl._create_default_https_context = ssl._create_unverified_context

dbname="www.ifamilyedu.com"
dbuser="root"
dbpass="848a2f3a"
dbbase="poetry"
pname = "女冠子·四月十七"
db = MySQLdb.connect(dbname,dbuser,dbpass,dbbase,charset="utf8" )

def dbinsert(pname,pcom,pfy):
    cursor = db.cursor()
    sql = 'insert into poetry_temp_com (pname,pcom,pfy) values ' \
          '(\''+pname+'\',\''+pcom+'\',\''+pfy+'\')'
    print(sql,'sqlll')
    try:
        print(sql, 'exexesfasfdasfasfd')
        cursor.execute(sql)
        db.commit()
    except:
        traceback.print_exc()

#dbinsert('pnmadfsadf','commmmm','中文')

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
    print(f[0],'本次打开第一层')



def getgushiID():
    gushiID = 787,798,938
    return gushiID

def requesturl(url,par=''):
    print('请求数据')
    value= {
         'id':par,
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
        print(URL[0])
        htmldom = requesturl(URL[0])
        soup = BeautifulSoup(htmldom, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('href')[1:8] == "shiwenv":
                ListshiwendetailURL.append(link.get('href'))
URLParser()
print(len(ListshiwendetailURL))

def CommentParser(): #解析译文与赏析
    for link in ListshiwendetailURL:
        alllink = "https://so.gushiwen.org"+link
        #alllink = "https://so.gushiwen.org/shiwenv_cecffc2a400d.aspx"
        print(alllink,'<---------------------------------------------------all')
        clickID = requesturl(alllink,par=None)
        soup = BeautifulSoup(clickID, 'html.parser')
        s_soup=soup.find_all('div',attrs={"onclick":re.compile(r"shangxiShow.")})
        f_soup=soup.find_all('div',attrs={"onclick":re.compile(r"fanyiShow.")})
        t_soup=soup.h1
        t_pname=t_soup.contents[0]
        tempid_ = re.findall(r"shangxiShow\(\d+\)",s_soup.__str__())
        if (len(tempid_)==0):
            sxid = None
        else:
            sxid = re.findall(r"\d+",tempid_[0])[0] # 获得sxID
        print(sxid,"这里是ID--------")

        tempid_ = re.findall(r"fanyiShow\(\d+\)",f_soup.__str__())
        if (len(tempid_)==0):
            fyid = None
        else:
            fyid = re.findall(r"\d+", tempid_[0])[0]  # 获得fyID
        print(fyid, "这里是ID--------")

        fy_sx(fyid=fyid,sxid=sxid,pname=t_pname,alllink=alllink)
        time.sleep(100000)

def fy_sx(fyid,sxid,pname,alllink):
    fyurl = "https://so.gushiwen.org/shiwen2017/ajaxfanyi.aspx"
    sxurl = "https://so.gushiwen.org/shiwen2017/ajaxshangxi.aspx"
    fyfinal, sxfinal = '', ''

    if (fyid!=None):
        fycontent = requesturl(fyurl, par=fyid)
        fysoup = BeautifulSoup(fycontent, 'html.parser')
        for string in fysoup.stripped_strings:
            fyfinal = fyfinal + string + '</br>'
        findstr1 = re.findall(r"有用\(\d+\)", fyfinal)
        findstr2 = re.findall(r"没用\(\d+\)", fyfinal)
        fyfinal = fyfinal.replace(findstr1[0], '')
        fyfinal = fyfinal.replace(findstr2[0], '')
        fyfinal = fyfinal.replace("▲", '')
        print(fyfinal)
    else:
        fyfinal=getsimpfy(alllink)

    if (sxid!=None):
        sxcontent = requesturl(sxurl, par=sxid)
        sxsoup = BeautifulSoup(sxcontent, 'html.parser')
        for string in sxsoup.stripped_strings:
            sxfinal = sxfinal + string + '</br>'
        findstr1 = re.findall(r"有用\(\d+\)", sxfinal)
        findstr2 = re.findall(r"没用\(\d+\)", sxfinal)
        sxfinal = sxfinal.replace(findstr1[0], '')
        sxfinal = sxfinal.replace(findstr2[0], '')
        sxfinal = sxfinal.replace("▲", '')
        print(sxfinal)
    else:
        sxfinal=getsimpsx(alllink)
    time.sleep(4)
    #dbinsert(pname=pname,pcom=sxfinal,pfy=fyfinal)

def getsimpfy(alllink):
    fycontent = requesturl(alllink, par=None)
    soup = BeautifulSoup(fycontent, 'html.parser')
    fysoup = soup.find_all('div', attrs={"class":"contyishang"})
    print(type(fysoup),'这个好---',fysoup[1])
    for tg in fysoup:
        print("--->",tg,"<---")


    return "this is simpfydoc"

def getsimpsx(alllink):
    return "this is simpfydoc"


CommentParser()

#for  link in  ListshiwendetailURL:
#    print("-----》","https://so.gushiwen.org"+link,"《------")
