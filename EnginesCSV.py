class Engine:
    def __init__(self, name, weight, colour):
        self.name = name
        self.weight = weight
        self.colour = colour

    def addToCSV(self, file):
        file.write(f"{self.name},{self.weight},{self.colour}\n")
    def __repr__(self):
        return f"{self.name},{self.weight},{self.colour}"


engines_list = []
engines_list.append(Engine('Thomas', 600, 'blue'))
engines_list.append(Engine('James', 650, 'red'))
engines_list.append(Engine('Edward', 1000, 'blue'))
engines_list.append(Engine('Gordon', 2500, 'blue'))
engines_list.append(Engine('Henry', 2100, 'green'))
def writeToFile():
    with open("files/Engine_Data.csv", "w") as file:
        x = Engine("Name","Weight", "Colour")
        x.addToCSV(file)
        for e in engines_list:
            e.addToCSV(file)
        print("Complete")
def readFromFile():
    newEngineList = []
    with open("files/Engine_Data.csv", "r") as file:
        for i in file:
            x = i.strip()
            newEngineList.append(Engine(x.split(",")[0],x.split(",")[1],x.split(",")[2]))
    print(newEngineList[1:])

x = input("Do you want to read or write from file r/w: ")
if x == "r":
    readFromFile()
elif x == "w":
    writeToFile()
