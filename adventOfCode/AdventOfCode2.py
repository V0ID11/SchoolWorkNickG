with open("adventOfCode/AOC2.txt", "r") as file:
    lines = file.readlines()

elf = []
me = []
for i in lines:
    i = i.strip()
    x,y = i.split(" ")
    me.append(y)
    elf.append(x)

wins = {"A":"P", "B":"S", "C":"R"}
equal = {"A":"R", "B":"P", "C":"S"}
loss = {"A":"S", "B":"R", "C":"P"}
Scores = {"R":1, "P":2, "S":3}
choice = []
score = 0
for i in range(len(me)):
    if me[i] == "Y":
        score += 3
        choice.append(Scores[equal[elf[i]]])
    elif me[i] == "Z":
        score += 6
        choice.append(Scores[wins[elf[i]]])
    else:
        choice.append(Scores[loss[elf[i]]])
print(choice)
score += sum(choice)
    
print(score)