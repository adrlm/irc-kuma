import sqlite3 as sql
import sys


con = sql.connect('living_in_the_.db')

with con:
   cur = con.cursor()
   cur.execute('SELECT SQLITE_VERSION()')

   data = cur.fetchone()

   print("SQLite version {0}".format(data))