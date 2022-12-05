table = [['Q','F','M','R','L','W','C','V'],['D','Q','L'],['P','S','R','G','W','C','N','B'],
['L','C','D','H','B','Q','G'],['V','G','L','F','Z','S'],['D','G','N','P'],['D','Z','P','V','F','C','W'],
['C','P','D','M','S'],['Z','N','W','T','V','M','P','C']]

number = []
fromColumn = []
toColumn = []

with open("adventOfCode/AOC5.txt", "r") as file:
    lines = file.readlines()
    for i in lines:
        y = i.strip("\n")
        x = y.split(" ")
        print(x)
        number.append(x[1])
        fromColumn.append(x[3])
        toColumn.append(x[5])

for i in range(len(number)):
    for x in range(int(number[i])):
        table[int(toColumn[i])-1].append(table[int(fromColumn[i])-1][-int(number[i])+x])
        table[int(fromColumn[i])-1].pop(-int(number[i])+x)

printedList = []
for i in range(9):
    printedList.append(table[i][-1])

print("".join(printedList))