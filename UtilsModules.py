def max_number(numbers):
    max = numbers[0]
    for no in numbers:
        if no > max:
            max = no
    print(max)
numbers = [6,1,5,7,8,1,10,13]
max_number(numbers)

def big_word(words):
    max = 0
    mname = ""
    for name in words:
        if len(name) > max:
            return name
words = ["BurnaBoy","Fireboy","BigWiz","Ruger"]
print(big_word(words))