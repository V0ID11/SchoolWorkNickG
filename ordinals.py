
def ending(pos):
    if pos == '12' or pos == '11' or pos == '13':
        pos += 'th'
    elif pos[-1] == '1':
        pos += "st"
    elif pos[-1] == '2':
        pos+="nd"
    elif pos[-1] == '3':
        pos += 'rd'
    else:
        pos += "th"
    return pos

char = ""
while len(char) != 1:
    char = input("What letter do you want to find.").lower()
pos = ord(char) - ord("a") + 1
pos = str(pos)
print(ending(pos))