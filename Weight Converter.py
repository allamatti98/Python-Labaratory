weight = input("What is your weight? ")
while True:
    metrics = input("Is it in Kilograms (Kg) or Pounds(Lbs)")
    if metrics.upper() == "KGS":
        pounds = float(weight) /1.6
        print(f'Your weight in pounds is {pounds}')
        break
    elif metrics.lower() == "lbs":
        kilograms = float(weight) * 1.6
        print("Your weight in Kilograms is " + kilograms)
        break
    else:
        print("Type 'Kgs' or 'Lbs'")