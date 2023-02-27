import timeit
def createLattice(gridSize):
    n = 2*gridSize
    r = gridSize
    choose = factorial(n)/(factorial(r)*factorial(n-r))
    return choose

def factorial(x):
    if x >1:
        result = x*factorial(x-1)
        return result   
    else:
        return 1
    




if __name__ == "__main__":
    start = timeit.timeit()
    print(createLattice(20))
    print(timeit.timeit()-start)