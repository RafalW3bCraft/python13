#lv class object
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print("So far",self.x)
an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
print("Type", type(an))
print("Dir ", dir(an))

#lv1 Plating with dir() and type()
x = list()
print(type(x))
print(dir(x))

#ex Try dir() with String
y = 'Hello there'
print(dir(y))
print(y.upper())
print(y.replace(y, 'hi'))

#lv2
class RowAgent:
    al = 0
    def agent(bond):
        bond.al = bond.al + 1
        print('Target', bond.al)
oo7 = RowAgent()
oo7.agent()
print('Type', type(oo7))
print('Dir ', dir(oo7))

#test QA
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()
