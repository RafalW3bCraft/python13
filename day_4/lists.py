#lv concatenating list using +
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
print(a)

#lv1 list slicing
t = [9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

#lv2 list method can be seen in python3
x = list()
type(x)
dir(x)

#lv3 buid list from scratch
stuff = list()
stuff.append('book')
print(stuff)
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

#lv4 is something in a list
some = [1,9,21,10,16]
a = 9 in some
print(a)
b = 15 in some
print(b)
c = 20 not in some
print(c)

#lv5 list are in order
friends = ['jojo', 'kakarot', 'naruto', 'ace']
friends.sort()
print(friends)
print(friends[1])

#lv6 build in functions and lists
nums = [3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#ex take value and calculate as num is added
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count =count + 1
average = total / count
print('Average', average)
 
 #ex2 store value and apend in arr
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average', average)

