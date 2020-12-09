from configparser import ConfigParser
from itertools import chain
from sys import exit

import mysql.connector

import debuglog

record = debuglog.record_bug()


class connect_DB:
    def __init__(self):
        try:
            self.cfg = ConfigParser()
            self.cfg.read('conf.ini')

            self.db = mysql.connector.connect(
                host=self.cfg.get('DATABASE', 'host'),
                user=self.cfg.get('DATABASE', 'username'),
                password=self.cfg.get('DATABASE', 'password')
            )
            self.cursor = self.db.cursor()
        except:
            record.recordlog()
            exit()

    def creatdb(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS " + self.cfg.get('DATABASE', 'database'))  # sql: use db name
        self.commit()

    def query(self, sql, *args):
        try:
            args = list(chain.from_iterable(args))
            self.cursor.execute("use " + self.cfg.get('DATABASE', 'database'))  # sql: use db name
            self.cursor.execute(sql, args)  # format: qurey %s (var)
            return self.cursor.fetchone()
        except:
            record.recordlog()
            exit()
    def read_query(self, sql, *args):
        try:
            args = list(chain.from_iterable(args))
            self.cursor.execute("use " + self.cfg.get('DATABASE', 'database'))  # sql: use db name
            self.cursor.execute(sql, args)  # format: qurey %s (var)
            return self.cursor.fetchall()
        except:
            record.recordlog()
            exit()
    def commit(self):
        try:
            self.db.commit()
        except:
            record.recordlog()
            exit()

    def close(self):
        self.cursor.close()




