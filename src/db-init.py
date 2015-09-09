import sqlite3 as sql
import sys


con = sql.connect('living_in_the_.db')
OPS  = ["bo1g", "rekyuu", "Luminarys", "Mei-mei", "nuck", "tsunderella", "Liseda", "Wizzie", "Wizbright", "remove_me"]

with con:
   con.row_factory = sql.Row
   db = con.cursor()

   db.execute('DROP TABLE IF EXISTS Ops;')
   db.execute('CREATE TABLE IF NOT EXISTS Ops(Id INTEGER PRIMARY KEY, Name TEXT);')

   for op in OPS:
      db.execute("INSERT INTO Ops(Name) VALUES('{0}');".format(op))

   db.execute('SELECT * FROM Ops;')
   rows = db.fetchall()

   for row in rows:
      print(row['Name'])

   delete = 'remove_me'
   db.execute("DELETE FROM Ops WHERE Name='{0}';".format(delete))

   db.execute('SELECT * FROM Ops;')
   rows = db.fetchall()

   for row in rows:
      print(row['Name'])