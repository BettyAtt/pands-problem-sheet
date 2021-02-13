# This program asks the user to input a positive integer
# and outputs the results of a calculation based upon whether
# the integer is an even or odd 

number = int(input("enter a positive integer: "))
while number <= 0:
    print("Error!")
    number = int(input("enter a positive integer: "))

numbers = []  # I create a list to capture the entry 
# and ensuing calculation results
numbers.append(int(number)) 
# appending adds the calculations to the list
# https://www.w3schools.com/python/ref_list_append.asp

# Reference: https://www.w3schools.com/python/python_while_loops.asp
while number != 1:
    if number % 2 == 0:
        number = number / 2 
        # this increment prevents loop continuing forever
    else:
        number = ((number * 3) + 1)
    numbers.append(int(number))

print(numbers)
