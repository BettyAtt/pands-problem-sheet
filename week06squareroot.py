# This program ask users to input  a positive floating point number
# and creates a function which output the input squared.
#Author: Betty Attwood

def NewtonMethod_sqrt(number, number_iters = 10):
    a = float(number) # number program gets square root of
    for i in range(number_iters): # have the number go 
        through above set number of iterations
        number = 0.5 * (number + a / number)
        # Newton's Method formula based on Medium reference: x_(n+1) = 0.5 * (x_n +a / x_n)
    return number

n = float(input("Enter a positive number: "))
if n < 0:
    print("Please enter a positive number")
    # this prevents user entering a negative number
else:
    answer = (NewtonMethod_sqrt(n))
    print("The approximate square root of {} is ".format(n) + str(round(answer,1)))