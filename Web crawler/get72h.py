import re
import time
from datetime import datetime
from sys import exit

import requests
from bs4 import BeautifulSoup

import db_con
import debuglog

record = debuglog.record_bug()


# this class is to get all the cases happend in the last 72h
# use:
# x=get_72h()
# x.all_case_in72h()

class get_72h:
    def __init__(self):
        self.url = "https://www.gunviolencearchive.org/last-72-hours"
        self.url2 = "https://www.gunviolencearchive.org/query/"

        self.db = db_con.connect_DB()

    def write_case_ID(self, vals):
        # self.db.query("use "+DBname)
        self.sql_query = '''
        INSERT IGNORE INTO case_ID
  (case_ID, 
  case_data, 
  state, 
  city, 
  address, 
  dead, 
  injured, 
  source) 
VALUES 
  (%s, 
  %s, 
  %s, 
  %s, 
  %s, 
  %s, 
  %s, 
  %s);
'''
        try:
            self.db.query(self.sql_query, vals)
            self.db.commit()
        except:
            record.recordlog()
            exit()
    def get_page(self, page=0, dbname="gva_1"):
        payload = {'page': page}
        html = requests.get(self.url, params=payload)
        # print(html)
        soup = BeautifulSoup(html.text, "html.parser")
        for i, web_url, source in zip(soup.findAll('tr', attrs={'class': 'odd'}),
                                      soup.findAll('li', attrs={'class': '0 first'}),
                                      soup.findAll('li', attrs={'class': '1 last'})
                                      ):
            urls = web_url.find('a')['href']
            source = source.find('a')['href']
            case_ID = int(re.search(r"(\d)+", urls).group())
            case_data = datetime.strptime(i.find_all('td')[0].string, "%B %d, %Y")
            state = i.find_all('td')[1].string
            city = i.find_all('td')[2].string
            address = i.find_all('td')[3].string
            dead = int(i.find_all('td')[4].string)
            injured = int(i.find_all('td')[5].string)
            self.write_case_ID((str(case_ID), str(case_data), str(state), str(city), str(address), str(dead),
                                str(injured), str(source)))
            # print (state, city, address, dead, injured,source,urls  )

    def get_page_que(self, page=0, pre_url="xx"):
        path = str(self.url2 + pre_url)
        # print(path)

        payload = {'page': page}
        html = requests.get(path, params=payload)
        # print(html)
        soup = BeautifulSoup(html.text, "html.parser")
        for i, web_url, source in zip(soup.findAll('tr', attrs={'class': 'odd'}),
                                      soup.findAll('li', attrs={'class': '0 first'}),
                                      soup.findAll('li', attrs={'class': '1 last'})
                                      ):
            urls = web_url.find('a')['href']
            source = source.find('a')['href']
            case_ID = int(i.find_all('td')[0].string)

            case_data = datetime.strptime(i.find_all('td')[1].string, "%B %d, %Y")
            state = i.find_all('td')[2].string
            city = i.find_all('td')[3].string
            address = i.find_all('td')[4].string
            dead = int(i.find_all('td')[5].string)
            injured = int(i.find_all('td')[6].string)
            self.write_case_ID((str(case_ID), str(case_data), str(state), str(city), str(address), str(dead),
                                str(injured), str(source)))

    def all_case_in72h(self):
        for i in range(0, 14):
            self.get_page(i)
        record.msg_record("suss 15 Page")
        print("15 page success, no error")

    def all_case_quey(self, que, lens):
        count_num = 0
        for i in range(0, int(lens)):
            count_num += 1
            self.get_page_que(i, que)
            print("\rnow process: %s  " % (count_num), end="")
            time.sleep(3)
        print('')
        print("finished")
