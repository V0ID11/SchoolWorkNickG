import random

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value
    
    def addItem(self, toAdd):
        if self.data == toAdd:
            return

        elif toAdd < self.data:
            if self.left == None:
                self.left = Node(toAdd)
            else:
                self.left.addItem(toAdd)
        
        else:
            if self.right == None:
                self.right = Node(toAdd)
            else:
                self.right.addItem(toAdd)
    
    def findItem(self, toFind):
        
        if self.data == toFind:
            return True
        elif toFind < self.data:
            if self.left == None:
                return False
            else:
                return self.left.findItem(toFind)
        else:
            if self.right == None:
                return False
            else:
                return self.right.findItem(toFind)

    

test = [random.randint(1,100) for i in range(50)]
x = Node(test[0])
for i in (1,len(test)-1):
    x.addItem(test[i])
print(sorted(test))
for i in range(10):
    toFind = random.randint(1,100)
    print(toFind,": ",x.findItem(toFind))




