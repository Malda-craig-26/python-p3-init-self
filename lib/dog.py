#!/usr/bin/env python3













class Dog:
    
   def __init__(self):
        print("A dog is born!")

   def bark(self):
        print("Woof!")

fido = Dog()

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed


dog1 = Dog("Buddy")
print(dog1.name)
print(dog1.breed)  

dog2 = Dog("Max", "Golden Retriever")
print(dog2.name)   
print(dog2.breed)  









#class Dog:
    #def __init__(self, name):
        #self.name = name

    #def bark(self):
        ##print("Woof!")

    #def get_adopted(self, owner_name):
        #self.owner = owner_name

#fido = Dog("Fido")
#fido.get_adopted("Sophie")
#fido.owner
# "Sophie"

#class Dog:
    #def __init__(self, name, favorite_toy="Any"):
        #self.name = name
        #self.favorite_toy = favorite_toy

#fido = Dog("Fido")
#fido.favorite_toy
# Any

#snoopy = Dog("Snoopy", "Tennis Ball")
#snoopy.favorite_toy
# Tennis Ball

