import random

difficulty =  int(input("What difficulty do you want 1,2 or 3")) #choose difficulty

if difficulty == 1: #condition to run the write difficulty
    highscore = open("easyHighscore.txt","a") #open file
    print(highscore)
    number = random.randint(1000,10000) #generate random number in correct range
    count  = 0
    while True: #loop till correct guess
        correctPlaces =  []
        count  += 1
        guess = int(input("Enter a number to guess")) #user inputs guess
        if guess == number:
            print(f"You won in {count} guesses")
            break
        else:
            for i in range(4):
                if str(guess)[i] == str(number)[i]:
                    correctPlaces.append(i) #list with the different numbered places in the number that are correct
            print(correctPlaces)
    usr = input("What is your name") #create a list of scores
    highscore.write(f"{usr},{count}\n")
    highscore.close()
elif difficulty == 2:
    highscore = open("highscore.txt","a") #open  file in a appendable state
    print(highscore)
    number = random.randint(1000,10000) #generate random number in middle difficulty range
    count  = 0  #create a count for number of guesses it takes
    while True: #run until correct answer is given
        correctPlaces =  0
        count  += 1 
        guess = int(input("Enter a number to guess")) #get the user to input a guess
        if guess == number: #check for correct guessss
            print(f"You won in {count} guesses") 
            break
        else:
            for i in range(4):
                if str(guess)[i] == str(number)[i]: #display number in correct position
                    correctPlaces += 1
            print(correctPlaces)
    usr = input("What is your name")
    highscore.write(f"{usr},{count}\n") #append name and number of guesses in correct position
    highscore.close() #close the file
elif difficulty == 3:
    highscore = open("hardHighscore.txt","a")

    print(highscore) 
    number = random.randint(10000,100000) #choose random number in the range
    count  = 0
    while True:
        correctPlaces =  0
        count  += 1
        guess = int(input("Enter a number to guess")) #user guess of number
        if guess == number:
            print(f"You won in {count} guesses")
            break
        else:
            for i in range(5):
                if str(guess)[i] == str(number)[i]: 
                    correctPlaces += 1
            print(correctPlaces) #number of guesses in correct place
    usr = input("What is your name") #enter name for high score list
    highscore.write(f"{usr},{count}\n")
highscore.close()

