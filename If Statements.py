# --- If Statement 1 ---
def temp():
    city = input("In what city are you?: ")
    temperature = int(input("What is the temperature in " + city + "? "))
    if temperature > 25:
        print("""
        It's a hot day.
        Drink plenty of water.
        """)
    elif temperature < 15:
        print("""
        It's a cold day.
        Wear warm clothes.
        """)
    else:
        print(f"{temperature} degrees is okay, It's definately a good day in {city}")

def credit_score():
    price = 1_000_000
    credit = float(input("What is your credit score?: "))
    if credit > 300:
        print ("You are eligible for a loan.")
    else:
        print("You are not eligible for a loan.")

def loan_scheme():
    income = float(input("What is your weekly income?: "))
    credit = float(input("What is your credit score?: "))
    if income >= 50_000 and credit >= 300:
        print("You are eligible for a loan.")
    elif income >= 50_000 and credit < 300:
        print("Your income is good but your credit score is low.")
    elif income < 50_000 and credit >= 300:
        print("Your credit score is good but our salar is low.")
    else:
        print("You are not eligible for a loan")

#1. temp()
#2. credit_score()
#3. loan_scheme()