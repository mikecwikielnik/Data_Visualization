"""
DAT-610 scrap for final visualizations
"""


import csv
from fileinput import filename
from turtle import color
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
 

filename = 'iihs_data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get the names of the cars from this file
    cars, avgloss = [], []
    for row in reader:
        try:
            car = row[0]
            avglos = row[1]
        except NameError:
            print("error")
        else:
            cars.append(car)
            avgloss.append(avglos)

int(avgloss)
# Plot the cars 
fig = plt.figure(figsize = (5, 5))
plt.bar(cars, avgloss, color = 'maroon', width = 0.4)
plt.title("Titletown", fontsize = 25)
plt.xlabel("cars", fontsize = 16)
plt.ylabel("average loss", fontsize = 2)
plt.show()
           
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.bar([cars], , c='red', alpha=0.5)

# Format plot
# ax.set_title("title", fontsize=20)
# ax.set_xlabel('', fontsize=16)
# ax.set_ylabel("", fontsize=16)
# ax.tick_params(axis='both', which='major', labelsize=16)

