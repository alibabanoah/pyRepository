import urllib.parse
import urllib.request
import re
print('请求数据')

def requestgushiwen(index):
    print('请求数据')
    url = 'http://so.gushiwen.org/shiwen2017/ajaxshangxi.aspx'
    value= {
         'id':787,
    }
    result = getHtml(url,value)
    return result