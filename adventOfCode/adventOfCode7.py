class Directory:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.total_size = 0
        self.file_sizes = 0
        self.parent = parent
        self.subdirs = []

    
    def totalSize(self):
        self.total_size = self.file_sizes
        for i in self.subdirs:
            self.total_size += i.totalSize()
        return self.total_size

    def __repr__(self) -> str:
        return f"[{self.name=}   {self.total_size=}  {self.subdirs=}]"

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
                    sizes.update({currentDirectory: currentDirectory.totalSize()})
                    currentDirectory = outerDirectory
                    
                elif i[2] == "..":
                    sizes.update({currentDirectory: currentDirectory.totalSize()})
                    currentDirectory = currentDirectory.parent
                else:
                    sizes.update({currentDirectory: currentDirectory.totalSize()})
                    currentDirectory = x
                    break

        elif i[0] == "dir":
            x = Directory(i[1],currentDirectory)
            currentDirectory.subdirs.append(x)
            count+=1

        elif i[0].isnumeric():
            currentDirectory.file_sizes += int(i[0])
        
    
print(count)
totalSize = 0
less100000 = []
greater100000 = []
for i in sizes:
    if sizes[i] < 100000:
        less100000.append(sizes[i])
        totalSize += sizes[i]
    elif sizes[i]>=100000:
        greater100000.append(sizes[i])
print(len(less100000) + len(greater100000))
print(totalSize)
            
print(outerDirectory)
    

