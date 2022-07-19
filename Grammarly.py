#Replace user input with better words form your dictionary.output
#You look beautiful -> You're absolutely gorgeous
Dic = {
    "You": "You're",
    "look": "Absolutely",
    "beautiful": "gorgeous"
    #"very very": "extremely"
}
vv = input("Enter message: ")
words = vv.split(" ")
output = ""
for w in words:
    output += Dic.get(w,w) + " "
print (output)








notes = ("""
message = input ("->")
box = message.split(" ")
Dic = {
    "You": "You're",
    "look": "absolutely",
    "beautiful": "gorgeous",
    "How": "Wagwan",
    "that": "dem",
    "side": "ends"
}
output = ""
for word in box:
    output += Dic.get(word, word) + " "
print(output)
""")