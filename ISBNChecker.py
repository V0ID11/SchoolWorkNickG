ISBN = [None]*13
for count in range(13):
    ISBN[count] = int(input("What is the next digit in the code"))
#ISBN = [int(i) for i in input().split(", ")]

calculatedDigit = 0
count = 0

while count < 12:
    calculatedDigit += ISBN[count]
    count = count + 1
    calculatedDigit += ISBN[count] * 3
    count += 1

while calculatedDigit >= 10:
    calculatedDigit -= 10

calculatedDigit = 10 - calculatedDigit

if calculatedDigit == 10:
    calculatedDigit = 0

if calculatedDigit == ISBN[12]:
    print("Valid ISBN")
else:
    print("Invalid ISBN")
