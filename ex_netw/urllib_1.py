import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = dict()
for line in fhand:
#simple	print(line.decode().strip())
	words = line.decode().split()
	for word in words:
		count[word] = count.get(word,0) + 1
print(count)
