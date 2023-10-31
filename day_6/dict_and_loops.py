#lv counting patter
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

#lv1 define loops and dictionaries
counts = {'kira': 1, 'iraf' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])

#lv2 retrieving lists of keys and and values
jjj = {'kira': 1, 'jonah': 42, 'ior': 100}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#lv3 two iteration variables
kk = {'j': 1, 'jen': 42, 'fer': 100}
for aaa,bbb in kk.items() :
    print(aaa, bbb)

#lv4 
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

#test QA
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
        