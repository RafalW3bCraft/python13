import urllib.request, urllib.parse, urllib.error

#lv Using utllib in python with import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#lv1 like a file
bhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') 
counts = dict()
for line in bhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#lv2 read web pages
ahand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in ahand:
    print(line.decode().strip())
 



#test QA
'''
import urllib.request

fhand = urllib.request.urlopen('http://www.ribison.com')
for line in fhand:
    print(line.decode().strip())
'''