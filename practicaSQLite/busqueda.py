#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('imdb.db')
c = conn.cursor()
conn.commit()
conn.close()

def searchMovie(kind):
    c.execute()

def searchActhor():
