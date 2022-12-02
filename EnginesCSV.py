class Engine:
    def __init__(self, name, weight, colour):
        self.name = name
        self.weight = weight
        self.colour = colour

    def addToCSV(self, file):
        file.write(f"{self.name},{self.weight},{self.colour}\n")


engines_list = []
engines_list.append(Engine('Thomas', 600, 'blue'))
engines_list.append(Engine('James', 650, 'red'))
engines_list.append(Engine('Edward', 1000, 'blue'))
engines_list.append(Engine('Gordon', 2500, 'blue'))
engines_list.append(Engine('Henry', 2100, 'green'))

with open("files/Engine_Data.csv", "w") as file:
    x = Engine("Name","Weight", "Colour")
    x.addToCSV(file)
    for e in engines_list:
        e.addToCSV(file)

