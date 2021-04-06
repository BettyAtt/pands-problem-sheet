# Write a program called plottask.py that 
# displays a plot of the functions f(x)=x, 
# g(x)=x2 and h(x)=x3 in the range [0, 4] 
# on the one set of axes.

import numpy as np
import matplotlib.pyplot as plt

# x-axis values:
x=np.arange(0.0,4.0,1.0) #range of 1-4; steps of 1
# y-axis values:
y1 = x     # f(x)
y2 = x**2  # g(x)
y3 = x**3  # h(x)

#plotting the points
#  color='blue', linestyle='solid', linewidth= 2,
        #marker='d', markerfacecolor='pink', markersize=6, label='f(x)')
plt.plot(y1, 'd-m', lw = 2, ms = 6, mec = 'hotpink', mfc = 'pink', label='f(x)')
plt.plot(y2, 'd:c', lw = 2, ms = 6, mec = 'hotpink', mfc = 'pink', label='g(x)')
plt.plot(y3, 'd:b', lw = 2, ms = 6, mec = 'hotpink', mfc = 'pink', label='h(x)')
# above plots the point, and sets line color, line type, linewidth, the marker 
# on the line at the point, the color of marker and marker size for each point.
# The label adds the name of the line and works in conjunction with the following code:

plt.title('f(x)[f(x)=x], g(x)[g(x)=x**2] and h(x)[h(x)=x**3]') # adds the plot title
plt.xlabel('X-axis') # names x-axis
plt.ylabel('Y-axis') # names y-axis


plt.legend() # displays labels in plots above
plt.show() # Depicts graphic representation of the plot
