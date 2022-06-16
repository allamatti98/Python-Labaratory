#Take two input from the user, perform arithmetic calculations and return output and values repectively eg TOTAL: 50 Sum:20 etc
x = float(input("First Number: "))
y = float(input("Second Number: "))
sum = x + y
difference = x - y
product = x * y
division = x / y
modulus = x % y
divnoremdr = x // y

print(sum)
print(difference)
print(division)
print(modulus)
print(divnoremdr)
print("Thats all for now.")








notes = ("""
x = input("Enter first number: ")
y = input("Enter second number: ")
output = float(x) * float(y)
print("The answer is " + str(output))

x = float(input("Input the first value: "))
y = float(input("Input the second value: "))
sum = x + y
difference = x-y
product = x * y
division = x / y
rounded_division = x // y
modulus = x % y
exponent = x ** y
print("Sum: " + str(sum))
print("Difference: " + str(difference))
print("Division: " + str(division))
print("Rounded Division " + str(rounded_division))
print("Modulus: " + str(modulus))
print("Exponent: " + str(exponent))
""")