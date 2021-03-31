# This program asks user to input a string
# and outputs every second letter in reverse order
# Author: Betty Attwood


# asks user to input a string
rawString = input("please enter a sentence:")
# start and end are blank which means default 
# (0 and length of string)
# step is every second character
# negative means it starts at the end of the string
print(rawString[::-2])