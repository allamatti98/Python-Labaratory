#draw a christmas tree 
def star_tree():
    import time
    s = 6
    a = 1
    output = ""
    for i in range (6):
        spaces = " " * s
        asterisks = "*" * a
        output = spaces + asterisks
        s -= 1
        a += 2
        print(output)

        trunk = ""
    for j in range (4):
        d = " " * 5
        e = "*" * 2
        trunk = d + e
        print(trunk)
        time.sleep(1)
star_tree()





















'''
def star_tree():
    import time
    s = 5
    a = 1
    output = ""
    for i  in range (6):
        sp = " " * s
        ast = "*" * a
        output = (sp + ast)
        s -= 1
        a += 2
        print (output)

    for i in range (5):
        s1 = 4 * " "
        a1 = 3 * "*"
        out = s1 + a1
        print(out)
        time.sleep(1)
star_tree()
'''