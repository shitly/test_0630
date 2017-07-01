# coding:utf-8
import urllib.request as ur
import re
from bs4 import BeautifulSoup

import pandas as pd


class SpyderTest(object):

    def __init__(self, url):
        self.url = url

    def open_url(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = ur.Request(url=url, headers=headers)  # python2，urllib.request()
        response = ur.urlopen(req)  # python2，urllib2.urlopen()
        return response.read().decode('utf-8')

    def set_all(self):
        data = self.open_url(self.url)
        soup1 = BeautifulSoup(data, 'html.parser')
        soup = soup1.findAll("div", attrs={"class": "list-con"})
        res = [x for x in tuple(soup)][1].findAll("a")
        return res

    def sigle_jx(self, i):
        x = self.set_all()[i]
        partern = '''.*<a class="livecard" (.*?)="(.*?)" (.*?)="(.*?)" (.*?)="text:(.*?),(.*?):(.*?),(.*?):(.*?),(.*?):(.*?)" (.*?)="(.*?)" (.*?)="(.*?)" target="_blank">.*'''
        t1 = [y for y in re.findall(partern, repr(x))[0]]
        # the head of link-info
        res = {}
        for i in range(int(len(t1) / 2 - 1)):
            res.setdefault(t1[2 * i], t1[2 * i + 1])

        imgs = [re.findall('.*src="(.*?)".*', repr(x)) for x in x.findAll("img")]
        see_num, game = tuple([x.next_element for x in tuple(x.findAll("span", attrs={"class": "livecard-meta-item-text"}))])
        username = x.find("strong", attrs={"class": "livecard-modal-username"}).next_element
        try:
            badge = x.find("span", attrs={"class": "livecard-badge"}).next_element
        except AttributeError:
            badge = "无描述"
        res.setdefault("see_num", see_num)
        res.setdefault("game", game)
        res.setdefault("zhubo", username)
        res.setdefault("desc", badge)
        res.setdefault("imgs", imgs)

        return res


if __name__ == '__main__':
    url = '''http://longzhu.com/channels/all'''
    t = SpyderTest(url)
    result = [t.sigle_jx(i) for i in range(len(t.set_all()))]
    df = pd.DataFrame(result)
    print(df)
    df.to_csv("c://demo.csv")
    i = 0
    for x in df['imgs']:
        for img in x:
            i += 1
            with open(str(i)+".png", "wb") as o:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
                req = ur.Request(url=img[0], headers=headers, )
                response = ur.urlopen(req).read()
                o.write(response)
    print("end")