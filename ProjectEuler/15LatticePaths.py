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
    

import functools
@functools.cache
def recursiveSolution(m,n):
    if n == 0 or m == 0: 
        return 1

    return recursiveSolution(m,n-1)+recursiveSolution(m-1,n)

def iterativeSolution(m,n):
    grid = [["" for i in range(m+1)] for i in range (n+1)]

    for i in range(m+1):
        
        grid[i][0] = 1
    
    for j in range(n+1):
        grid[0][j] = 1

    for i in range(1,m+1):
        for j in range(1,n+1):
            grid[i][j] = int(grid[i-1][j])+int(grid[i][j-1])

    return grid[m][n]
 



if __name__ == "__main__":
    start = timeit.timeit()
    print(createLattice(20))
    # print(recursiveSolution(15,15))
    # print(iterativeSolution(20,20))
    # print(timeit.timeit()-start)