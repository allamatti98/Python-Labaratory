biodata = {
    "name": "Alex Hunter",
    "age": 19,
    "employed": "True",
    "email": "mralex@gmail.com"
}
print(biodata["email"])

dic1 = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
contact = input("Kindly enter your phone number? ")
output = ""
for no in contact:
    output += (dic1.get(no)) + " "
print(output)
















"""
biodata = {
    "First_Name": "Alex",
    "Last_Name": "Hunter",
    "Age": 23,
    "Striker": True
}

print(biodata)
print(biodata["Striker"])
print(biodata["Last_Name"])
#print(biodata["School"])
print(biodata.get("birthdate","1st July 1999"))


#Challenge
numbers = {
    "0": "Zero ",
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four ",
    "5": "Five ",
    "6": "Six ",
    "7": "Seven ",
    "8": "Eight ",
    "9": "Nine "
}
contact = input("Kindly enter your contact: ")
for number in contact:
    print(numbers[number])

#MstAns
output = ""
for number in contact:
    output += numbers.get(number, "!") + " "
print(output)
"""