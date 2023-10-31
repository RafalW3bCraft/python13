#lv split 
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)
print(stuff[-1])

#lv1
line = 'A lot            of spaces'
etc = line.split()
print(etc)
line = 'first;second;third'
thing = line.split()
print(thing)
print(len(thing))
thing = line.split(';')
print(thing)
print(len(thing))

#lv2
fhand = open('file.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('hello'): continue
    word = line.split()
    print(word[2])

line = 'From stephan.king@utc.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)
email = words[1]
print(email)
pieces = email.split('@')
print(pieces)
print(pieces[1])

#test QA
words = 'His e-mail is q-lar@@freecodecamp.org'
pieces = words.split()
print(pieces)
parts = pieces[3].split('-')
print(parts)
n = parts[1]
print(n)