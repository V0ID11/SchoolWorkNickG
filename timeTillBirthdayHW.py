import datetime
from time import strftime 

date = datetime.datetime.today()
print(f"Today's date is {date.day}/{date.month}/{date.year}") #finding current date and printing it

nextBirthday = input("Please enter the date of your next birthday separated by /: ") #input for next birthday
Bday,Bmonth,Byear = nextBirthday.split("/") #dividing next birthday into separate segments then generateing a date out of them
fullBirthday = datetime.date(int(Byear),int(Bmonth),int(Bday))

endOfCurrentYear = datetime.date(date.year,12,31) #finding end of this year

numOfDays = (int(endOfCurrentYear.strftime("%j"))-int(date.strftime("%j"))) + int(fullBirthday.strftime("%j"))
print(numOfDays) #calculating number of days left in this year + number of days through the next year the birthday is