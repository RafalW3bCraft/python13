#lv dictionaries
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

#lv1 comparing losts and dictionaries
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)

#lv2 dictionary literals
jjj = {'chuck':1, 'fred':42, 'jan':100}
print(jjj)
ooo = { }
print(ooo)

#test QA
dict = {'Fri':20, 'Thu':6, 'Sat':1}
dict['Thu'] = 13
dict['Sat'] = 2
dict['Sun'] = 9
print(dict)