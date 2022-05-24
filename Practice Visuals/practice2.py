"""
I am trying to create a bar graph
"""


from enum import unique
import random
from matplotlib import pyplot as plt
from matplotlib.axis import YAxis
from numpy import integer
from plotly.graph_objs import Bar, Layout
from plotly import offline


# A practice loop generating 10 random numbers
# n=0
# while n < 11:
#     print(random.randrange(1, 20))
#     n += 1

# A loop that doesn't use i in the program, i only counts    
integers = []
for i in range(10000):
    randnum = random.randrange(1, 101)
    integers.append(randnum)

# Counting each integer
frequencies = []
for i in integers:
    frequency = integers.count(i)
    frequencies.append(frequency)

"""
print(integers.count(2)) is a test to make sure our loop is working correctly
It should yield how many 2's are in the integers list.
frequencies should do this for all integers in integers. 
"""
# integers.count(2)

# figure 1, a beautiful bar graph

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.bar(integers, frequencies, label = "count of integers")
ax.set_xlim(45, 55)
ax.set_ylim(0, 200)
ax.set_xlabel("Random integers")
ax.set_ylabel("Count")
ax.set_title("Beast Mode")
ax.legend(loc='upper left')
plt.show()
plt.clf()

# figure 2, less appealing that figure 1

data = [Bar(x=integers, y=frequencies)]

x_axis_config = {'title': 'buckets'}
y_axis_config = {'title': 'count'}
my_layout = Layout(title='beastmode', 
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='barChart_scrap.html')

