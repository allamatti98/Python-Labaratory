def findmax(numbers):
    maximum = numbers[0]
    for nos in numbers:
        if nos > maximum:
            maximun = nos
    return maximum