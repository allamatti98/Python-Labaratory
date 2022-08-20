l = ["John", "Simon", "Peter", "Luke", "Mathew","Emiliana"]
max = 0
lname = ""
for name in l:
    if len(name) > max:
        lname = name
print(name)

list = [1,2,3,4,5]
list.append(10)
list.insert(0,0)
list.remove(10)
list.clear()

numb = [1,2,3,3,3,4,5,5,6,7,8,9]
numb2 = []
for no in numb:
    if no not in numb2:
        numb2.append(no)
print(numb2)


















"""
ballers = ["Kevin", "Sterling", "Grielish", "Fernandinho"]
print (ballers [0])
print (ballers[0:3])
print (ballers [-3])
ballers [0] = "Kevin De Bruyne"
print (ballers)
for Item in ballers:
    print(Item)


sets = [1,5,2,3,5,6,3,7,8,9,9,9,6,4,3,6,7,9,11]
import math
from statistics import mode
print(max(sets))
print(mode(sets))

numbers = (1,2,3,4,5,6,7,8,9,10)
"""