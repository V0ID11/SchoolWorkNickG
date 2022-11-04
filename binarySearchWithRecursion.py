import math
import random
def binarySearch(items, searchFor, high, low):
    midpoint = math.ceil((high+low)/2)
    
    
    if items[midpoint] == searchFor:
        return "Found"
    elif low > high:
        return "Not Found"
    elif items[midpoint] > searchFor:
        binarySearch(items,searchFor, midpoint-1,low)
    elif items[midpoint] < searchFor:
        binarySearch(items,searchFor,high,midpoint + 1)
        

if __name__ == "__main__":
    items = [random.randint(1,100) for i in range(50)]
    items.sort()
    print(items)
    for i in range(50):
        toFind = random.randint(1,100)
        print(i,toFind, binarySearch(items, toFind, len(items)-1, 0))
    