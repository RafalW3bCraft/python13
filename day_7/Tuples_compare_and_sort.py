#lv sorting list of tuples
t = {'p':10,'y':1,'t':22}
print(t.items())
at = sorted(t.items())
print(at)

#using sorted()
for k,v in sorted(t.items()):
    print(k,v)

#lv1 sort by values instead of key
l = {'k':10, 'i':1, 'a':22}
tmp = list()
for k,v in l.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

#lv2 most common word find fro disc
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)

#lv3 even shorter version
c = {'a': 10, 'b':1, 'c':22}
print(sorted([(v,k) for k,v in c.items()]))

#test QA
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)
#short version
print(sorted([(v,k) for k,v in counts.items()], reverse=True))