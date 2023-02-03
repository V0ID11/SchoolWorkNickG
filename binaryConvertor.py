def convertToBin(number):
    x = number//2
    thing = ""
    if x > 1:
        thing += convertToBin(x)
        thing += str(number % 2)
    else:
        thing += "1"
    return thing
hex = "0123456789ABCDEF"
def convetToHex(number):
    x = number//16
    thing = ""
    
    thing += hex[x]
    thing += hex[(number % 16)]
        

    return thing

    

num = int(input("What number do you want? "))
print(convertToBin(num))
print(convetToHex(num))

