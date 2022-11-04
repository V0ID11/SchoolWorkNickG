import random
import math

def binSearch(items, toSearch):
    high = len(items) - 1
    low = 0
    found = False
    while found == False and low <= high:
        midpoint = math.ceil((low+high)/2)
        if items[midpoint] == toSearch:
            found = True
        elif items[midpoint] < toSearch:
            low = midpoint + 1
        elif items[midpoint] > toSearch:
            high = midpoint - 1
    if found == True:
        return f" found at {midpoint}"
    else:
        return " not in list"

if __name__ == "__main__":
    items = [random.randint(1,100) for i in range(20)]
    items.sort()
    print(items)
    for i in range(10):
        toFind = random.randint(1,100)
        print(toFind, binSearch(items, toFind))