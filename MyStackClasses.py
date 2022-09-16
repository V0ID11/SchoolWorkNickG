class stack:
    def __init__(self, stack, pointer, base, highWaterMark):
        self.stack = stack
        self.pointer = pointer
        self.base = base
        self.highWaterMark = highWaterMark
    def testForMax(self):
        if self.highWaterMark == self.pointer:
            return True
        else:
            return False

    def testForMin(self):
        if self.base == self.pointer:
            return True
        else:
            return False

    def push(self):
        if self.testForMax() == True:
            return
        else:
            add = input("What do you want to add to the stack? ")
            self.stack.append(add)
            self.pointer = len(self.stack)

    def remove(self):
        if self.testForMin() == True:
            return
        else:
            self.stack.pop()
            self.pointer = len(self.stack)
            
    def peek(self):
        print(self.stack[self.pointer-1])
    
    def menu(self):
        end = False
        while not end:
            action = input("1.Push\n2.Pop \n3.Peek \n4.Test For Empty \n5.Test For Full \n6.Quit ")
            if action == "1":
                self.push()
                print(stack)
            elif action == "2":
                self.remove()
                print(stack)
            elif action == "3":
                self.peek()
            elif action == "4":
                print(self.testForMin())
            elif action == "5":
                print(self.testForMax())      
            else:
                quit()

List = []
pointer = 0
base = 0
highWaterMark = 10
main = stack(List, pointer, base, highWaterMark)
main.menu()