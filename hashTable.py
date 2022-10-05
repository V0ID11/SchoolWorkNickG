table = ["-1"]*523

def hashTable(word):
    hash = 0
    for i in word:
        hash += ord(i) ** 2
    hash = hash % 523
    return hash

while True:
    word = input("What word would you like to place in the table: ")
    if word == "-1":
        break
    equivalent = input("What is the French Equivalent: ")
    table[hashTable(word)] = equivalent

while True:
    word = input("Enter the word you want to find in the hash table: ")
    if word == "-1":
        break
    print(table[hashTable(word)])
    