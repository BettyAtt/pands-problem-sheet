# This program outputs whether or not 
# today is a weekday.
#Author: Betty Attwood

# import Python's module for datetime
import datetime

# pulling the date as day of the week
#https://www.w3schools.com/python/python_datetime.asp
today = datetime.date.today()
#print(today.strftime("%A"))

# create tuple for weekdays
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")

if today in weekDays:
    print("Yes, unfortunately, today is a weekday.")
else:
    print("It is the weekend, yay!")