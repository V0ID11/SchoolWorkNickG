from flask import Flask
from flask import request 
import datetime

app = Flask(__name__)

def calc_next_birthday(day,month,year):
    dob = datetime.date(int(year),int(month),int(day))
    today = datetime.date.today()

    
    birthday_this_year = datetime.date(today.year, dob.month, dob.day)
    birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = birthday_next_year

    nextBirthday = next_birthday.strftime("%d/%m/%Y")
    nextBirthday = f"Next birthday:  {nextBirthday}"
    days_to_birthday = (next_birthday - today).days
    age = (next_birthday - dob).days // 365     # Note, this doesn't take account of leap years so isn't perfect.
    numDays = f'Days to next birthday:  {days_to_birthday}'
    nextAge = f'Age at next birthday:  {age}'
    return nextBirthday,numDays,nextAge

@app.route("/DoB")
def dateOfBirth():
    year = request.args.get('year','')
    month = request.args.get('month','')
    day = request.args.get('day','')
    if day and month and year:
        return f"{day},{month},{year}"
    else:
        return "No Arguments Detected"

@app.route("/next_birthday")
def nextBirthday():
    year = request.args.get('year','')
    month = request.args.get('month','')
    day = request.args.get('day','')

    nextBirthday,numDays,nextAge = calc_next_birthday(day,month,year)
    print(nextBirthday)
    return f"{nextBirthday}<p>{numDays}<p>{nextAge}"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)