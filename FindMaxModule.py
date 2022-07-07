def find_max(numbers):
    maximum = numbers[0]
    for nos in numbers:
        if nos > maximum:
            maximum = nos
    print(maximum)