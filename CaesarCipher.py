def encrypt(text,key):
    dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,
            'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
            'V':21,'W':22,'X':23,'Y':24,'Z':25,' ':26}
    characters = []
    for i in text.upper():
        characters.append(dict[i])
    for i in range(len(characters)):
        item = (characters[i]+key)%27
        characters[i] = list(dict.keys())[list(dict.values()).index(item)]
    return "".join(characters)

def decrypt(text,key):
    dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,
            'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
            'V':21,'W':22,'X':23,'Y':24,'Z':25,' ':26}
    characters = []
    for i in text.upper():
        characters.append(dict[i])
    for i in range(len(characters)):
        item = (characters[i]-key)%27
        characters[i] = list(dict.keys())[list(dict.values()).index(item)]
    return "".join(characters)

x = encrypt("What would you like to do at my house this evening",5)
y = decrypt(x,5)

print(x)
print(y)

