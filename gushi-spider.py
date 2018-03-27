import urllib.parse
import urllib.request
import re
print('开始请求数据......')

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

print(requestgushiwen())