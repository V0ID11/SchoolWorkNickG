class todo:
    def __init__(self):
        priority = []
        tasks = []   
        y = open("to-do-list.txt","r")
        lines = y.readlines()
        for i in lines:
            line = i.split(",")
            tasks.append(line[0])
            priority.append(int(line[1]))
        self.tasks = tasks
        self.priority = priority
    def add(self):
        task = input("What task needs to be added: ")
        pri = input("What is the priority of this task 1,2,3: ")
        try:
            x = self.priority.index(int(pri) + 1)
            self.tasks.insert(x, task)
            self.priority.insert(x,int(pri))
        except:
            if pri == 1:
                try:
                    x = self.priority.index(int(pri) + 2)
                    self.tasks.insert(x, task)
                    self.priority.insert(x,int(pri))
                except:
                    self.tasks.append(task)
                    self.priority.append(int(pri))
            elif pri == 2:
                self.tasks.append(task)
                self.priority.append(int(pri))
            else:
                self.tasks.append(task)
                self.priority.append(int(pri))
    def displayAll(self):
        x = "Task"
        y = "Priority"
        print(f"{x:>20}{y:>20}\n")
        for i in range(len(self.tasks)):
            print(f"{self.tasks[i]:>20}{self.priority[i]:>20}")
    def checkNext(self):
        print(f"{self.tasks[0]:>20}{self.priority[0]:>20}")
    def complete(self):
        self.priority.pop(0)
        self.tasks.pop(0)
    def Menu(self):
        end = False
        while not end:
            action = input("1.Add\n2.Display All \n3.Check Next \n4.Complete Task \n5.Quit ")
            if action == "1":
                self.add()
            elif action == "2":
                self.displayAll()
            elif action == "3":
                self.checkNext()
            elif action == "4":
                self.complete()  
            else:
                x = open("to-do-list.txt","w")
                for i in range(len(self.tasks)):
                    x.writelines(f"{self.tasks[i]},{self.priority[i]}\n")
                quit()



main = todo()
main.Menu()