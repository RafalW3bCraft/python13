import re
#lv matching and extracting data with re.findall()
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOU]+',x) #because capital world not avail
print(y)

#lv1 Warning: Greedy MAtching
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)
y = re.findall('^F.+?:',x)
#we choose non greedy +?
print(y)

#lv2 fine-tuning string extraction
x = 'From stephan.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
y = re.findall('^From (\S+@\S+)',x)
print(y)

#test QA
S = 'A message from csev@umich.edu to cwen@iupuo.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+',S)
print(lst)
