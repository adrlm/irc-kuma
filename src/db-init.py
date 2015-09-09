import sqlite3 as sql
import sys


con = None

try:
   con = sql.connect('living_in_the_.db')

   cur = con.cursor()
   cur.execute('SELECT SQLITE_VERSION()')

   data = cur.fetchone()

   print("SQLite version {0}".format(data))

except (sql.Error, e):
   print("Error {0}:".format(e.args[0]))
   sys.exit(1)

finally:
   if con:
      con.close()