#Create a parent class with three sub classes then print the various methods
class Cars:
    def tyres():
        print("Tyres")

    def engine():
        print("Engine")

    def chairs():
        print("Chairs")


class Toyota (Cars):
    def spares():
        print("Cheap spares.")

class Benz(Cars):
    def elegance():
        print("Eleganto")

class SinoTruck(Cars):
    def size():
        print("Very big")

C1 = Cars.chairs()
C2 = Toyota.chairs
C3 = Benz.elegance()

class Christian:
    def __init__ (self, king, house):
        self.king = king
        self.house = house
    
    def k(self):
        print("Cool cool")
    
class Catholic(Christian):
    pass

cat1 = Catholic("Jesus","Church")
cat1.k()

class Anglican(Christian):
    pass

cat2 = Anglican("Jesus","Church")
print(cat2.king)














'''
class Africa:
    def color():
        print("Black")
    
    def tempereature():
        print("Hot")


class Uganda(Africa):
    def Museveni(self):
        print("YKM7")

class Kenya(Africa):
    def Kenyata(self):
        print("Uhuru Kenyatta")

class Tanzania(Africa):
    pass

class Rwanda(Africa):
    pass

#Dont parse parent class
#Shh1 = Africa()
#Shh1.color()
Uganda.color()
Kenya.Kenyata()
Tanzania.mro()
Rwanda.tempereature()

#To print attribute, parse self in function first
Ug1 = Uganda()
Ug1.Museveni()
'''