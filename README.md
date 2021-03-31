# pands-problem-sheet

___

# PANDS 2021 Problem Sheet for Weekly Tasks 

## Betty Attwood G00398300 January - April 2021

# Introduction

___

This ReadMe explains how the code works and provides references used to complete the weekly tasks for Programming and Scripting module for GMIT's Computer Science Data Analytics postgraduate degree. 

# Task 1:

___

### Task Description:
Please copy a link to your repository here (only the URL).

### Code:
Task 1 did not involve any code. Repository was created and file pushed. The url to my repository was submitted as https://github.com/BettyAtt/myWork

### Explaining the Code:
No coding for this task.

### References:
No references for this task.

# Task 2:
___

### Task Description:
Write a program that calculates somebody's Body Mass Index (BMI). Call the file bmi.py

The inputs are the person's height in centimetres and weight in kilograms.
The output  is their weight divided by their height in metres squared.

>$ python bmi.py
>Enter weight: 65
>Enter height: 180
>BMI is 20.06.


### Code:
    height = float (input ('Enter your height in cm: '))
    weight = float (input ('Enter your weight in kg: '))
    metersquared = (height/100)**2
    BMI = round(weight / metersquared, 2)
    print('Your BMI is {}'.format(BMI))

### Explaining the Code:
1. The user is prompted to enter height and weight as a float. 
2. The entered weight is divided by the entered height in meters to the power of two.
3. The output is printed. The code `.format(BMI)` fills in the placeholder `{}`with the BMI variable which calculates the BMI using the formula utilising the users inputs.

### References:
1. w3schools.com. 2020. Python String format() Method. [online] Available at: https://www.w3schools.com/python/ref_string_format.asp [Accessed 31 January 2021].
2. Vanderplas, J., n.d. 2016. A Whirlwind Tour Of Python. O'Reilly Media Inc. Available at: https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf [Accessed 31 January 2021].
3. Tintumon, M., M, K., Visser, S. and Nath, A., 2021. BMI Calculator In Python. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792 [Accessed 31 January 2021].
4. Diabetes Canada. 2021. How to Calculate Body Mass Index. Available at: https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator#:~:text=Body%20Mass%20Index%20is%20a,range%20is%2018.5%20to%2024.9. [Accessed 31 January 2021].

# Task 3:

___

### Task Description:
Write a program that takes asks a user to input a string and outputs every second letter in reverse order.

>$ python secondstring.py
>Please enter a sentence: The quick brown fox jumps over the lazy dog.
>.o zletrv pu o wr cu h

### Code:

### Explaining the Code:

### References:

# Task 4:

___

### Task Description:
Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

>$ python collatz.py
>Please enter a positive integer: 10
>10 5 16 8 4 2 1

### Code:

### Explaining the Code:

### References:

# Task 5:

___

### Task Description:
Write a program that outputs whether or not today is a weekday.

(You will need to search the web to find how you work out what day it is)

An example of running this program on a Thursday is given below.

>$ python weekday.py
>Yes, unfortunately today is a weekday.

>An example of running it on a Saturday is as follows:
>$ python weekday.py
>It is the weekend, yay!

### Code:

### Explaining the Code:

### References:


# Task 6:

___

### Task Description:
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).

I suggest that you look at the newton method at estimating square roots.

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.


>$ python squareroot.py
>Please enter a positive number: 14.5
>The square root of 14.5 is approx. 3.8.

### Code:

### Explaining the Code:

### References:

# Task 7:

___

### Task Description:
Write a program that reads in a text file and outputs the number of e's it contains.

The program should take the filename from an argument on the command line.

>$ python es.py moby-dick.txt
>116960

### Code:

### Explaining the Code:

### References:

# Task 8:

___

### Task Description:
Write a program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

Some marks will be given for making the plot look nice.

### Code:

### Explaining the Code:

### References:


