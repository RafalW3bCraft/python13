#lv tuples are like lists
x = ('kia', 'sora', 'mano')
print(x[2])

y = ( 1, 8, 3)
print(y)
print(max(y))
print(sum(y))
print(sum(y) / len(y))
for l in y:
    print(l)

#lv1 tuples are immutable cannot mutate
r = [9, 8, 7, 6, 5]
r[2] = 1
print(r)

#lv2 tale of two sequence
l = list()
al = dir(l)
print(al)

t = tuple()
at = dir(t)
print(at)

#lv3 tuples and assignment
(x, y) = (13, 'row')
print(y)

(a, b) = (97, 13)
print(a)

#lv4 tuples and dictionaries
d = dict()
d['cere'] = 2
d['reza'] = 4
for (k,v) in d.items():
   print(k,v)

tups = d.items()
print(tups)

#lv5 tuples and comparables
print((0,1,2) < (5,1,2))
print((0,1,2000000)<(0,3,4))
print(('Ra', 'Kira')<('Ra', 'Sam'))
print(('Ra', 'Kira')>('Adams', 'Kindered'))

#test QA
d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k,i)