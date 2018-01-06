#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
import sys
import datetime
import tempmon
import  time

DB = "templog.db"
TABLE  = "Temps"
con = None

try:
    con = sqlite3.connect(DB)
    print(con)
    with con:
        current_date = datetime.datetime.now()
        temp, hum = tempmon.get_hum_temp()
        print(temp)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS {} (Date TIMESTAMP, Temperature FLOAT, Humidity FLOAT)".format(TABLE))
        print(current_date)
        sql = 'INSERT INTO {} (Date, Temperature, Humidity) values (?,?,?)'.format(TABLE)
        cur.execute(sql, (current_date, temp, hum))




except sqlite3.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()