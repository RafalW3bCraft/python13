#lv regular expression
'''
^   match begining of line
$   match the end of line
.   match any character
\s  match whitespace
\S  match not-whitespace characters
*   repeat character 0 or more times
*?  repeact character 0 or more times(non-greedy)
+   repeat character 1 or more times
+?  repeat character 1 or more times (non-greedy) 
[aeiou] match single character in listed set    
[^XYZ]  match a single characte not in the listed set
[a-z0-9]    the set of character can include a range    
(   indicate where string extraction start
)   indicate where string extraction end
'''

#lv1 using re.search() like find()
#ex without regular expression
hand = open('romeo.txt')
for lin in hand:
    lin = lin.rstrip()
    if lin.find('is') >= 0:
        print(lin)

#ex using regular expression start with import re
import re

hand = open('romeo.txt')
for line in hand:
    line = line.rstrip()
    if re.search('is', line):
        print(line)

#lv2 using re.search() link startswith()
#without
hand = open('romeo.txt')
for line in hand:
    line = line.rstrip()
    if line.startswith('It'):
        print(line)

#with
import re
hand = open('romeo.txt')
for line in hand:
    line = line.rstrip()
    if re.match('^It', line):
        print(line)

