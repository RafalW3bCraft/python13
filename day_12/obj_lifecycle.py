#lv constructor and destructor
class PartyAnimal:
    x = 0
    def __init__(self):
        print('I an constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('Goodbye! I am destructed')

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an conatains', an)


#lv1 construtors with parameters
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, z):
        self.name = z
        print(self.name, 'Constructed')        
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

s = PartyAnimal('Sally')
s.party()
j = PartyAnimal('Jim')
j.party()
j.party()


#test QA
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')
#al = PartyAnimal(input('enter'))
#print(al)

q.party()
m.party()
q.party()