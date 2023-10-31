#lv string data type
str1 = 'hello'
str2 = 'there'
bob = str1+str2
print(bob)
str3  = '123'
#str3=str3+1 will not work need int for str3 as bellow
x=int(str3)+1
print(x)

#lv1 read and convert
name = input('Enter:')
print(name)
apple = input('Enter:')
print(apple)
#x=apple-10 will have traceback as not work because not int added for apple
x=int(apple)-10
print(x)

#lv2 look inside string
fruit = 'banana'
letter = fruit[1]
print(letter)
x=3
w=fruit[x-1]
print(w)

#lv3 string have length
fruit = 'banana'
print(len(fruit))

#lv4 len function
fruit = 'coconut'
x = len(fruit)
print(x)

#lv5 looping thought string
fruit = 'watermelon'
index=0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

#lv6 looping thrrough string without index this is better if index is not needed from lv5
fruit = 'kiwi'
for letter in fruit:
    print(letter)

#lv7 looping and counting times a appear
word = 'grapesaa'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1

print(count)

#lv8 looking deep into in
for letter in 'banana':
    print(letter)

#test QA
for n in 'banana':
    print(n)