han = open('mbox-short.txt')

for line in han:
	line = line.rstrip()
#	print('Line:', line)
#	if line == '':
#		print('Skip Blanck')
#		continue
	wds = line.split()
#	print('Words:',wds)
#guardian a bit stronger change 1 to 3 words
	if len(wds) < 3:
		continue
	if wds[0] != 'From':
#	if len(wds) < 3 or wds[0] != 'From':
#		print('Ignore')
		continue
	print(wds[2])
