#Make a program that gives a player 3 chances to guess a magic number.
for i in range(3):
    answer = input("Guess the secret number: ")
    if answer == "9":
        print("Good Job!!!")
        break
    else:
        print("Wrong answer champ.")
else:
    print("Sorry, you're out of chances. :(")



















'''
for i in range (3):
    cc = int(input("Guess the magic number: "))
    if cc != 9:
        print("Sorry wrong answer.")
    else:
        print("Congz... You nailed it.")
        break
else:
    print("Sorry chances are done")

'''