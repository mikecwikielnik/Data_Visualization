"""
I am trying to generate visualizations via random numbers (int or float)
"""

from cProfile import label
import random
from shutil import which
from turtle import color
import numpy as np
from matplotlib import pyplot as plt, ticker
from matplotlib import colors


xvalues = random.sample(range(0, 1000), 50)
yvalues = random.sample(range(0, 1000), 50)

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(xvalues, yvalues, s= 50, marker='X', edgecolors='black', label="randoms")
ax.set_xlim(0, 1100)
ax.set_ylim(0, 1100)
ax.set_xlabel("Random X's")
ax.set_ylabel("Random Y's")
ax.set_title("Beast Mode")
ax.legend(loc='upper left')
plt.show()
plt.clf()

plt.style.available