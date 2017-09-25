#! /usr/bin/python
import re
import string
import time 
import datetime
import io
from os import curdir
from os.path import join as pjoin
import sqlite3

data = []
test = 0


conn = sqlite3.connect('bukatempr.sqlite')
cur = conn.cursor()

with io.open('store.json', encoding='utf-8') as myfile:
    for i in myfile.readlines():
    	line = i.split("\t")
    	date=datetime.datetime.strptime(line[0], '%Y-%m-%d').date()
    	line[0] = date
  #   	line[1] = int(line[1])
		# line[2] = int(line[2])
		# line[3] = int(line[3])
		# line[4] = int(line[4])
		# line[5] = int(line[5])
    	data.append(line)
    	# test+=1
    	# if test==5:
    		# break
cur.executemany('INSERT INTO report("date","hrs","temp","hum","pres","wind","wind_dir","detail") VALUES (?,?,?,?,?,?,?,?)', data)
conn.commit()