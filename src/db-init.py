import sqlite3 as sql
import sys


con = sql.connect('living_in_the_.db')
OPS  = ["bo1g", "rekyuu", "Luminarys", "Mei-mei", "nuck", "tsunderella", "Liseda", "Wizzie", "Wizbright"]

with con:
   db = con.cursor()

   db.execute('DROP TABLE IF EXISTS Ops;')
   db.execute('CREATE TABLE IF NOT EXISTS Ops(Id INTEGER PRIMARY KEY, Name TEXT);')

   i = 0
   for op in OPS:
      db.execute("INSERT INTO Ops(Name) VALUES('{0}');".format(op))
      i += 1