s = 10
a = 0
output = ""
while(a<=8):
    s -= 1
    a += 1
    space = '' * s
    star = '*' * a
    output = space + star
    print(output)