#lv
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)

#lv start with sqlite
import sqlite3

conn = sqlite3.connect('ex_db')
c = conn.cursor()

#create table
c.execute('''CREATE TABLE stocks
          (date text, trans text, symbol text, qty real, price real)''')
          