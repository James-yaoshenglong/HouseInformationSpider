import requests
import pyquery
import re

searchPara = {
    'm' : 'esf',
    'c' : 'info',
    'etype' : '1',
    'agent':'2',
}
def producePara(s):
    sb = s.encode('gbk')
    searchPara['q'] = sb

def search(searchPara):
    try:
        url="https://www.jy510.com/index.php"
        r = requests.get(url,params=searchPara)
        r.raise_for_status
        # r.encoding = r.apparent_encoding 这个不需要，原来就是gbk
        # return r
    except:
        print("爬取失败")


    html_content = pyquery.PyQuery(r.text)
    a = html_content('.site-house-list.cl.listHavePic .cl p').items()
    for temp in a:
        print(temp.text())
        content = temp.html()
        txt = re.search(r'<!-- span[^>]*>(.*)</span -->',content)
        if txt:
            print(txt.group(1))

def main():
    s = '西苑'
    producePara(s)
    search(searchPara)


if __name__ == "__main__":
    main()