import urllib.request as ur

from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime
import urllib


def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = ur.Request(url=url, headers=headers)  # python2，urllib.request()
    response = ur.urlopen(req)  # python2，urllib2.urlopen()
    return response.read()


def set_all(url):
    data = open_url(url).decode('utf-8')
    soup1 = BeautifulSoup(data, 'html.parser')
    soup = soup1.findAll("ul", attrs={"class": "news_list"})
    res = [x for x in tuple(soup)][0].findAll("li")
    return res


def find_page(i):
    return '''http://1122nf.com/tupianqu/yazhou/index_''' + str(i) + '''.html'''


def all_title(url):
    return set_all(url)


init_url = '''http://1122nf.com'''


def single_detail(x):
    partern = '''.*<li><a href="(.*?)"(.*?)"><span>(.*?)</span>(.*?)</a> </li>.*'''
    tt = re.findall(partern, repr(x))
    info = {}
    info.setdefault("url", str(init_url) + tt[0][0])
    info.setdefault("date", tt[0][2])
    info.setdefault("title", tt[0][3])

    return info


def set_all_img(url):
    data = open_url(url).decode('utf-8')
    soup1 = BeautifulSoup(data, 'html.parser')
    soup = soup1.findAll("div", attrs={"class": "news"})
    res = [x for x in tuple(soup)][0].findAll("img")
    return res

array = []


def find_img(x):
    info = single_detail(x)
    now = datetime.today()
    rq = str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
    file_name = "img/" + str(info["title"]) + str(rq)
    try:
        res1 = set_all_img(info['url'])
    except urllib.error.URLError:
        res1 = []
        pass
    partern1 = '''.*<img src="(.*?)"/>.*'''
    num = 0
    for x in res1:
        img_url = re.findall(partern1, repr(x))[0]
        array.append([file_name, img_url, num])
        num += 1
        print(img_url)


def save_imgs(x):
    info = single_detail(x)
    now = datetime.today()
    rq = str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
    file_name = "img/" + str() + str(info["title"]) + str(rq)
    res = set_all_img(info['url'])
    partern = '''.*<img src="(.*?)"/>.*'''
    num = 0
    for x in res:
        img_url = re.findall(partern, repr(x))[0]
        print(img_url)
        with open(file_name + str(num) + ".jpg", "wb") as o:
            o.write(open_url(img_url))
    print("写入" + info["title"])


def get_all_urls():
    urls = []
    for i in [j+2 for j in range(1500)]:
        try:
            url = find_page(i)
            urls.append(url)
        except urllib.error.HTTPError:
            print("结束")
            break
    return urls


def main():
    for url in get_all_urls():
        for url1 in all_title(url):
            try:
                find_img(url1)
            except IndexError:
                pass

main()
print(array)
df = pd.DataFrame(array, columns=["file", "url", "i"])
df.to_csv("demo.csv")
print("END")



