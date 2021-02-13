# Weekly Task 1 (Week 02)
# This Program calculates a person's BMI.
# Author: Betty Attwood

height = float (input ('Enter your height in cm: '))
weight = float (input ('Enter your weight in kg: '))

#conversion of centimeters to meters squared
metersquared = (height/100)**2

#calculation of BMI
BMI = round(weight / metersquared, 2)

#BMI output
print('Your BMI is {}'.format(BMI))
