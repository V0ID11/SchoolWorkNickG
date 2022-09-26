import time
def sieve(max):
    AllNums = [i for i in range(2,max+1)] # generate list of numbers up to and including max
    primes = [2]
    NextNum = 2
    
    for y in range(1,max):
        for i in range(0,max+1,NextNum):
            if i in AllNums:
                AllNums.remove(i)
        if AllNums == []:
            break
        primes.append(AllNums[0])
        NextNum = AllNums[0]  
    print(primes)
        
        
start = time.time()
max = input("What Do you want to print the Primes Up to: ")
sieve(int(max))
print("Elapsed time:", time.time()-start)
