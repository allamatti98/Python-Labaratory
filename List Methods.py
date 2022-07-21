#Add and remove values to the end of the list. At specific points add or remove numbers.
#Identify whether a number is in the list. Reverse the list then organise it.
#Write a program that removes repeated numbers
















notes = ("""
numbers = [1, 2, 3, 4, 5]
#numbers.append(6)
#numbers.insert(0, 0)
#numbers.remove(3)
#numbers.clear
print(numbers)
print(1 in numbers) #To kno whether 1 exists in the list
print(len(numbers)) #To know the number of items in a list

nos = [1,2,3,4,5,6,7,8,9,10]
nos.append(0) #puts at the end
print(nos)
nos.remove(0) #removes an item
nos.insert(0,0) #puts in a designated index
print(nos)
#print(nos.clear())
nos.append(11)
print(nos)
nos.pop() #Removes last item in a list
print(nos)
nos.insert(4,4)
print(nos)
nos.pop(5) #Removes number in parsed index
print(nos)
print(nos.index(9))
#print(nos.index(88))
print(9 in nos)
nos.insert(10,9)
nos.insert(11,9)
print(nos)
print(nos.count(9))

noz = [1,5,8,3,5,1,3,8,0,11,15,21,13,14]
print(noz.sort())
print(noz)
print(noz.reverse())
print(noz)
noz.sort()
print(noz)
nbz = noz.copy() #Makes a copy that remains unaffected by changes to the original list
noz.insert(0,-1)
print(noz)
print(nbz)


#Program that removes repeated numbers
janzi = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,7,8,8,9,9,10]
jazz = []
for number in janzi:
    if number not in jazz:
        jazz.append(number)
print(jazz)

list = [1,2,3,4,5,6,7,8,9]
print(list)
list.append(10) #Adds at the end
print(list)
list.insert(0,0) #Index 0, put 0
print(list)
list.remove(0) #Index 0
print(list)
list.pop() #Removes last item
print(list)
list.pop(5) #Index 5
print(list)
print(6 in list) #To know whether number is in the list
#print(list.clear())
list.reverse()
print(list)
list.sort()
print(list)

#Program that removes repeated numbers
lst1 = [1,2,3,4,5,6,7,8,9,3,4,5,6,7,8,4,3,2,2,2,5,5,9,9,9,9]
lst2 = []
print(lst1.count(9))
lst1.reverse()
print(lst1)
lst1.sort()
print(lst1)
for no in lst1:
    if no not in lst2:
        lst2.append(no)
print(lst2)

noz.append(10)
print(noz)
noz.remove(10)
print(noz)
noz.pop(0)
print(noz)
noz.insert(0,1)
print(noz)
noz.remove(6)
print(noz)
noz.insert(5,6)
print(noz)
noz.append(6)
noz.append(6)
print(noz)
noz.remove(6)
print(noz)
noz.pop()
print(noz)
noz.pop()
print(noz)
noz.insert(5,6)
print(5 in noz)
print(len(noz))
noz.reverse()
print(noz)
noz.sort()
print(noz)
kl = [1,2,2,3,4,5,5,5,6,6,7,8,9,9,9,9,9]
print(kl)
nl = []
for noz in kl:
    if noz not in nl:
        nl.append(noz)
print(nl)
""")