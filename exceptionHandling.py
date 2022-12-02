usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']

class BadGuyError(Exception):
    pass

def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    try:
        number = int(usernumber)
    except ValueError:
        print("Not a valid number")
        number = 1 
    try:
        print("Welcome", usernames[number], "user number", number,".")
        try:
            if usernames[number] == "Mumm-Ra":
                raise BadGuyError
        except:
            print("Not Good Guy")
    except IndexError:
        print("That user does not exist")
        print( print("Welcome", usernames[1], "user number", 1,"."))
    try:
        division = 301 / number
    except ZeroDivisionError:
        print("Dividing by zero is not possible")
        division = 301
    print(f"301 divided by {number} = {division}")


while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)