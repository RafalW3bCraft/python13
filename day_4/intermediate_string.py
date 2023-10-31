#lv slicing string
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])

#lv1 string concatention
a= 'Hello'
b = a + 'There'
print(b)
c= a + ' ' + 'There'
print(c)

#lv2 using in as logical operator
fruit = 'banana'
a = 'na' in fruit
print(a)
b = 'a' in fruit
print(b)
if 'n' in fruit:
    print('Gotcha')

#lv3 string comparison
word = 'banana'
if word  == 'banana':
    print('all right, bananas.')
if word < 'banana':
    print('your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('your word,' + word + ', comes after banana.')
else:
    print('all right, bananas.')

#lv4  string library
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi there'.lower())

#example to  get all directory for all kind strings  aka string method
stuff = 'Hello world'
type(stuff)
dir(stuff)

#lv5 string library example find() method
fruit = 'banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

#lv6 convert upper & lower case
greet = 'Hey py'
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)

#lv7 search and replace
greet = 'Hey py how is day'
nstr = greet.replace('py', 'python')
print(nstr)
nstr = greet.replace('y', 'i')
print(nstr)

#lv8 remove white space aka strip whitespace
greet = ' hi py '
a = greet.lstrip()
print(a)
b = greet.rstrip()
print(b)
c = greet.strip()
print(c)

#lv9 prefix
line = 'hey big bad wolf there'
a = line.startswith('hey')
print(a)
b = line.startswith('h')
print(b)
c = line.endswith('there')
print(c)

#lv10  parsing and extracting
data = 'From stephan.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
ace = data.find('@')
print(ace)
al = data.find(' ',ace)
print(al)
kir = data[ace+1 : al]
print(kir)


#test QA
word = 'bananana'
i = word.find('na')
print(i)