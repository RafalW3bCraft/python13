#lv opening file using open()
#handle = open(filename, mode)
fhand = open('file.txt')
print(fhand)

#lv1 newline character
stuff = 'Hello\nWorld'
print(stuff)
morestuff = 'X\nY'
print(morestuff)
print(len(morestuff))

#lv2 dile handle as sequence
#newline is used by \n
xfile = open('file.txt')
for each in xfile:
    print(each)

#lv3 counting lines in file
fhand = open('file.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count', count)

#lv4 reading whole file
fhand = open('file.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

#lv5 searching through a file
fhand = open('file.txt')
for line in fhand:
    if line.startswith('hello:'):
        print(line)
 
#lv6 searching through a file(fixed)
fhand = open('file.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('hello:'):
        print(line)

#lv7 skipping with continue
fhand = open('file.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('hello:'):
        continue
    print(line)

#lv8 without : after 'hello' and without continue
fhand = open('file.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('hello'):
        print(line)

#lv9 without : after 'hello' and with continue
fhand = open('file.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('hello'):
        continue
    print(line)

#lv10 usinf in to select lines
fhand = open('file.txt')
for line in fhand:
    line = line.rstrip()
    if not 'big bad wolf' in line:
            continue
    print(line)

#lc11 prompt for file name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('pack'):
        count = count + 1
    print('There were', count, 'subject lines in', fname)

#lv12 bad file name
rname = input('Enter file name: ')
try:
    fhand = open(rname)
except:
    print('File cannot be opened:', rname)
    quit()
count = 0
for lines in fhand:
    if line.startswith('hello'):
        count = count + 1
print('There were', count, 'subject lines in', rname)




