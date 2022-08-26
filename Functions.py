def lambo_diagnosis():
    print("""
    Dashboard Lights on
    Speedometer run
    3d Model off Lambo
 -> Fuel Low
 -> Next Service in 12 days
    Headlights on
    Radio On
    """)

def greet_user(name):
    print("Hello " + name)

greet_user("Peter")

def cube(number):
    return number ** 3

print(cube(2))

from UtilsModules import big_word,max_number
words = ["BurnaBoy","Ruger","Fireboy"]
big_word(words)
numbers= [1,5,9,10,15]
max_number(numbers)