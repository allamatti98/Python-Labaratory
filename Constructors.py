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