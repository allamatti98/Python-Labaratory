weight = input("What is your weight? ")
metrics = input("Is it in Kilograms (Kg) or Pounds(Lbs)")
if metrics.upper() == "KG":
    pounds = float(weight) /1.6
    print(f'Your weight in pounds is {pounds}')
elif metrics.lower() == "lbs":
    





















"""
while True:
    weight = float(input("Kindly enter your weight: "))
    unit = input("Is it in Kilograms (Kgs) or Pounds(Lbs)?: ")
    if unit.upper() == "KGS":
        weight * 0.45
        print("Your weight in Pounds is " + str(weight) + "Lbs.")
        break
    elif unit.upper() == "LBS":
        weight/0.45
        print("Your weight in Kilograms is " + str(weight) +"Kgs")
        break
    else:
        print("Type 'Kgs' or 'Lbs'")
"""
















'''
weight = input("What is your weight?: ")
while True:
    unit = input("Is it in Kilograms(Kgs) or Pounds(Lbs)? ")
    if unit.upper() == "KGS":
        pounds = float(weight) / 0.45
        print(f"Your weight in Pounds is {pounds}")
        break
    elif unit.upper() == "POUNDS":
        kilograms = float(weight) * 0.45
        print("Your weight in Kilograms is " + kilograms)
        break
'''