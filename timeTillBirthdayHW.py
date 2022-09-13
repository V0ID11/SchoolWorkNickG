import datetime
from time import strftime 

date = datetime.datetime.today()
print(f"Today's date is {date.day}/{date.month}/{date.year}") #finding current date and printing it

while True: #including error checking
    nextBirthday = input("Please enter the date of your next birthday separated by /: ") #input for next birthday
    Bday,Bmonth,Byear = nextBirthday.split("/") #dividing next birthday into separate segments then generateing a date out of them
    if int(Byear) < date.year:
        print("Make sure this birthday has not already happened")
    elif int(Bmonth) < date.month and date.year == int(Byear):
        print("Make sure this birthday has not already happened")
    elif int(Bday) < date.day and date.year == int(Byear) and date.month == int(Bmonth):
        print("Make sure this birthday has not already happened")
    else:
        break
fullBirthday = datetime.date(int(Byear),int(Bmonth),int(Bday))

endOfCurrentYear = datetime.date(date.year,12,31) #finding end of this year
if int(Byear)==int(date.year)+1:
    numOfDays = (int(endOfCurrentYear.strftime("%j"))-int(date.strftime("%j"))) + int(fullBirthday.strftime("%j"))
    #calculating number of days left in this year + number of days through the next year the birthday is
else:
    numOfDays = int(fullBirthday.strftime("%j")) - int(date.strftime("%j"))
    
if numOfDays == 0:
    print("Happy Birthday!")
else:
    print(f"Your Birthday is in {numOfDays} days!")