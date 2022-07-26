def greet_user(name):
    print(f"Hello {name}, How are you?")


greet_user("Peter")
snap = input("What is your name?: ")
greet_user(snap)

def bio(fname, lname, sex, age):
    print(f"Hello {fname} {lname}, Happy birthday, {age} years of positive existance!!!")
bio("Peter","Parker",'M',"23")