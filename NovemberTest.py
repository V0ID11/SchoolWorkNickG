def checkForWord(firstWord, secondWord):
    for i in firstWord:
        if i in secondWord:
            if secondWord.count(i) >= firstWord.count(i):
                continue
            else:
                return False
        else:
            return False
    return True


wordToFind = input(f"What word do you want to find: ")
wordToCheck = input(f"What word do you want to find {wordToFind} in: ")

x = checkForWord(wordToFind,wordToCheck)
if x == False:
    print("Word can't Be Made")
else:
    print("Word can be made")