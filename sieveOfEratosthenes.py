
import time

def sieve():
    x = 1
    max = int(input("Enter Number you want to find primes to: "))
    primes = []
    start = time.time()
    AllNums = [True]*max
    for i in range(3,max):
        if i % 2 == 0:
            AllNums[i] = False
    AllNums[0] = False
    AllNums[1] = False
    nextNum = 2
    while nextNum**2 <= max:
        for i in range(nextNum**2,max,nextNum):
            if AllNums[i] == True:
                AllNums[i] = False
        while AllNums[nextNum + x] != True:
            x += 1
        nextNum = nextNum+x
        x = 1
    for i in range(len(AllNums)):
        if AllNums[i] == True:
            primes.append(i)
    print("Number Of Primes:", len(primes))
    print("Elapsed: ", time.time() - start)

sieve()