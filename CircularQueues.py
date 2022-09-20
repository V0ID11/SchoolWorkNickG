class Queue:
    def __init__(self,lowPoint,queue,highPoint,WaterMark):
        self.lowPoint = lowPoint
        self.queue = queue
        self.highPoint = highPoint
        self.WaterMark = WaterMark 
    def testForFull(self):
        if self.highPoint == self.WaterMark:
            return True
        else:
            return False
    def testForEmpty(self):
        if self.lowPoint == self.highPoint:
            return True
        else:
            return False
    def push(self):
        if self.testForFull() == True:
            self.highPoint = 0
        
        add = input("What do you want to add to the Queue? ")
        self.queue[self.highPoint] = add
        self.highPoint += 1
        return
    def get(self):
        if self.testForEmpty() == True:
            print("Queue is empty")
            return
        else:
            self.queue[self.highPoint] = ''
            self.highPoint += 1
            return
    def menu(self):
        end = False
        while not end:
            action = input("1.Push \n2.Remove \n3.Test For Empty \n4.Test For Full \n5.Quit ")
            if action == "1":
                self.push()
                print(self.queue)
            elif action == "2":
                self.get()
                print(self.queue)
            elif action == "3":
                print(self.testForEmpty())
            elif action == "4":
                print(self.testForFull())      
            else:
                quit()
waterMark = 10
queue = ['']*waterMark
lowPoint = -1
highPoint = 0
Main = Queue(lowPoint,queue,highPoint,waterMark)
Main.menu()