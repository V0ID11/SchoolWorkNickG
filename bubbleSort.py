import random


def bubbleSort(toSort):
    length = len(toSort)
    for i in range(0,length-1):
        if toSort[i] > toSort[i+1]:
            temp = toSort[i]
            toSort[i] = toSort[i+1]
            toSort[i+1] = temp
    if length > 2:
        x = toSort[-1]
        toSort = bubbleSort(toSort[0:length-1])
        toSort.append(x)
    
    return toSort

needsSorting = [random.randint(1,100) for i in range(50)]
print(needsSorting)
print(bubbleSort(needsSorting))
