#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('imdb.db')
c = conn.cursor()
f = open('imdb.sql')
sql = f.read()
c.executescript(sql)
conn.commit()
conn.close()
