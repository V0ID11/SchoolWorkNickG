def isPrime(number):
    if number <= 1:
        return False
    squareroot = number**0.5
    for i in range(2,int(round(squareroot,0))+1):
        if number % i == 0:
            return False
    return True

primeList = []

for i in range(1000001):
    if isPrime(i) == True:
        primeList.append(i)

print(primeList[-6:])
