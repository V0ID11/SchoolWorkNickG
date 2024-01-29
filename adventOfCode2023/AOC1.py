f = open("AOC1.txt","r")
sums = 0
nums = ["0","1","2","3","4","5","6","7","8","9"]
for i in f:
    print(i)
    initial = -1
    final = -1
    counter = 0
    while initial == -1:
        print(i[counter])
        print(initial)
        try:
            x = int(i[counter])
            initial = i[counter]
            break
        except:
            counter +=1
    counter = -1
    while final == -1:
        try:
            x = int(i[counter])
            final = i[counter]
            break
        except:
            counter -=1
    x = str(initial) + str(final)
    print(x)
    sums += int(x)
print(sums)
