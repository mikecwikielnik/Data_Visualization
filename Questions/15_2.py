# 15-2. Colored Cubes: Apply a colormap to your cubes plot.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 315). No Starch Press. Kindle Edition. 


from shutil import which
from tkinter import YView
from matplotlib import pyplot as plt
plt.style.available
    
x_values = range(5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# Set chart title and label axes
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# set the range for each axis
ax.axis([0, 5001, 0, 5001**3])

plt.show()


