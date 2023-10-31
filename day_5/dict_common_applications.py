#lv many counters with a dictionary
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

#lv1 dictionary traceback check with in
ddd = dict()
al = 'csev' in ddd
#print(ddd)
print(al)

#lv2 add new name if that repeat add 1
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

#lv3 get() method for dictionaries
#get() method can be exchange with above if statement
counts = dict()
names = ['kira', 'al', 'alpha', 'demon', 'al', 'jonah', 'sizil', 'ikra', 'sizil']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

#lv4 here without + 1 every result has o even name repeat
counts = dict()
names = ['kira', 'al', 'alpha', 'demon', 'al', 'jonah', 'sizil', 'ikra', 'sizil']
for name in names:
    counts[name] = counts.get(name, 0)
print(counts)

#text QA
counts = { 'quincy' : 1, 'mrugesh' : 42, 'beau' : 100, '0': 10} 
print(counts.get('kris', 0))
