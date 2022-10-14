
class Node:
    def __init__(self,data,nextNode) -> None:
        self.data = data
        self.nextNode = nextNode
    
    def get_Data(self):
        return self.data
    
    def set_Next_Node(self,newNode):
        self.nextNode = newNode

class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.endNode = Node("Empty",0)
        self.headNode = self.endNode
        
    def Pop(self):
        if self.headNode == self.endNode:
            print("List Empty")
            return
        x = self.headNode
        self.headNode = self.headNode.nextNode
        del(x)
        self.size -= 1

    def Push(self):
        x = input("What data would you like the new node to contain")
        newNode = Node(x,self.headNode)
        self.headNode = newNode
        self.size += 1
    
    def displayAll(self):
        newHead = self.headNode
        display = []
        while newHead != self.endNode:
            display.append(newHead.get_Data())
            newHead = newHead.nextNode
        return display

linkedList = Stack()
linkedList.Push()
linkedList.Push()

print(linkedList.headNode.get_Data())
print(linkedList.displayAll())

