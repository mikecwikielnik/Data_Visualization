# 15-1. Cubes: A number raised to the third power is a cube. 

# Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 315). No Starch Press. Kindle Edition. 



from shutil import which
from tkinter import YView
from matplotlib import pyplot as plt
plt.style.available

# for i in range(1,4): # one off error
#     x = i**3
#     print(x)
    
x_values = range(5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# set the range for each axis
ax.axis([0, 5001, 0, 5001**3])

plt.show()


