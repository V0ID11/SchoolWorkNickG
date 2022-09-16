
def push(stack, pointer,highWaterMark):
    if testForFull(pointer,highWaterMark) == True:
        return
    else:
        addToStack = input("What do you want to add to the stack? ")
        pointer = len(stack) + 1
        stack.append(addToStack)
        return stack,pointer

def remove(stack,pointer,base):
    if testForEmpty(pointer,base) == True:
        return
    else:
        pointer = len(stack)-1
        stack.pop(-1)
        return stack, pointer

def peek(pointer,stack):
    print(stack[pointer-1])

def testForEmpty(pointer,base):
    if pointer == base:
        return True
    else:
        return False

def testForFull(pointer,highWaterMark):
    if pointer == highWaterMark:
        return True
    else:
        return False

def Menu(highWaterMark,base,pointer,stack):
    end = False
    while not end:
        pointer = len(stack)
        action = input("1.Push\n2.Pop \n3.Peek \n4.Test For Empty \n5.Test For Full \n6.Quit ")
        if action == "1":
            push(stack,pointer,highWaterMark)
            print(stack)
        elif action == "2":
            remove(stack,pointer,base)
            print(stack)
        elif action == "3":
            peek(pointer,stack)
        elif action == "4":
            print(testForEmpty(pointer,base))
        elif action == "5":
            print(testForFull(pointer, highWaterMark))      
        else:
            quit()


highWaterMark = 10
base = 0
pointer = 0
List = []
Menu(highWaterMark,base,pointer,List)