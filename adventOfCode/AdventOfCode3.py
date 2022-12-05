alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
with open("adventOfCode/AOC3.txt", "r") as file:
    y = file.readlines()
    firstelf = ""
    secondelf = ""
    thirdelf = ""

    total = 0

    for i in range(0,len(y),3):
        firstelf = y[i].strip()
        secondelf = y[i+1].strip()
        thirdelf = y[i+2].strip()
        for x in set(firstelf):
            if x in set(secondelf) and x in set(thirdelf):
                total += (alphabet.index(x)+1)
                break
        
            
print(total)