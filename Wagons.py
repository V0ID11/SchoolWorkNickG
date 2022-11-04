
class Yard:
    def __init__(self) -> None:
        self.sidings = [Siding(), Siding(),Siding(),Siding()]
    
    def addWagon(self, siding,wagon):
        self.sidings[siding].push(wagon)
    
    def removeWagon(self,siding):
        return self.sidings[siding].pop()
    
    def __str__(self) -> str:
        return "\n".join([self.sidings[i].__str__() for i in range(len(self.sidings))])
    

class Siding:
    def __init__(self) -> None:
        self.wagons = [None]*30
        self.pointer = -1

    def push(self, wagon):
        if self.pointer == 29:
            raise Exception("Siding is Full")
        else:
            self.pointer += 1
            self.wagons[self.pointer] = wagon

    def pop(self):
        if self.pointer == -1:
            raise Exception("Queue Empty")
        else:
            a = self.wagons[self.pointer]
            self.wagons[self.pointer] = None
            self.pointer -= 1
            return a

    def __repr__(self):
        i = 0
        thing = []
        while i < 30 and self.wagons[i] != None :
            thing.append(self.wagons[i].get_Type())
            i += 1
        return ', '.join(thing)

        
class Wagon:
    def __init__(self, ownerName, weight,numOfWheels) -> None:
        self.ownerName = ownerName
        self.weight = weight
        self.numOfWheels = numOfWheels

    def __repr__(self):
        return f"Owner: {self.ownerName}\nWeight: {self.weight}\nWheels{self.numOfWheels}"

class OpenWagon(Wagon):
    def __init__(self,ownerName,weight,numOfWheels) -> None:
        super().__init__(ownerName,weight,numOfWheels)

    def get_Type(self):
        return "Open Wagon"    

    def __repr__(self):
        return f"Open Wagon\nOwner: {self.ownerName}\nWeight: {self.weight}\nWheels: {self.numOfWheels}"
        

class ClosedWagon(Wagon):
    def __init__(self, height, numberOfDoors, suitableForFoodstuffs, ownerName, weight, numOfWheels) -> None:
        super().__init__(ownerName, weight, numOfWheels)
        self.height = height
        self.numberOfDoors = numberOfDoors
        self.suitableForFoodstuffs = suitableForFoodstuffs
    
    def get_Type(self):
        return "Closed Wagon"

    def __repr__(self):
        return f"Closed Wagon\nOwner: {self.ownerName}\nWeight: {self.weight}\nWheels: {self.numOfWheels}\nHeight: {self.height}\nDoors: {self.numberOfDoors}\nSuitable For Food: {self.suitableForFoodstuffs}"

if __name__ == "__main__":
    
    yard = Yard()
    for x in range(4):
        for i in range(30):
            yard.addWagon(x,OpenWagon("James", 4.7,5))
    for x in range(4):
        for i in range(15):
            yard.removeWagon(x)
    

    print(yard)
    print(yard.removeWagon(3))