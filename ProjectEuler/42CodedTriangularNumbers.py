def TriangleNumbers():
    triangleList = []
    for i in range(70):
        triangleList.append(0.5*i*(i+1))
    return triangleList

def ConvertWordToValues(word):
    sum = 0
    for i in word:
        sum += ord(i) - (ord("A")-1)
    return sum


with open("words.txt","r") as f:
    x = f.readline()
    x = x.split(",")
    finalWords = []
    for i in range(len(x)):
        y = x[i].replace('"','')
        finalWords.append(y)
print(finalWords)
triangleList = TriangleNumbers()
count = 0

for i in finalWords:
    if ConvertWordToValues(i) in triangleList:
        count+=1

print(count)



