# This program ask users to input  a positive floating point number
# and creates a function which output the input squared.
#Author: Betty Attwood

def sqrt(number, number_iters = 2):
    a = float(number) # number program gets square root of
    # why choose a?
    for i in range(number_iters):
        #what the significance of i?
        number = 0.5 * (number + a / number)
        # Medium reference: x_(n+1) = 0.5 * (x_n +a / x_n)
        # I guess I don't understand math
    return number

n = float(input("Enter a positive number: "))
# why n here and a above?
if n < 0:
    print("Please enter a positive number")
    # this prevents user entering a negative number
    # can I repeat the above or loop back to it?
else:
    answer = (sqrt(n))
    print(round(answer,1))