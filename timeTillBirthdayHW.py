import datetime
from time import strftime 

date = datetime.datetime.today()
print(f"Today's date is {date.day}/{date.month}/{date.year}") #finding current date and printing it

nextBirthday = input("Please enter the date of your next birthday separated by /: ") #input for next birthday
Bday,Bmonth,Byear = nextBirthday.split("/") #dividing next birthday into separate segments then generateing a date out of them
fullBirthday = datetime.date(int(Byear),int(Bmonth),int(Bday))

endOfCurrentYear = datetime.date(date.year,12,31) #finding end of this year and the year of next birthday
endOfBirthdayYear = datetime.date(int(Byear),12,31)

numOfDays = int(endOfCurrentYear.strftime("%j"))-int(date.strftime("%j"))+ (int(endOfBirthdayYear.strftime("%j")) -(int(endOfBirthdayYear.strftime("%j"))-int(fullBirthday.strftime("%j"))))
print(numOfDays) #total number of days in this year and birthday year - number of days through this year and when bitday is
#removes need to workout leap years.