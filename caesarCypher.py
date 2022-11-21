trueAlphabet = 'abcdefghijklmnopqrstuvwxyz'
shiftedAlphabet = 'ghijklmnopqrstuvwxyzabcdef'
plainText ='T'
cipherText = ""

def generateAlphabet(shift):
    x = trueAlphabet[:shift]
    y = trueAlphabet[shift:]
    return y + x

def decrypt(msg, shift):
    shiftedAlphabet = generateAlphabet(shift)
    plainText = ""
    for i in msg:
        if i in shiftedAlphabet:
            place = shiftedAlphabet.index(i)
            plainText += trueAlphabet[place]
        else:
            plainText += i
    return plainText

shift = int(input("How Much do you want to shift by"))
shiftedAlphabet = generateAlphabet(shift)
print(shiftedAlphabet)

def encrypt(msg,shiftedAlphabet):
    msg = msg.lower()
    cipherText = ""
    for i in msg:
        if i in shiftedAlphabet:
            place = trueAlphabet.index(i)
            cipherText += shiftedAlphabet[place]
        else:
               cipherText += i
    return cipherText

toEncrypt = input("What do you want to encrypt")
shift = int(input("What to you want to shift by"))
x = encrypt(toEncrypt, generateAlphabet(shift))
print(x)
print(decrypt(x,shift))

