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