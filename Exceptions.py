#Define a function that collects biodata in their correct data types or else it displays your error message.
def bio():
    name = input("Name: ")
    age = int(input("Age: "))
    nationality = input("Nationality: ")
    birth = 2022 - age
try:
    bio()
    print("Good Good!!!")
except ValueError:
    print("Must be a value")











"""
def bio():
    fname = input("What is your first name?: ")
    lname = input ("What is you second name?: ")
    age = int(input("How old are you?: "))
    gender = input("What is your gender?: ")
    status = bool(input("Are you married?: "))
    year = 2022
    birth = year - age
    print(f"You were born in {birth}???")
print("Hey there...")
try:
    bio()
    print("Thank You.")
except ValueError:
    print("Age must be a number.")
"""