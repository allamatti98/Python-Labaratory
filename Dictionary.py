biodata = {
    "name": "John Doe",
    "age": 23,
    "married": True
}
print(biodata["name"])

numbers = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    }
output = ""
contact = input("Kindly enter your contact: ")
for no in contact:
    output += numbers.get(no, "!") + " "
print(output)




































'''
biodata = {
    "name": "Alex Hunter",
    "age": 19,
    "employed": "True",
    "email": "mralex@gmail.com"
}
print(biodata["email"])

dic1 = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}
output = ""
contact = input("Kindly enter your contact: ")
for no in contact:
    output += dic1.get(no,"!")
dic2 = {
    "cool": "dope",
    "understand": "feel",
    "those": "dem"
}
output2 = ""
text = input("Type in text :")
t2 = text.split()
for key in t2:
    output2 += dic2.get(key, key) + " "
print(output2)
'''