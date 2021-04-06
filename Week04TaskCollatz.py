# This program asks the user to input a positive integer
# and outputs the results of a calculation based upon whether
# the integer is an even or odd 

collat = int(input("enter a positive integer: "))
while collat <= 0:
    print("Error!")
    collat = int(input("Enter a positive integer: "))

collatz = []  # I create a list to capture the entry 
# and ensuing calculation results
collatz.append(int(collat)) 
# appending adds the calculations to the list
# https://www.w3schools.com/python/ref_list_append.asp

# Reference: https://www.w3schools.com/python/python_while_loops.asp
while collat != 1:
    if collat % 2 == 0:
        collat = collat / 2 
        # this increment prevents loop continuing forever
    else:
        collat = ((collat * 3) + 1)
    collatz.append(int(collat))

print(collatz)
    
