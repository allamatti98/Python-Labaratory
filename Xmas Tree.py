def star_tree()
    import time
    output = ""
    s = 8
    a = 1
    while a <= 13:
        spaces = " " * s
        stars = "*" * a
        output = spaces + stars
        print(output)
        s -= 1
        a += 2
    for i in range(4):
        print (" "*7 + "*"*2)
        time.sleep(1)

star_tree()