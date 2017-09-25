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

stat = []
with io.open('store.json', encoding='utf-8') as myfile:
    for i in myfile.readlines():
    	line = i.split("\t")
    	date=datetime.datetime.strptime(line[0], '%Y-%m-%d').date()
    	line[0] = date
    	data.append(line)
    	# test+=1
    	# if test==5:
    		# break
