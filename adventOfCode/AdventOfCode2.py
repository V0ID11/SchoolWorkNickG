with open("adventOfCode/AOC2.txt", "r") as file:
    lines = file.readlines()

elf = []
me = []
for i in lines:
    x,y = i.split(" ")
    y.strip()
    me.append(y)
    elf.append(x)

wins = {"A":"Y", "B":"Z", "C":"X"}
score = 0
for i in range(len(me)):
    if me[i] == elf[i]:
        score += 3
    elif wins[elf[i]].upper() == me[i]:
        print(wins[elf[i]])
        score += 6
    if me[i] == "X":
        score += 1
    elif me[i] == "Y":
        score+=2
    else:
        score+=3
print(score)