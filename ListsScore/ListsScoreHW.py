

def newScore():
    scores = open("Scores.csv","a")
    name = input("Who would you like to enter a score for?")
    score = input("What is their score x/y: ")
    x,y = score.split("/")
    score = (int(x)/int(y)) * 100
    scores.write(f"{name},{score}")
    print("Complete")
    scores.close()
    Menu()

def average():
    scores = open("Scores.csv", "r")
    allScores = []
    x = scores.readline()
    for i in x:
        y = i.split(',')
        print(y)
        allScores.append(float(y[1]))
    print(f"{sum(allScores)/len(allScores)}%")
    scores.close()
    Menu()
    

def Menu():
    action = input("\n\n1.New Score \n2.Create Average \n3.Quit  ")
    if action == "1":
        newScore()
    elif action == "2":
        average()
    else:
        quit()

Menu()

