import csv
class Engine:
    def __init__(self, name, weight, colour):
        self.name = name
        self.weight = weight
        self.colour = colour

    def addToCSV(self, file):
        file.write(f"{self.name},{self.weight},{self.colour}\n")

    def getForCSVImport(self):
        return [self.name,self.weight,self.colour]
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
        x = "Name,Weight,Colour\n"
        file.write(x)
        for e in engines_list:
            e.addToCSV(file)
        print("Complete")

def readFromFile():
    newEngineList = []
    with open("files/Engine_Data.csv", "r") as file:
        header = file.readline()
        for i in file:
            x = i.strip()
            newEngineList.append(Engine(x.split(",")[0],x.split(",")[1],x.split(",")[2]))
    print(newEngineList)

def writeWithImport():
    with open("files/Engine_Data.csv", "w", newline='') as file:
        engineWriter = csv.writer(file,delimiter=',', quotechar='"',quoting=csv.QUOTE_NONNUMERIC)
        engineWriter.writerow(['Name','Weight', 'Colour'])
        for i in engines_list:
            engineWriter.writerow(i.getForCSVImport())

def readWithImport():
    newEngineList = []
    with open("files/engine_Data.csv", "r") as file:
        engineReader = csv.reader(file, delimiter=',',quotechar='"', quoting = csv.QUOTE_NONNUMERIC)
        header = next(engineReader)
        for row in engineReader:
            newEngineList.append(Engine(row[0],row[1],row[2]))
        print(newEngineList)
x = input("Do you want to read or write from file r/w: ")
if x == "r":
    readWithImport()
elif x == "w":
    writeWithImport()
