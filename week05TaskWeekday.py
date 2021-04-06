# This program outputs whether or not 
# today is a weekday.
#Author: Betty Attwood

# import Python's module for datetime
import datetime

# pulling the date as day of the week
#https://www.w3schools.com/python/python_datetime.asp
today = datetime.date.today()
print("Today is ", today.strftime("%A"))


weekDay = datetime.datetime.today().isoweekday()
# From Python Docs datetime module. Today returns local datetime,
# isoweekday returns weekdays as integers 1-7 Monday=1, Sunday = 7

# using the int values of weekdays, 
# we can use all days with int values less than 6 are weekdays,
# everything else is weekend.
if weekDay < 6:
    print("Yes, unfortunately, today is a weekday.")
else:
    print("It is the weekend, yay!")