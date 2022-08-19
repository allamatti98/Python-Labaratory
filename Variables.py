name = input("What is your name? ")
print("Hello " + name + ", Welcome to Kampala Hospital.")
age = input("How old are you? ")
yob = 2022 - int(age)
print(f'My brother was also born in {yob} ')
while True:
    is_new = input("Have you been a patient here before? ")
    if is_new.upper() == "YES" or is_new == "NO":
        print("Data saved successfully")
        break
    else:
        print("Type 'Yes' or 'No'")
        


















'''
name = input("What is your name?: ")
print("Hello " + name + ", welcome to Kingsman Hospital.")
age = input("How old are you?: ")
bd = 2022 - int(age)
print("I too was born in " + str(bd))
while True:
    is_new = input("Are you a new Patient?: ")
    if is_new.upper() == "YES" or is_new.upper() == "NO":
        print("File successfully saved")
        break
    else:
        print(f"The answer is Yes or No {name}")
'''