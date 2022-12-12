def check(dir1, dir2, pointSize ):
    totalLeft = 0
    totalRight = 0
    if dir1 == '':
        return 0
    elif dir2 == '':
        return 0

    for i in dir1:
        totalLeft += 1
        if int(i) >= int(pointSize):
            break
        

    for i in dir2:
        totalRight += 1
        if int(i) >= int(pointSize):
            break
        
    #print(totalRight)
    #print(totalRight*totalLeft)  
    return totalRight*totalLeft

def checkHorizontal(line,vertical, point, vpos, pointSize):
    toRight = line[point+1:]
    toLeft = line[:point]
    toLeft = toLeft[::-1]
    x = check(toRight,toLeft, pointSize)
    toUp = vertical[:vpos]
    toDown = vertical[vpos+1:]
    #print([toDown])
    #print([toUp])
    toUp = toUp[::-1]
    
    y = check(toUp, toDown, pointSize)
    
    return x*y
    

total = 0       
with open("AOC8.txt", "r") as file:
    lines = []
    for i in file:
        lines.append(i.strip())
    
    for i in range(len(lines)):
        for x in range(len(lines[i])):
            thing = ""
            for z in range(len(lines)):
                thing += lines[z][x]
            b = checkHorizontal(lines[i],thing,x,i, lines[i][x])
            if b > total:
                total = b

    
print(total)
