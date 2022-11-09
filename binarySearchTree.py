import random


class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value
    
    def addItem(self, toAdd):
        

        if toAdd < self.data:
            if self.left != None:
                print("left:",self.left)
                self.left.addItem(toAdd)
                
            else:
                self.left = Node(toAdd)
                print("left:",self.left)
                
        elif toAdd > self.data:
            if self.right != None:
                print("right:",self.right)
                self.right.addItem(toAdd)
                
            else:
                self.right = Node(toAdd)
                print("right:",self.right)

        elif self.data == toAdd:
            print(self)
            return
                
    def findItem(self, toFind):
        
        if self.data == toFind:
            return True
        elif toFind < self.data:
            if self.left != None:
                #print(self.left)
                x = self.left.findItem(toFind)
            else:
                return False
        else:
            if self.right != None:
                #print(self.right)
                x = self.right.findItem(toFind)
            else:
                return False
        return x
    def __str__(self) -> str:
        return f"{self.data}"

    

test = [random.randint(1,10000) for i in range(5000)]
Tree = Node(test[0])
print(Tree)
for i in range(1,len(test)):
    Tree.addItem(test[i])
print(sorted(test))
for i in range(100):
    toFind = random.randint(1,10000)
    print(toFind,": ",Tree.findItem(toFind))




