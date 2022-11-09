import random


def bubbleSort(toSort):
    x = 1
    length = len(toSort)
    for u in range(length):
        swapped = False
        for i in range(0,length-x):
            if toSort[i] > toSort[i+1]:
                temp = toSort[i]
                toSort[i] = toSort[i+1]
                toSort[i+1] = temp
                swapped = True
        if swapped == False:
            return toSort
        x += 1
    
    
    return toSort

needsSorting = [random.randint(1,1000) for i in range(2000)]
print(needsSorting)
print(bubbleSort(needsSorting))
