
pairs = 0
with open("adventOfCode/AOC4.txt","r") as file:
    for i in file:
        elf1 = []
        elf2 = []
        i = i.strip("\n")
        x,y = i.split(",")
        elfBroken1 = x.split("-")
        elfBroken2 = y.split("-")
        for i in range(int(elfBroken1[0]),int(elfBroken1[1])+1):
            elf1.append(i)
        for i in range(int(elfBroken2[0]),int(elfBroken2[1])+1):
            elf2.append(i)
        print(elf1)
        for i in elf1:
            if i in elf2:
                pairs += 1
                break
        
print(pairs)
