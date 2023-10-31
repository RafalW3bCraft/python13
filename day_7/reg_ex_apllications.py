#lv regular expression applications
#without 
data = 'From stephan.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
at = data.find('@')
print(at)
sp = data.find(' ', at)
print(sp)
host = data[at+1: sp]
print(host)

#without 1
words = data.split()
print(words)
email = words[1]
print(email)
pieces = email.split('@')
print(pieces[1])

#with regex version
import re
y = re.findall('@([^ ]*)', data)
print(y)
#even cooler regex version
y = re.findall('^From .*@([^ ]*)', data)
print(y)


#lv1 
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

#lv2 escape character
import re
x = 'We just recieved $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)
