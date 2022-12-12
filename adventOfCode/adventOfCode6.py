with open("adventOfCode/AOC6.txt","r") as file:
    string = file.readline()
    items = []
    for i in range(14):
        items.append(string[i])
    if len(set(items)) == len(items):
        print(1)
    for i in range(1,len(string)+1):
        items.pop(0)
        items.append(string[i+14])
        if len(set(items)) == len(items):
            print(set(items))
            print(items)
            print(i+15)
            break