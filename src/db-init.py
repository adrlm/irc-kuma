import sqlite3 as sql
import sys


con = sql.connect('living_in_the_.db')
OPS  = ["bo1g", "rekyuu", "Luminarys", "Mei-mei", "nuck", "tsunderella", "Liseda", "Wizzie", "Wizbright"]

with con:
   cur = con.cursor()

   i = 0
   for op in OPS:
      cur.execute('INSERT INTO Ops VALUES({0},\'{1}\')'.format(i, op))
      i += 1