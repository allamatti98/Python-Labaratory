#Constructors provide a platform to parse arguments to Parameters
class Shujaa:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


Sha1 = Shujaa(7,2,9)
print(Sha1.x)


class Person:
    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print(f"Talk {self.name}")


ps1 = Person("Peter Parker")
ps1.talk()
print(ps1.name)

class Christian:
    def __init__ (self, city):
        self.city = city
        
Ch1 = Christian("Kampala")
print(Ch1.city)

class Human:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def age():
        print("One's age. ")

h1 = Human("Peter",23)
print(h1.name)
print(h1.age)