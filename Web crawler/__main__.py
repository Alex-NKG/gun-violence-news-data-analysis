from sys import exit

import cap_source
import creat_DB
import db_con
import debuglog
import feach_db
import get72h
import img

record = debuglog.record_bug()


def get_info_from_new_web():
    val = "select Case_ID,source from case_ID where case_ID not in (select case_ID from flag)"

    img_process = img.img_process()
    feach_data = feach_db.feach_db()
    web_info = cap_source.news_info()
    case_source_list = feach_data.read_case_ID(val)
    count_num = 0
    print("The Total number need to process is: ", len(case_source_list))

    for i in case_source_list:

        count_num += 1
        caseID = i[0]
        sor_url = i[1]
        try:
            sta_id = int(web_info.check_status(sor_url))
        except:
            record.recordlog()
            sta_id = 404
        print("\rnow process: %s get case: %s, stat %s " % (count_num, caseID, sta_id), end="")

        if sta_id == 200:
            html = web_info.get_web(sor_url)
            txt = web_info.get_text(html)
            if len(txt) > 10:
                feach_data.write_txt((str(caseID), str(txt)))
            img_list = web_info.get_img(html)
            if (img_list):
                for j in img_list:
                    news_img = img_process.down_img(j)
                    if img_process.check_img_dim(news_img):
                        np_img = img_process.img_crop(news_img)
                        feach_data.write_img((str(caseID), np_img))
            feach_data.write_flag((str(caseID), (sta_id)))
        else:
            feach_data.write_flag((str(caseID), sta_id))
    print('')
    print("finished")


case_ID_DDL = '''
CREATE TABLE if not exists  
case_ID (
  Case_ID   int NOT NULL, 
  case_data date, 
  state     char(255), 
  city      char(255), 
  address   char(255), 
  dead      int, 
  injured   int, 
  source    VARCHAR(2083), 
  PRIMARY KEY (case_ID));
'''

flag_DDL = '''
CREATE TABLE if not exists 
flag (
  case_ID int NOT NULL, 
  flag    int NOT NULL, 
  PRIMARY KEY (case_ID));
'''

text_DDL = '''
CREATE TABLE if not exists 
text (
  case_ID int NOT NULL, 
  text    mediumtext, 
  PRIMARY KEY (case_ID));
'''

img_DDL = '''
CREATE TABLE if not exists 
img (
  num     int NOT NULL auto_increment,
  case_ID int NOT NULL, 
  img     mediumblob, 
  PRIMARY KEY (num,case_ID));
'''


def db_init():
    temp = db_con.connect_DB()
    temp.creatdb()
    creat_DB.write_case_ID(case_ID_DDL)
    creat_DB.write_case_ID(text_DDL)
    creat_DB.write_case_ID(img_DDL)
    creat_DB.write_case_ID(flag_DDL)
    print("finish creat DB")


def get_72_info():
    gets = get72h.get_72h()
    gets.all_case_in72h()

def get_72_que():
    gets = get72h.get_72h()
    que = input("input query secret: ")
    while len(que) != 36:
        print("incorrect secret!")
        que = input("input new secret: ")
    pgl = input("input page len: ")
    while (int(pgl) > 80 or int(pgl) < 1):
        print("incorrect length! ")
        pgl = input("input new len: ")

    gets.all_case_quey(que, pgl)

print('''
       ___          _        ___        _                       _  _              _    _               
      / _ \/\   /\ /_\      /   \ __ _ | |_  __ _    ___  ___  | || |  ___   ___ | |_ (_)  ___   _ __  
     / /_\/\ \ / ///_\\    / /\ // _` || __|/ _` |  / __|/ _ \ | || | / _ \ / __|| __|| | / _ \ | '_ \ 
    / /_\\  \ V //  _  \  / /_//| (_| || |_| (_| | | (__| (_) || || ||  __/| (__ | |_ | || (_) || | | |
    \____/   \_/ \_/ \_/ /___,'  \__,_| \__|\__,_|  \___|\___/ |_||_| \___| \___| \__||_| \___/ |_| |_|

    ''')
print("##############   GVA Data collection   ###################")
print("##############   Designed for US CDC   ###################")
print("###### For Education and public welfare use only #########")
# print("###### It is you own risk to run it on windows 10 ########")

print('''
    input to begin:
    [1] init DB
    [2] get the 72h data from GVA(Abandoned)
    [3] collect data from GVA by query secret
    [4] collect News source
    [5] exit
    ''')

while 1:

    x = input("input your choice: ")
    if x == "1":
        try:
            db_init()
        except x:
            print(x)

    elif x == "2":
        try:
            get_72_info()
        except x:
            print(x)

    elif x == "4":
        x = get_info_from_new_web()

    elif x == "3":
        get_72_que()
    elif x == "5":
        exit()
    else:
        print("error input")
