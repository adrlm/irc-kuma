# Average output generator
def avg (list_):
   x = 0
   for i in list_:
      x += i
   return int(x / len(list_))