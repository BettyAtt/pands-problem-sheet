# This program asks user to input a string
# and outputs every second letter in reverse order
# Author: Betty Attwood


#reverse_str = s[::-1]
#print(reverse_str)
# ref: https://www.journaldev.com/23584/python-slice-string#:~:text=The%20slicing%20starts%20with%20the,for%20any%20index%20'i'.
# Returns every 2nd item between position 6 to 1 in reverse order
# Ref: https://www.learnbyexample.org/python-string-slicing/
# S = 'ABCDEFGHI'
#print(S[6:1:-2])    # GEC
# added int before (lengthOfString) Ref: https://stackoverflow.com/questions/20733156/slice-indices-must-be-integers-or-none-or-have-index-method
rawString = input("please enter a sentence:")
lengthOfString = len(rawString)
print(rawString[int(lengthOfString):1:-2])