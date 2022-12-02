with open("adventOfCode/AOC1.txt","r") as file:
    lines = file.readlines()

count = 0
Calories = []
for i in lines:
    if i == "\n":
        Calories.append(count)
        count = 0
    else:
        count += int(i.strip())

top3 = [0,0,0]
for x in Calories:
    if x > top3[0]:
        top3[2] = top3[1]
        top3[1] = top3[0]
        top3[0] = x
    elif x > top3[1]:
        top3[2] = top3[1]
        top3[1] = x
    elif x > top3[2]:
        top3[2] = x
    
print(sum(top3))