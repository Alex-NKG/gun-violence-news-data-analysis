
import db_con
import debuglog
record= debuglog.record_bug()
from sys import exit

class feach_db:
    def __init__(self):
        self.db = db_con.connect_DB()

    def read_case_ID(self, vals):
        return (self.db.read_query(vals))

    def write_flag(self, vals):

        self.sql_query = '''
        INSERT IGNORE INTO flag
  (case_ID, 
  flag) 
VALUES 
  (%s, 
  %s);
'''
        try:
            self.db.query(self.sql_query, vals)
            self.db.commit()
        except:
            record.recordlog()
            exit()

    def write_img(self, vals):

        self.sql_query = '''
        INSERT IGNORE INTO img
  (case_ID, 
  img) 
VALUES 
  (%s, 
  %s);
'''
        try:
            self.db.query(self.sql_query, vals)
            self.db.commit()
        except:
            record.recordlog()
            exit()

    def write_txt(self, vals):

        self.sql_query = '''
        INSERT IGNORE INTO text
  (case_ID, 
  text) 
VALUES 
  (%s, 
  %s);
'''
        try:
            self.db.query(self.sql_query, vals)
            self.db.commit()
        except:
            record.recordlog()
            exit()
