#lv collection
friends = ['kivi', 'chichi', 'alward', 'jowas']
num = [1, 13, 69, 0]
alphanum = [13, 'bad', 'luck', 7, 'cronos', 3.14, 'pie']
arr = [1, 13, [7, 0], 99]
print(friends)
print(num)
print(alphanum)
print(arr)

#lv1 list and define loops
for friend in friends:
    print('Bad', friend)
print('Done!')

z = ['kira', 'fal', 'white', 'pikachu', 'doraemon']
for x in z:
    print('i choose you:', x)
print('All set!')

#lv2 looking inside lists
friend = ['ra', 'mojo', 'itachi', 'john']
print(friend[1])

#lv3 list are mutable
fruit = 'Banana'
#fruit[0] = 'b' will not work
x = fruit.lower()
print(x)
lotto = [2,14,26,41,63]
print(lotto)
lotto[2] = 28
print(lotto)

#lv4 how long is list
greet = 'hello py'
print(len(greet))
x= [1, 2, 'joe', 99]
print(len(x))

#lv5 range function
print(range(4))
friend = ['roshi', 'kraken', 'game']
print(len(friend))
print(range(len(friend)))

#lv6 a tale of two loops
friends = ['jo', 'arsi', 'hong']
for friend in friends:
    print('hoho:', friend)
for i in range(len(friends)):
    friend = friends[i]
    print('wow:', friend)
print(len(friends))
print(range(len(friends)))

#test QA
fruit = 'banana'
x = fruit[1]
print(x)