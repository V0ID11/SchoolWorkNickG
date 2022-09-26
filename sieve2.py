import time
max = int(input("Enter Number you want to find primes to: "))
start = time.time()
boolnums = []
for i in range(2):
    boolnums.append(False)
for i in range(max - 2):
    boolnums.append(True)
current = 2
primes = [2]
while current + 1 < max:
    for i in range(current,max,current):
        boolnums[i] = False
    for i in range(current,max):
        if boolnums[i]:
            current = i
            primes.append(current)
            break

print(primes)
print("Elapsed: ", time.time() - start)