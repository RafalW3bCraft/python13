#lv json process
import json
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456" 
  },
  "email": {
    "hide" : "yes"
  }
}'''
info = json.loads(data)
print('Name:',info["name"])
print("Hide:",info["email"]["hide"])


#lv1 
import json

input = '''[
  { "id" : "001",
    "x" : "2",
    "name" : "kirh"
  },
  { "id" : "009",
    "x" : "7",
    "name" : "wick"  
  }
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])


#test QA
import json

data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''

info = json.loads(data)
print(info[1]['name'])