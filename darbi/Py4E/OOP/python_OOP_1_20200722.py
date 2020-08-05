class PartyAnimal:               # The 'class' keyword defines a template indicating what data and code
   x = 0                         # will be contained in each object of type PartyAnimal.

   def party(self) :             # Definition of method 'party' which adds 1 to x inside the object 
     self.x = self.x + 1
     print("So far",self.x)

an = PartyAnimal()
an.party()                       # 'party' method call
an.party()
an.party()
PartyAnimal.party(an)
