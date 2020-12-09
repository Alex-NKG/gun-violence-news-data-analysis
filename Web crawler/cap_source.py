import re

import requests
from bs4 import BeautifulSoup

import debuglog

record = debuglog.record_bug()


# html = requests.get("https://www.wlky.com/article/man-fatally-shot-in-paoli-woman-in-custody/34441877",headers=headers)


class news_info():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    def check_status(self, url):
        try:
            html = requests.get(url, headers=self.headers)
            return html.status_code
        except:
            record.recordlog()
            return 404

    def get_web(self, url):
        try:
            html = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(html.text, "html.parser")
            return soup
        except:
            return "None"

    def get_text(OO0OOO0000000O00O, OOO00OO0O00O000O0):  # line:1
        O00OOO0O0OOO000OO = str()  # line:2
        try:  # line:3
            O0OOO000000O00O0O = OOO00OO0O00O000O0.findAll('p')  # line:4
            for O00O0OOO0O00OO0O0 in O0OOO000000O00O0O:  # line:5
                for O0OO00OOO0O0O0OOO in O00O0OOO0O00OO0O0.contents:  # line:6
                    if O0OO00OOO0O0O0OOO.string:  # line:7
                        O00OOO0O0OOO000OO += (O0OO00OOO0O0O0OOO.string)  # line:8
            return O00OOO0O0OOO000OO  # line:9
        except:  # line:10
            record.recordlog()  # line:11
            return "None"

    def get_img(self, soup):
        img_list = list()
        all_image = soup.find_all('img')
        for image in all_image:
            try:
                matchObj = re.match(r'(http)(.)+(.jpg?)(.)+', image['src'], re.M | re.I)
                if matchObj:
                    # print(matchObj.group())
                    img_list.append(matchObj.group())
            except:
                record.recordlog()
            return img_list
            # exit()

# x=news_info()
# che=x.check_status("https://www.kktv.com/2020/10/22/1-killed-2-injured-in-shooting-at-springs-apartment-complex/")
# print(che)
# html=x.get_web("https://www.kktv.com/2020/10/22/1-killed-2-injured-in-shooting-at-springs-apartment-complex/")

# text=x.get_text(html)
# img=x.get_img(html)
# print(text)
# print(img[0])
