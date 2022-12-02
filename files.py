def read_file(filename):
    with open(filename,"r") as file:
        x = file.readlines()
        for i in x:
            print(i, end = "")

def new_addition(filename, inp):
    with open(filename, "a") as file:
            file.write("\n" + inp)

fileName = input("What File do you want to read? ")
while True:
    again = input("Do you want to add to the file y/n")
    if again == "n":
        break
    add = input("What would you like to add: ")
    new_addition(fileName, add)
read_file(fileName)