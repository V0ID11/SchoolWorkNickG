class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.total_size = 0
        self.file_sizes = 0
        self.parent = parent
        self.subdirs = []

        if parent != None:
            self.parent.subdirs.append(self)

    
    def totalSize(self):
        self.total_size = self.file_sizes
        for i in self.subdirs:
            self.total_size += i.totalSize()
        return self.total_size

    def __repr__(self) -> str:
        return f"[{self.name=}   {self.total_size=}  {self.subdirs=}]"

    def getSubDirs(self):
        return [j for i in self.subdirs for j in i.getSubDirs()] + [self]

count = 0
sizes = {}
with open("AOC7.txt", "r") as file:
    x = file.readline()
    x.strip("\n")
    a,b,c = x.split(" ")
    outerDirectory = Directory(c,None)
    currentDirectory = outerDirectory
    for i in file:
        i = i.strip("\n")
        i = i.split(" ")
        if i[0] == "$":
            if i[1] == "cd":
                if i[2] == "/":
                    currentDirectory = outerDirectory
                    
                elif i[2] == "..":
                    currentDirectory = currentDirectory.parent
                else:
                    currentDirectory = Directory(i[2], currentDirectory)
                    

        elif i[0].isnumeric():
            currentDirectory.file_sizes += int(i[0])

    print(outerDirectory)
    print(outerDirectory.getSubDirs())
    sizes = [i.totalSize() for i in outerDirectory.getSubDirs()]
        
    
print(count)
totalSize = 0
items = []
x = 70000000 - outerDirectory.totalSize()
x = 30000000 - x

for i in sizes:
    if i >= x:
        items.append(i)


print(min(items))


    

