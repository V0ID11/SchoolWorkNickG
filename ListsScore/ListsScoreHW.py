#adds score to file
def newScore():
    scores = open("ListsScore/Scores.txt","a")
    name = input("Who would you like to enter a score for?")
    score = input("What is their score x/y: ")
    x,y = score.split("/") #splits to make a percentage so all scores can be compared equally
    score = (int(x)/int(y)) * 100
    scores.writelines(f"{name},{score}\n")
    print("\nComplete") 
    scores.close()
    
#generate average
def average():
    scores = open("ListsScore/Scores.txt", "r") 
    allScores = []
    x = scores.readlines()
    for i in x:
        y = i.split(',') #split so last percentage value can be used
        allScores.append(float(y[1]))
    print(f"\nAverage Score: {round(sum(allScores)/len(allScores),2)}%") #rounds the average to two decimal places
    scores.close()
    
#shows highscore  
def highscore():
    scores = open("ListsScore/Scores.txt","r")
    highName = ""
    highScore = 0
    x = scores.readlines()
    for i in x:
        y = i.split(',')
        if float(y[1]) > float(highScore):
            highScore = float(y[1])
            highName = y[0]
    print(f"\n{highName} has the highest score of {round(highScore,2)}%")
    scores.close()
#shows lowest score
def lowScore():   
    scores = open("ListsScore/Scores.txt","r")
    lowName = ""
    lowScore = 100
    x = scores.readlines()
    for i in x:
        y = i.split(',')
        if float(y[1]) < float(lowScore):
            lowScore = float(y[1])
            lowName = y[0]
    print(f"\n{lowName} has the lowest score of {round(lowScore,2)}%")
    scores.close()
#shows the scores in percentage order descending
def orderedScores():
    scores = open("ListsScore/Scores.txt","r")
    allScores = []
    x = scores.readlines()
    for i in x:
        y = i.split(',')
        allScores.append([y[0],y[1]])
    allScores.sort(key = lambda l:l[1], reverse=True) #lambda function returns the second value for each item in the 2d array so sorting can properly occur
    print('\n')                                       #for each item in the 2d array so sorting can properly occur
    for i in allScores:
        x,y = i[0],i[1]
        print(f"{x}, {round(float(y),2)}%")
    scores.close()
#generate a displayable menu
def Menu():
    end = False
    while not end:
        action = input("\n1.New Score \n2.Create Average\n3.Highest Score \n4.Lowest Score \n5.Ordered Scores \n6.Quit  ")
        if action == "1":
            newScore()
        elif action == "2":
            average()
        elif action == "3":
            highscore()
        elif action == "4":
            lowScore()
        elif action == "5":
            orderedScores()
        else:
            end = True

Menu()

