# the overall structure of DB, run only once
import db_con
def write_case_ID(vals):

        db = db_con.connect_DB()
        #db.query("use " +DBname )
        db.query(vals)
        db.commit()

#5.0.3及更高版本：0到65,535之间的值。
case_ID_DDL='''
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

flag_DDL='''
CREATE TABLE if not exists 
flag (
  case_ID int NOT NULL, 
  flag    int NOT NULL, 
  PRIMARY KEY (case_ID));
'''

text_DDL='''
CREATE TABLE if not exists 
text (
  case_ID int NOT NULL, 
  text    mediumtext, 
  PRIMARY KEY (case_ID));
'''

img_DDL='''
CREATE TABLE if not exists 
img (
  case_ID int NOT NULL, 
  num     int NOT NULL auto_increment, 
  img     mediumblob, 
  PRIMARY KEY (num，case_ID));
'''

# write_case_ID(case_ID_DDL)
# write_case_ID(text_DDL)
# write_case_ID(img_DDL)
# write_case_ID(flag_DDL)
