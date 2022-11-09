import random


def bubbleSort(toSort):
    length = len(toSort)
    swapped = False
    for i in range(0,length-1):
        if toSort[i] > toSort[i+1]:
            temp = toSort[i]
            toSort[i] = toSort[i+1]
            toSort[i+1] = temp
            swapped = True
    if swapped == False:
        return toSort
    if length > 2:
        x = toSort[-1]
        toSort = bubbleSort(toSort[0:length-1])
        toSort.append(x)
    
    return toSort

needsSorting = [random.randint(1,1000) for i in range(1000)]
print(needsSorting)
print(bubbleSort(needsSorting))
